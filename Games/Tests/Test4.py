import time

class OOP:
    def TextLoader(self,Text,Sleep):
        for i in Text:
            print(f'{i}',end='')
            time.sleep(Sleep)
        print()
class MainObjects:
    def __init__(self,Program_Name,User_Name,save):
        self.Program = Program_Name
        self.User = User_Name
        self.save = save

    def Main(self):
        AllObj = OOP()
        AllObj.TextLoader(f'Hello {self.User}.\nDo you remember you MAIN Mission?',0.2)
        answer = input(f'[{self.User}](Yes or No):\t')
        if answer == 'No':
            AllObj.TextLoader('Sireus?',0.7)
            answer = input(f'[{self.User}](Yes or No):\t')
            if answer == 'Yes':
                AllObj.TextLoader('Your mission to restart the simulation computer.\nYou need to off all systeams of this simulation.\nFinaly you need to delete you game file to escape simulation.',0.000000001)
            elif answer == 'No':
                AllObj.TextLoader('Ok',0.3)
        elif answer == 'Yes':
            pass

        AllObj.TextLoader('Continue?')
        input(f'[{self.User}](Yes or Yes):\t')
'''
class Car:
    def Sound(self):
        AllObj = OOP()
        AllObj.TextLoader('Beep',0.1)
    def Long_Sound(self):
        AllObj = OOP()
        AllObj.TextLoader('Beeeeep',0.7)
class Button:
    def __init__(self):
        self.click = 0

    def Click(self):
        self.click += 1
    
    def Click_count(self):
        print(self.click)
           

    def Clear(self):
        self.click = 0
'''

Machine = MainObjects(Program_Name='COWR',User_Name='RTBot',save=0)
Machine.Main()
'''
Car_Obj = Car()
Car_Obj.Sound()
Car_Obj.Long_Sound()
Button_ = Button()
while True:
    if input('do\t') == 'click':
        Button_.Click()
    elif input('do\t') == 'clear':
        Button_.Clear()
    print(Button_.click)
'''

