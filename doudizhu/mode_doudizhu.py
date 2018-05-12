'''
    模拟斗地主发牌，共５４张
    黑桃('\u2660'),梅花('\u2663'),方块('\u2666'),红桃('\u2665'),
    种类：A2~10JQK
    三人每人17张，底牌3张
        输入回车，打印第一个人的17张牌
        输入回车，打印第二个人的17张牌
        输入回车，打印第三个人的17张牌
        输入回车，打印３张底牌(要求每次不一样)
'''

import random
# 黑桃：2660  梅花：2663  方块：2666  红心：2665  大王:265a 小王：265b
hua = ['\u2660','\u2663','\u2665','\u2666']
dian = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

L = ['\u265a','\u265b']
for i in hua:
    for j in dian:
        L.append(i + ' ' + j)

random.shuffle(L)

k = 0
while True:
    print() 
    p = input("按<enter>键即可看到玩家的牌!")
    k += 1
    if not p:
        player = random.sample(L,17)
        player.sort()
        print("玩家%d牌为：%s" % (k,player))
        for n in player:
            L.remove(n)
    if k == 3:
        print()
        print("底牌为：",L)
        break
