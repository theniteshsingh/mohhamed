#any import here
import functions
#Import ends here


#Data Start here

#seat coaches
GryffindorUp,GryffindorDown,HufflepuffUp,HufflepuffDown,RavenClawUp,RavenClawDown,SlytherinUp,SlytherinDown =6,6,6,6,6,6,6,8,

trains =[

    #Up trains
    ("Gryffindor Up Train","9:00 am",GryffindorUp*80),
    ("Hufflepuff Up Train","11:00 am",HufflepuffUp*80),
    ("RavenClaw Up Train","1:00 Pm",RavenClawUp*80),
    ("Slytherin Up Train","3:00 pm",SlytherinUp*80),

    #down trains
    ("Gryffindor Down Train","10:00 am",GryffindorDown*80),
    ("Hufflepuff Down Train","12:00 pm",HufflepuffDown*80),
    ("RavenClaw Down Train","2:00 pm",RavenClawDown*80),
    ("Slytherin Down Train","4:00 pm",SlytherinDown*80),
         ]

# Data ends here

print("Welcome to Hogwarts School of Witchcraft and Wizardry's train booking system")

for train in range(4):
    print(f" Option {train+1} : {trains[train][0]} depart at {trains[train][1]} and current seat availibility {trains[train][2]}")

SelectedTrain=int(input("Enter your choices :"))
PurchaseSeat=int(input("How many seats you want to purchase today :"))

functions.booking(SelectedTrain,PurchaseSeat)

