'''
Author: qiuyelengyusw qiuyelengyu@qq.com
Date: 2023-05-02 09:54:12
LastEditors: qiuyelengyusw qiuyelengyu@qq.com
LastEditTime: 2023-05-02 10:34:33
FilePath: \MyPythonProject\while循环.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import time  #定义一个时间函数，用import 调取
player_lift = 350  #设定玩家血量值
player_attack = 20  #设定玩家攻击力
enemy_lift = 400  #设定敌人血量值
enemy_attack = 12  #设定敌人攻击力
while player_lift > 0 and enemy_lift > 0:    #当玩家血量与敌人血量都大于零时运行循环
    player_lift = player_lift - enemy_attack  #玩家血量等于玩家原来的血量减去敌人攻击力
    enemy_lift = enemy_lift - player_attack   #敌人血量等于敌人原来的血量减去玩家攻击力
    print("the enemy launch an attack,the player's blood:" + str(player_lift))
    print("the player launch an attack,the enemy's blood:" + str(enemy_lift))
    time.sleep(1) #暂停2秒
if player_lift > 0 >= enemy_lift:  #如果玩家的血量大于零并且敌人的血量小于等于零的时候，判定玩家获胜
    print("The player Win!")
else:     #反之则判断敌人获胜
    print("The enemy Win")  #输出结果
    print("Game Over")  #游戏结束