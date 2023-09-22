import random
class Student:
    def __init__(self, name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True
    def to_study(self):
        print("Час навчитись!")
        self.progress+=0.12
        self.gladness-=8
    def to_chill(self):
        print("Час відпочити!")
        self.gladness+=5
        self.progress-=0.1
    def to_sleep(self):
        print("Час спати!")
        self.gladness+=3
    def to_itschool(self):
        print("Час навчатися в айті школі")
        self.progress+=0.12
        self.gladness+=0.1
    def is_alive(self):
        if self.progress< -0.5:
            print('Відрахували...')
            self.alive=False
        elif self.gladness<=0:
            print('Депресія...')
            self.alive=False
        elif self.progress>5:
            print('Закінчив естерном')
            self.alive=False

    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress,2)}")
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
        else:
            self.to_itschool()
        self.end_of_day()
        self.is_alive()
yarik=Student(name="Yarik")
for day in range(365):
    if yarik.alive==False:
        break
    yarik.live(day)
