import random
mylist = ["snake","water","gun"]
randnum = random.choice(mylist)
def game(user,randnum):
    if randnum == "snake":
        if user == "s":
            print("oops! Match tied computer chose: ",randnum)
            return 0
        elif user == "w":
            print("oops! you lost computer chose: ",randnum)
            return 0
        elif user == "g":
            print("Hurray! you won computer chose: ",randnum)
            return 1
    elif randnum == "water":
        if user == "s":
            print("Hurray! you won computer chose: ",randnum)
            return 1
        elif user == "w":
            print("oops! Match tied computer chose: ",randnum)
            return 0
        elif user == "g":
            print("oops! you lost computer chose: ",randnum)
            return 0
    elif randnum == "gun":
        if user == "s":
            print("oops! you lost computer chose: ",randnum)
            return 0
        elif user == "w":
            print("Hurray! you won computer chose: ",randnum)
            return 1
        elif user == "g":
            print("oops! Match tied computer chose: ",randnum)
            return 0     
finalscore = 0
user = input("Choose Between Snake(s),Water(w),Gun(g)\n")
score = game(user,randnum)
finalscore = finalscore + score
i=0
while i<1:
    play=input("Play Again! (y/n)\n")
    if(play=="y"):
        randnum = random.choice(mylist)
        user = input("Choose Between Snake(s),Water(w),Gun(g)\n")
        score = game(user,randnum)
        finalscore = finalscore + score
    else:
        i+=2
else:
    print("Thanks for Playing Your Total score is: ",finalscore)
    print("Game made by Raghav Kohli Thanks to CodeWithHarry")
