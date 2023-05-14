import random
class Student:
    def __init__(self, name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.money=5000
        self.alive=True
        self.stipyha=0
    def to_study(self):
        print("Час нвачитись!")
        self.progress+=0.12
        self.gladness-=3
        self.stipyha+=100
    def to_chill(self):
        print("Час відпочити!")
        self.gladness+=5
        self.progress-=0.1
    def to_sleep(self):
        print("Час спати!")
        self.gladness+=3
    def to_working(self):
        print("За роботу.")
        self.money+=100
        self.gladness-=2
    def is_alive(self):
        if self.progress<-0.5:
            print('Відрахували...')
            self.alive=False
        elif self.gladness<=0:
            print('Депресія...')
            self.alive=False
        elif self.progress>5:
            print('Закінчив естерном')
            self.alive=False
        elif self.money<=0:
            print('Банкрот')
            self.alive=False
    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress,2)}")
        print(f"Money - {round(self.money,2)}")
        print(f"Stependia - {round(self.stipyha, 2)}")
    def live(self, day):
        day="Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube=random.randint(1,4)
        if live_cube==1:
            self.to_study()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_chill()
        elif live_cube==4:
            self.to_working()
        self.end_of_day()
        self.is_alive()
nick=Student(name="Nick")
for day in range(365):
    if nick.alive==False:
        break
    nick.live(day)
