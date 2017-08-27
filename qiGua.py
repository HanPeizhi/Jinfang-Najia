liuShenWuXing = {'甲': 0, '乙': 0, '丙': 1, '丁': 1,
                 '戊': 2, '己': 3, '庚': 4, '辛': 4,
                 '壬': 5, '癸': 5} #0->木  1->火 #唯一要注意的是：戊->勾陈，而己->螣蛇

liuShen = ('青龙', '朱雀', '勾陈', '螣蛇', '白虎', '玄武')

baGua = {'111': '乾', '011': '兑', '101': '离', '001': '震',
         '110': '巽', '010': '坎', '100': '艮', '000': '坤'}


# 六神, 根据日干五行配对六神五行
def setLiuShen(inStr):  # -> 日干支
    index = liuShenWuXing[inStr[0]]
    return liuShen[index:] + liuShen[:index]


# 寻宫诀,四五游魂内变更
def doNeiGuaBinNot(inStr):  # -> '111000'
    if len(inStr) == 6: s = inStr[3:6]
    else: s = inStr
    return ''.join([str(int(c)^1) for c in s])  #.replace(' ','')


# 寻世诀： 天同二世天变五  地同四世地变初  本宫六世三世异  人同游魂人变归
# int('111', 2) => 7
# 世爻 >= 3, 应爻 == 世爻 - 3， index = 5 - 世爻 + 1
# 世爻 <= 3, 应爻 == 世爻 + 3，
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
            youguiHun = '游魂'; return 4
    else:
        if waiGuaNum[0] == neiGuaNum[0] and waiGuaNum[2] == neiGuaNum[2]:
            youguiHun = '归魂'; return 3
    # 地同四世地变初
    if waiGuaNum[2] == neiGuaNum[2]:
        if waiGuaNum[1] != neiGuaNum[1] and waiGuaNum[0] != neiGuaNum[0]: return 4
    else:
        if waiGuaNum[1] == neiGuaNum[1] and waiGuaNum[0] == neiGuaNum[0]: return 1
    # 本宫六世三世异
    if waiGuaNum == neiGuaNum: return 6
    if not int(waiGuaNum, 2) & int(neiGuaNum, 2): return 3

    # return waiGuaNum


def getNeiWaiGua(inStr):  # -> '111000'
    return  baGua[inStr[:3]] + baGua[inStr[3:]]  # 外卦 + 内卦


# 纳甲口诀：
# 乾金甲子外壬午 子寅辰午申戍 
# 震木庚子外庚午 子寅辰午申戍 
# 坎水戊寅外戊申 寅辰午申戍子 
# 艮土丙辰外丙戍 辰午申戍子寅 
# 坤土乙未外癸丑 未巳卯丑亥酉 
# 巽木辛丑外辛未 丑亥酉未巳卯 
# 离火巳卯外巳酉 卯丑亥酉未巳 
# 兑金丁巳外丁亥 巳卯丑亥酉未
# 外乾内坤
naZhiBiao = {
    '乾': {
        0: '子寅辰',   # 内卦
        1: '午申戍'    # 外卦
    },
    '震': {0: '子寅辰', 1: '午申戍'},
    '坎': {0: '寅辰午', 1: '申戍子'},
    '艮': {0: '辰午申', 1: '戍子寅'},
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
def naZhi(inStr):  # -> '111000'
    neiWaiGua = getNeiWaiGua(inStr)
    return naZhiBiao[neiWaiGua[0]][1], naZhiBiao[neiWaiGua[1]][0]


# 纳天干
def naGan(inStr):
    neiWaiGua = getNeiWaiGua(inStr)
    return naGanBiao[neiWaiGua[0]][1], naGanBiao[neiWaiGua[1]][0]



if __name__ == '__main__':
    #youguiHun = ''
    # print(setLiuShen('甲'))  # ['青龙', '朱雀', '勾陈', '螣蛇', '白虎', '玄武']
    # print(getNeiWaiGua('111000'))  # 乾坤
    # neiWaiGua = getNeiWaiGua('111000')
    # print(naGanBiao[neiWaiGua[0]][0])  # 甲
    # print(naZhi('111000'), naGan('111000'))
    #print(doNotBin('111000'))
    print(setShiYao('101101')) #6
    print(naZhiBiao['乾'][0])  #子寅辰