import random
mylist = ["stone","paper","scissor"]
randnum = random.choice(mylist)
def game(user,randnum):
    if randnum == "stone":
        if user == "s":
            print("oops! Match tied computer chose: ",randnum)
            return 0
        elif user == "p":
            print("oops! you lost computer chose: ",randnum)
            return 0
        elif user == "c":
            print("Hurray! you won computer chose: ",randnum)
            return 1
    elif randnum == "paper":
        if user == "s":
            print("Hurray! you won computer chose: ",randnum)
            return 1
        elif user == "p":
            print("oops! Match tied computer chose: ",randnum)
            return 0
        elif user == "c":
            print("oops! you lost computer chose: ",randnum)
            return 0
    elif randnum == "scissor":
        if user == "s":
            print("oops! you lost computer chose: ",randnum)
            return 0
        elif user == "p":
            print("Hurray! you won computer chose: ",randnum)
            return 1
        elif user == "c":
            print("oops! Match tied computer chose: ",randnum)
            return 0     
finalscore = 0
user = input("Choose Between Stone(s),Paper(p),Scissor(c)\n")
score = game(user,randnum)
finalscore = finalscore + score
i=0
while i<1:
    play=input("Play Again! (y/n)\n")
    if(play=="y"):
        randnum = random.choice(mylist)
        user = input("Choose Between Stone(s),Paper(p),Scissor()\n")
        score = game(user,randnum)
        finalscore = finalscore + score
    else:
        i+=2
else:
    print("Thanks for Playing Your Total score is: ",finalscore)
    print("Game made by Raghav Kohli Thanks to CodeWithHarry")
