print("Welcome to my quiz!!! ")

playing = input("Do you want to play ?")
if playing.lower() != "yes":
    print("Well, See ya later :3")
    quit()

print("Good choice, Lets begin the quiz !")

answer = input("Who is the GOAT in football ")
if answer.lower() == "ronaldo":
    print("You got 0 ball knowledge !")
elif answer.lower() == "messi":
    print("Yessir, you got great ball knowledge !")
else:
    print("Who ?")
    