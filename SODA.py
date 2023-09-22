class soda:
    def __init__(self, ingrediment=None):
        if isinstance(ingrediment, str):
            self.ingrediment = ingrediment
        else:
            self.ingrediment = None
    def show_my_drink(self):
        if self.ingrediment:
            print(f'Soda and {self.ingrediment}')
        else:
            print('Regular Soda')

drink1=soda()
drink2=soda(6)
drint=soda("spider eye")
drink1.show_my_drink()
drink2.show_my_drink()
drint.show_my_drink()