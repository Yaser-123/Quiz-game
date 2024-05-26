print("Welcome to my computer quiz!")

playing = input("Do you want to play ? ")

if playing.lower() != "yes" :
    quit()
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is the keyword used to define a function in python? ")
if answer.lower() == "def" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what symbol is used to start a comment in python? ")
if answer.lower() == "#" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("which method is used to add an element to the end of a list? ")
if answer.lower() == "append" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is the correct file extension for python files? ")
if answer.lower() == "py" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is the output of print(2 ** 3)? ")
if answer == "8" :
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("what function is used to get the length of a list in python? ")
if answer.lower() == "len" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is the output of print(10 // 3)? ")
if answer == "3" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is the output of print(len(""hello world""))? ")
if answer == "11" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What GPU stand for? ")
if answer.lower() == "graphics processing unit" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")

print("You got " + str(round((score / 11) * 100, 1)) + ("%."))
