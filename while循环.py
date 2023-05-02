import time
player_lift = 350
player_attack = 20
enemy_lift = 400
enemy_attack = 12
while player_lift > 0 and enemy_lift > 0:
    player_lift = player_lift - enemy_attack
    enemy_lift = enemy_lift - player_attack
    print("the enemy launch an attack,the player's blood:" + str(player_lift))
    print("the player launch an attack,the enemy's blood:" + str(enemy_lift))
    time.sleep(2)
if player_lift > 0 >= enemy_lift:
    print("The player Win!")
else:
    print("The enemy Win")
