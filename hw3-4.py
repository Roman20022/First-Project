class mouse:
    hp = 150
    eat = 150
    name = ""
    def __init__(self,n):
        self.name = n
        print(self.name,", your life is beginning")
        self.live()
        self.live()
        self.eateng()
        self.live()
        self.live()
        self.eateng()
        self.live()
        self.live()
        self.eateng()
    def eateng(self):
        self.eat += 5
        print(self.eat)
    def live(self):
        self.eat -= 5
        print(self.eat)
    def damage(self):
        self.hp -= 5
bread = mouse("Bread")
print("------------------------------------------------")
class Soda:
    def __init__(self, ingredient):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def show_my_drink(self):
        if self.ingredient:
            print(f'Газована вода і {self.ingredient}')
        else:
            print("Просто газована вода")
drink1 = Soda(3)
drink2 = Soda("сік")
drink3 = Soda(5)
drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()