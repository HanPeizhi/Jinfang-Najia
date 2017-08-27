liuShenWuXing = {'甲': 0, '乙': 0, '丙': 1, '丁': 1,
                 '戊': 2, '己': 3, '庚': 4, '辛': 4,
                 '壬': 5, '癸': 5} #0->木  1->火 #唯一要注意的是：戊->勾陈，己->螣蛇

liuShen = ('青龙', '朱雀', '勾陈', '螣蛇', '白虎', '玄武')

baGua = {'111': '乾', '011': '兑', '101': '离', '001': '震',
         '110': '巽', '010': '坎', '100': '艮', '000': '坤'}

baGuaWuXing = {
    '乾': '金',
    '兑': '金',
    '离': '火',
    '震': '木',
    '巽': '木',
    '坎': '水',
    '艮': '土',
    '坤': '土'
}

wuXingShu = {
    '木': 1,
    '水': 2,
    '金': 3,
    '火': 4,
    '土': 5
}

# 六神, 根据日干五行配对六神五行
def setLiuShen(inStr):  # -> 日干支
    index = liuShenWuXing[inStr[0]]
    return liuShen[index:] + liuShen[:index]


'''
认宫诀：
一二三六外卦宫，四五游魂内变更。
若问归魂何所取，归魂内卦是本宫。'''

# 一二三六外卦宫
def neiGuaGong(inStr):
    return baGua[inStr[3:6]]

# 归魂内卦是本宫
def waiGuaGong(inStr):
    return baGua[inStr[:3]]

# 寻宫诀,四五游魂内变更          '123456'
def neiGuaBinNot(inStr):  # -> '111000'
    if len(inStr) == 6: s = inStr[3:6]
    else: s = inStr
    return baGua[''.join([str(int(c)^1) for c in s])]  #.replace(' ','')



'''
寻世诀：
天同二世天变五，地同四世地变初。
本宫六世三世异，人同游魂人变归。

1. 天同人地不同世在二，天不同人地同在五
2. 三才不同世在三
3. 人同其他不同世在四，人不同其他同在三'''

# 寻世诀： 天同二世天变五  地同四世地变初  本宫六世三世异  人同游魂人变归
# int('111', 2) => 7
# 世爻 >= 3, 应爻 = 世爻 - 3， index = 5 - 世爻 + 1
# 世爻 <= 3, 应爻 = 世爻 + 3，
def setShiYao(inStr):
    waiGuaNum = inStr[:3]
    neiGuaNum = inStr[3:]
    global youguiHun
    # 天同二世天变五
    if waiGuaNum[0] == neiGuaNum[0]:
        if waiGuaNum[1] != neiGuaNum[1] and waiGuaNum[2] != neiGuaNum[2]: return 2
    else:
        if waiGuaNum[1] == neiGuaNum[1] and waiGuaNum[2] == neiGuaNum[2]: return 5
    # 人同游魂人变归
    if waiGuaNum[1] == neiGuaNum[1]:
        if waiGuaNum[0] != neiGuaNum[0] and waiGuaNum[2] != neiGuaNum[2]:
            youguiHun = '游魂'; return 4 #, youguiHun
    else:
        if waiGuaNum[0] == neiGuaNum[0] and waiGuaNum[2] == neiGuaNum[2]:
            youguiHun = '归魂'; return 3 #, youguiHun
    # 地同四世地变初
    if waiGuaNum[2] == neiGuaNum[2]:
        if waiGuaNum[1] != neiGuaNum[1] and waiGuaNum[0] != neiGuaNum[0]: return 4
    else:
        if waiGuaNum[1] == neiGuaNum[1] and waiGuaNum[0] == neiGuaNum[0]: return 1
    # 本宫六世
    if waiGuaNum == neiGuaNum: return 6
    # 三世异
    if not int(waiGuaNum, 2) & int(neiGuaNum, 2): return 3
    # print(int('101', 2) & int('010', 2)) # 0

    # return waiGuaNum

# 纳天干地支用，其实不用这步也可以
def getNeiWaiGua(inStr):  # -> '111000'
    return  baGua[inStr[:3]] + baGua[inStr[3:]]  # 外卦 + 内卦


