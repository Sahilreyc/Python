class Crop:
    """A Normal Food Crop"""

    def __init__(self,growth_rate, light_need, water_need):

        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Normal"

    def needs(self):
        return {'light need':self._light_need, 'water need':self._water_need}

    def report(self):
        return {'type':self._type,'status':self._status,'growth':self._growth,'days growing':self._days_growing}

    def update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seeding"
        elif self._growth == 0:
            self._status = "Seed"

    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()

def auto_grow(crop,days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grop(light,water)

def manual_grow(crop):
    valid = False
    while not valid:
        try:
            light = int(input("Please enter a light value (1-10): ")
            if 1 <= light <= 10:
                valid = True
            else:
                print("Value entered not valid, Please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid, Please enter a value between 1 and 10")
    valid = False
     while not valid:
        try:
            water = int(input("Pleaser enter a water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                 print("Value entered not valid, Please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid, Please enter a value between 1 and 10")
    crop.grow(light,water)

def display_menu():
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")                    
    print("3. Report Status")
    print("0. Exit test program") 
    print("")
    print("Please pick one of the options in the menu")                    

                        
def main():
    new_crop = Crop(1,4,3)
    print(new_crop.needs()['light need']
    print(new_crop.report())
    new_crop_grow(4,4)
    print(new_crop.report())

if __name__ == "__main__":
    main()


