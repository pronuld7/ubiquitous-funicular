class Computer:
    def calculate(self):
        print("Calculating...")
class Display:
    def display(self):
        print("I display the image on the screen...")
class SmartPhone(Display, Computer):
    def print_info(self):
        print(self.resolution)
        if self.resolution == "4K":
            print("Wow you have 4K!")
        print(self.memory)

iphone = SmartPhone()
iphone.calculate()
iphone.display()
