from OOP.items import Item


class Hero:
    POWER = 5
    ENDURANCE = 5
    INTELLECT = 5
    CAUTION = 5
    def __init__(self, name):
        self.name = name
        self.power = Hero.POWER
        self.endurance = Hero.ENDURANCE
        self.intellect = Hero.INTELLECT
        self.caution = Hero.CAUTION
        self.gear = []

    def calculate_stats(self):
        for i in self.gear:
            for key,value in i.__dict__.items():
                if key == "power":
                    self.power += value
                elif key == "endurance":
                    self.endurance += value
                elif key == "intellect":
                    self.intellect += value
                elif key == "caution":
                    self.caution += value

    def add_item(self,item):
        for hero_item in self.gear:
            if hero_item.typee == "Weapon":
                return "This Hero already had Weapon"
        self.gear.append(item)
        return f"Item added to {self.name} gear"

    def stats(self):
        result = "Hero stats:\n"
        result += f"Power:{self.power}\n"
        result += f"Endurance:{self.endurance}\n"
        result += f"Intellect:{self.intellect}\n"
        result += f"Caution:{self.caution}"
        return result


first_hero = Hero("Pesho")
first_item = Item("Blade of the Ruined King" ,"Weapon", 20,10,5,5)
second_item = Item("Infinity Edge" , "Weapon", 20,23,12,23)
print(first_hero.add_item(first_item))
print(first_hero.add_item(second_item))
first_hero.calculate_stats()
print(first_hero.stats())



