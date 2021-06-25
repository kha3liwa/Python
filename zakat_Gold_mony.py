from typing import Any

import sys
class Zakat:
    gold_weight: Any

    def __init__(self):
        global gold_weight
        global caliber
        self.startApp()
#---------------- code start pro ----------------------------------      
    def startApp(self):    
        print("  ")
        print("|----------------------------------------------|")
        print("|     Choose                                   |")
        print("|    1 Choosing zakat on money                 |")
        print("|    2 Choosing zakat on gold                  |")
        print("|    0 Exit                                    |")
        print("|----------------------------------------------|")
#---------------- code for choose any use --------------------------
        choose = int(input("enter 1 or 2 or 3  :"))
        if choose == 1:
            print (" your choose zakat on money  1\n")
            print(self.calculate_zakat_mony(1000))
            self.startApp()
        elif choose == 2 :
            print("your choose zakat on gold 2\n")
            print(self.calculate_zakat_Gold(100))
            self.startApp()
        elif choose == 0 :
            print("|----------------------------------------|")
            print("| Think you for use This App by:kha3liwa |")
            print("|----------------------------------------|")
            sys.exit()
        else:
            print("please try again\n")
            self.startApp()
 #---------------- code calculate zakat gold -------------------------- 
    def calculate_zakat_Gold(self, x):
        self.gold_weight = float(input("Enter the gold weight here : "))
        x = float(input('Enter the gold caliber :\n You should be 18 , 21 , 24 only For your account to be correct : '))
        return "The quorum is : {}  ".format(float(self.gold_weight * x / 24))
#----------------- code calculate zakat mony --------------------------
    @staticmethod
    def calculate_zakat_mony(amount):
        amount = float(input("What is the value of the amount for which Zakat is to be known? : "))
        # return amount /40
        return "{} DL  ".format(amount * 2.5 / 100)
        # return amount * 0.025
        
zakat1 = Zakat()
print(zakat1.startApp())
