print("Welcome to my quiz!!! ")

playing = input("Do you want to play ?")
if playing.lower() != "yes":
    print("Well, See ya later :3")
    quit()

print("Good choice, Lets begin the quiz !\n")

score = 0 

answer = input("Who is the GOAT in football\n ")
if answer.lower() == "ronaldo":
    print("You got 0 ball knowledge !\n")
elif answer.lower() == "messi":
    print("Yessir, you got great ball knowledge !\n")
    score += 1
else:
    print("Who ?\n")

print("Alright lets move onto the next question")
answer = input("Who wins ? Goku or Saitama \n")
if answer.lower() == "saitama":
    print("He's called one punch man for a reason and you are goddam Right !\n")
    score += 1
elif answer.lower() == "goku":
    print("Goku is goated but he aint surviving saitama's punch \n")
else:
    print("All you had to do was type saitama or goku, tf are you doing ?\n")

print("Alright lets move onto the next question")
answer = input("Who wins ? Rock vs Roman Reigns \n")
if answer.lower() == "rock":
    print("I can confirm that you can smell what the rock is cooking\n")
    score += 1

elif answer.lower() == "roman":
    print("Seems like you have a bad nose lol\n")
else:
    print("Stop waffling bro, you should only type roman or rock \n")

print("Let's make this a little harder ")
answer = input("Have you ever seen John Cena ? \n")
if answer.lower() == "yes":
    print("Stop capping, ain't no one seen him lmao \n")
elif answer.lower() == "no":
    print("Exactly, All I see is an invisible man beating up dudes\n")
    score += 1
else:
    print("Yes or no question bruh...\n")

print("Lets make this ultra hard now")
answer = input("What is 1+1 ? \n")
if answer.lower() == "2":
    print("Damn you are so smart!\n")
    score += 1
else:
    print("Nah bruh, you dumb asf\n")


print("Lets go, you finally answered all the questions. What took you so long lol")
print("All jokes aside, you got " + str(score) + " questions correctly")