# 纳甲口诀：
# 乾金甲子外壬午 子寅辰午申戌 
# 震木庚子外庚午 子寅辰午申戌 
# 坎水戊寅外戊申 寅辰午申戌子 
# 艮土丙辰外丙戌 辰午申戌子寅 
# 坤土乙未外癸丑 未巳卯丑亥酉 
# 巽木辛丑外辛未 丑亥酉未巳卯 
# 离火巳卯外巳酉 卯丑亥酉未巳 
# 兑金丁巳外丁亥 巳卯丑亥酉未
# 外乾内坤
naZhiBiao = {
    '乾': {
        0: '子寅辰',   # 内卦
        1: '午申戌'    # 外卦
    },
    '震': {0: '子寅辰', 1: '午申戌'},
    '坎': {0: '寅辰午', 1: '申戌子'},
    '艮': {0: '辰午申', 1: '戌子寅'},
    '坤': {0: '未巳卯', 1: '丑亥酉'},
    '巽': {0: '丑亥酉', 1: '未巳卯'},
    '离': {0: '卯丑亥', 1: '酉未巳'},
    '兑': {0: '巳卯丑', 1: '亥酉未'}
}

# naGan[八卦][内外卦]
naGanBiao = {
    '乾': {
        0: '甲',  # 内卦
        1: '壬'   # 外卦
    },
    '坤': {0: '乙', 1: '癸'},
    '震': {0: '庚', 1: '庚'},
    '坎': {0: '戊', 1: '戊'},
    '艮': {0: '丙', 1: '丙'},
    '巽': {0: '辛', 1: '辛'},
    '离': {0: '己', 1: '己'},
    '兑': {0: '丁', 1: '丁'}
}

# 纳地支
def naZhi(inStr):  # -> '111000' -> 乾坤; naiWaiGua[0] -> 乾 外卦
    neiWaiGua = getNeiWaiGua(inStr)
    return naZhiBiao[neiWaiGua[0]][1], naZhiBiao[neiWaiGua[1]][0]


# 纳天干
def naGan(inStr):
    neiWaiGua = getNeiWaiGua(inStr)
    return naGanBiao[neiWaiGua[0]][1], naGanBiao[neiWaiGua[1]][0]


#def naLiuQin(inStr):

zhiWuXing = {
    '子': '水',
    '丑': '土',
    '寅': '木',
    '卯': '木',
    '辰': '土',
    '巳': '火',
    '午': '火',
    '未': '土',
    '申': '金',
    '酉': '金',
    '戌': '土',
    '亥': '水'
}




if __name__ == '__main__':
    # youguiHun = ''
    # print(setLiuShen('甲'))  # ['青龙', '朱雀', '勾陈', '螣蛇', '白虎', '玄武']
    # print(getNeiWaiGua('111000'))  # 乾坤
    # neiWaiGua = getNeiWaiGua('111000')
    # print(naGanBiao[neiWaiGua[0]][0])  # 甲

    # print(naZhi('111000'), naGan('111000'))

    waigu_tiangan = naGan('111000')[0] # 外卦天干
    waigua_dizhi = naZhi('111000')[0] # 外卦地支
    yao_4_ganzhi = waigu_tiangan + waigua_dizhi[0] + zhiWuXing[waigua_dizhi[0]]
    yao_5_ganzhi = waigu_tiangan + waigua_dizhi[1] + zhiWuXing[waigua_dizhi[1]]
    yao_6_ganzhi = waigu_tiangan + waigua_dizhi[2] + zhiWuXing[waigua_dizhi[2]]

    neigua_tiangan = naGan('111000')[1] # 内卦天干
    neigua_dizhi = naZhi('111000')[1] # 内卦地支
    yao_1_ganzhi = neigua_tiangan + neigua_dizhi[0] + zhiWuXing[neigua_dizhi[0]]
    yao_2_ganzhi = neigua_tiangan + neigua_dizhi[1] + zhiWuXing[neigua_dizhi[1]]
    yao_3_ganzhi = neigua_tiangan + neigua_dizhi[2] + zhiWuXing[neigua_dizhi[2]]

    # print(waigu_tiangan, neigua_tiangan)
    # print(waigua_dizhi)
    print(yao_6_ganzhi)
    print(yao_5_ganzhi)
    print(yao_4_ganzhi)
    print(yao_3_ganzhi)
    print(yao_2_ganzhi)
    print(yao_1_ganzhi)

    print(zhiWuXing['未'])


    print(setShiYao('101101')) # 世6爻
    # print(naZhiBiao['乾'][0])  #子寅辰

    print(neiGuaBinNot('111000')) # 乾
    print(waiGuaGong('111000')) # 乾
    print(neiGuaGong('111000')) # 坤