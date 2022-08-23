#from lib2to3.pgen2.driver import Driver
from random import randint

#function for the ball range
def golf_ball_range(short, long):
    def ball_range():
        return randint(short, long)
    return ball_range
#the irons and drivers that you will be hitting with
clubs = {"Driver": golf_ball_range(200, 260), "3-wood": golf_ball_range(180,235),
        "8-iron": golf_ball_range(100,180),"Sand-Wedge": golf_ball_range(60,100),
         "Chip-Shot": golf_ball_range(5,20)}

course = {"Hole1": 339}

#functions for hitting the ball

def hitting_the_ball(iron):
     return clubs[iron]()
    
def on_the_green():
    print("You are on the green!")
    chance_of_winning = randint(1,4)
    print("Choose a number between 1 - 4 for your chance to putt it in: ")
    while True:
        thing = input()
        if int(thing) == chance_of_winning:
            print("You did it")
            return
        else:
            print("Putt again")


def which_club():
    print("Which club would you like to use?")
    for i in clubs.keys():
        print(i)




print("  GGGG" +  "   OO " +" L " + "   FFFF" )
print(" G     "+  " O  O " +"L " + "   F" )
print(" G   GG "+ "O  O " +"L "  + "   FFF"  )
print(" G    G "+ "O  O " +"L "  + "   F"  )
print("  GGGG" +  "   OO " +" LLLL " "F"  )

print( "")
print( "")



print("Welcome to the Golf Game\n")
name = input("Please Enter your name: ")

print("Welcome " + name + ", the first course you will play on is a 9 hole called Caleb's Caddy")
print("\n")
print("Hole 1: This is a Par 4 and it is "+ str(course["Hole1"]) +" yards")
print("\n")
cchole1 = 0
distance = course["Hole1"]
while distance > 20:
    which_club()
    print("---------\n")
    choice = input()
    print("\n")
    cchole1 = hitting_the_ball(choice)
    print("Your "+ choice + " hit " + str(cchole1))
    print("\n")
    distance = distance - cchole1
    if distance < 20:
        break
    print("You have " + str(distance) + " left." )
    print("\n")

print("\n")
on_the_green()



