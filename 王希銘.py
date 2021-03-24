import random
print("恭喜你收到浪漫霸主王希銘")
print("你的每個行動都會影響希銘的人生")
health = random.randint(50,80)
strong = 0
happy = 30
fat = random.randint(50,80)
hunger = 50
class Petlist():
    def __init__(self,health,strong,happy,fat,hunger):
        self.health = health
        self.strong = strong
        self.happy = happy
        self.fat = fat
        self.hunger = hunger

pet = Petlist(health,strong,happy,fat,hunger)

day=[0]
def sleep():
    pet.health +=4
    pet.fat -=2
    pet.hunger -=5
def training():
    pet.health +=1
    pet.strong +=3
    pet.happy -=4
    pet.fat -=1
    pet.hunger -=4 
def exercise():
    pet.health +=1
    pet.strong +=1
    pet.happy -=4
    pet.fat -=3
    pet.hunger -=4
def feeding():
    pet.fat +=5
    pet.hunger +=10
def play():
    pet.health -=4
    pet.happy +=8
def Action():
    print("拍抖音(A)洗澡(B)騎浪漫Force(C)吃響食天堂(D)騷擾妹子約浪漫(E)")
    action=str(input("請選擇動作"))
    if action == "A":
        sleep()
        day[0]+=1
    elif action =="B":
        training()
        day[0]+=1
    elif action =="C":
        exercise()
        day[0]+=1
    elif action =="D":
        feeding()
        day[0]+=1
    elif action =="E":
        play()
        day[0]+=1
    else:
        print("未知動作，請重新輸入")
while 1:
    Action()
    print("寵物數值:")
    print("唐氏症程度度:",pet.health,"衛生度",pet.strong,"浪漫度",pet.happy,"肥胖度",pet.fat,"飢渴度",pet.hunger)
    if pet.health <= 0:
        print("希銘唐氏症末期往生了 恭喜你")
        print("生存天數:",day[0],"天")
        break
    elif pet.strong >=100:
        print("恭喜養成一隻超級浪漫的霸主希銘!!")
        print("成就達成花了",day[0],"天")
        continue
    elif pet.happy <=0:
        print("霸主太久沒騎車 在台七乙壓彎撞到電線杆死了 恭喜你")
        print("生存天數:",day[0],"天")
        break
    elif pet.happy >=100:
        print("恭喜養成一隻超級浪漫的優質霸主希銘!!")
        print("成就達成花了",day[0],"天")
        continue
    elif pet.fat <=0:
        print("王希銘太久沒吃東西餓死了 恭喜你")
        print("生存天數",day[0],"天")
        break
    elif pet.fat >=100:
        print("王希銘肥死了 恭喜你")
        print("生存天數:",day[0],"天")
        break
    elif pet.hunger <=0:
        print("王希銘霸主被警方依性騷擾罪逮捕了 恭喜")
        print("生存天數:",day[0],"天")
        break
    elif pet.hunger >=100:
        print("王希銘獨自尻尻暗自sad猝死了 恭喜你")
        print("生存天數:",day[0],"天")
        break
    else:
        continue
