import random

class cat:
    def __init__(self, name):
        self.name=name
        self.food = 50
        self.gladness = 50
        self.alive = True
    def to_sleep(self):
        print("Time to sleep")
        self.gladness+=3
    def to_drinkmilkandeatfood(self):
        print("Time to eat")
        self.food+=1
    def to_play(self):
        print("Time to play")
        self.gladness+=2
    def to_destroyfurniture(self):
        print("Time to destroy the furniture!")
        self.gladness+=3
    def is_alive(self):
        if self.gladness<0:
            print("Cat is in depression")
            self.alive=False
        elif self.food<0:
            print("Cat starved to death")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness is now {self.gladness}")
        print(f"Food in cat is {self.food}")
    def live(self, day):
        day="Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube=random.randint(1,4)
        if live_cube==1:
            self.to_sleep()
        elif live_cube==2:
            self.to_drinkmilkandeatfood()
        elif live_cube==3:
            self.to_play()
        elif live_cube==4:
            self.to_destroyfurniture()
        self.end_of_day()
        self.is_alive()
baksik=cat(name="baksik")
for day in range(365):
    if baksik.alive==False:
        break
    baksik.live(day)