# Do install graphics module for code to run
import random

print(
    "Welcome to the game. So as our CSE project we have made a survival adventure game in python whic can be played through any IDLE.")
print(
    "In the game ,As the  protagonist You are a student who has just joined a new college and your aim is to pass your exams to get a good job")
name = str(input("Enter your name --> \n"))
print("welcome {}. Best of luck for your journey ahead as a CSE student.".format(name))

skills = 0
warnings = 0

print("Your skill level is zero, you will be required to have skills above 6 to pass")
print("Your warning level is zero, if your warning level reaches 3 you will be suspended (GAME OVER)")
print("This is your first day a college (Semester-1)")
print("Would you like to introduce yourself to your batchmates (Y/N)")
intro = input("(Y/N) \n")
if intro.upper() == "Y":
    skills = skills + 1
else:
    pass
print("Skill count = {}".format(skills))
print("Would you attend your classes regularly (Y/N)\n")
attend = input("(Y/N)")
if attend.upper() == "Y":
    skills = skills + 1
else:
    pass

print("Skill count = {}".format(skills))

print("Would you like to join a club (Y/N) \n")
club = input("(Y/N) \n")
if club.upper() == "Y":
    print("Which club would you like to join (GAMERS / SPORTS / DEVELOPERS)")
    club1 = input("(GAMERS / SPORTS / DEVELOPERS) \n")
    if club1.upper() == "GAMERS":
        pass
    elif club1.upper() == "SPORTS":
        pass
    elif club1.upper() == "DEVELOPERS":
        skills = skills + 1
    else:
        pass
else:
    skills = skills - 1
print("skill count = {}".format(skills))

print("Your friends are sneeking out of the campus, would you like to join them? (Y/N)")
sneek = input("(Y/N) \n")
if sneek.upper() == "Y":
    warnings = warnings + 1
    print("your warning level has been raised due to unacceptable action")
    print(f"warnings count = {warnings} !!!")
else:
    print("your friend got busted while sneeking out, GOOD JOB")

print("here is a suprise quiz for you")
print("what is the type for object --> 5.0")
answer = input("int / float / bool / str \n")
answer1 = answer.lower()
print(answer1)
if answer1 == ("int" or "bool" or "str"):
    print("OOPS, your answer is wrong")
    skills = skills - 1
elif answer1.lower() == "float":
    print("WOOW, you got correct answer")
    skills = skills + 1
else:
    print("OOPS, wrong input")
    skills = skills - 1
print(f"skills count = {skills}")

print("your 1st year marks are being evaluated. If skills are less than 2, you fail!")
print(f"your skill count in 1st year = {skills}")

if skills < 2:
    print("GAME OVER, YOU DIDN'T PASS")

else:
    print("You passed the first year \n")
    print("Would You like to play the next stage (Y/N)")
    second = input("(Y/N)")
    if second.upper() == 'N':
        print("Thank You for playing")
    else:
        print("Welcome to the 2nd stage of game and congrats on passing the first!!! \n")
        print(
            "The rules are same you need to get a set amount of skill points to pass it but this time its gonna be tough.")
        print("You will have a full-on quiz at the end and your score in that will determine if you win. \n")
        print("Also remember to keep you warnings count low or its game over! \n")
        print("Semester-2 starts:")
        print('''You have specialisation selection in your college,select one:
              (1.AI
              2.DATA SCIENCE
              3.BLOCK CHAIN
              4.GAMING AND VR
              5.CYBER SECURITY)''')
        spec = input("1/2/3/4/5 \n")
        print("Based on your choice of specialisation you will get a quiz later in the game")
        print("You have a surprise lucky draw in your college (select a number from 1 to 3)")
        draw = int(input("1/2/3-->"))
        luck = random.randint(1, 3)
        if draw == luck:
            print("Winner!!! you get an extra skill point")
            skills = skills + 1
            print("skill count=", skills)
            print("")
        else:
            print("Lose You didn't win better luck next time \n")
        print("You have an arts and python interactive activity ahead.")
        print("Would You like to join(Y/N)")
        art = input("Y/N")
        if art.upper() == 'Y':
            print("As of activity You have to draw a smiley face in upcoming gui")
            from graphics import *

            win = GraphWin("Smiling Face", 600, 400)
            head = Text(Point(300, 50), 'Click 2 points for eyes,3 points for nose,4 points for mouth in sequence')
            head.draw(win)
            foot = Text(Point(300, 350), 'Click anywhere after drawing to continue the game')
            foot.draw(win)
            circle = Circle(Point(300, 200), 90)
            circle.draw(win)
            circle.setFill('yellow')
            eye1 = win.getMouse()
            circle1 = Circle(eye1, 10)
            circle1.draw(win)
            circle1.setFill('black')
            eye2 = win.getMouse()
            circle2 = Circle(eye2, 10)
            circle2.draw(win)
            circle2.setFill('black')
            nose1 = win.getMouse()
            nose1.draw(win)
            nose2 = win.getMouse()
            nose2.draw(win)
            nose3 = win.getMouse()
            nose3.draw(win)
            triangle = Polygon(nose1, nose2, nose3)
            triangle.draw(win)
            triangle.setFill('blue')
            m1 = win.getMouse()
            m1.draw(win)
            m2 = win.getMouse()
            m2.draw(win)
            m3 = win.getMouse()
            m3.draw(win)
            m4 = win.getMouse()
            m4.draw(win)
            sqaure = Polygon(m1, m2, m3, m4)
            sqaure.draw(win)
            sqaure.setFill('red')
            win.getMouse()
            win.close()
            print("----------")
            print("Well done Here is a bonus skill point")
            skills = skills + 1
            print("skill count-", skills)
        else:
            print("Show more participation please!!!")
        print("Exams approach!!!")
        print("First for your specialisation quiz:")
        if int(spec) == 1:
            print("Q.Who is known as the -Father of AI?")
            print('''a)Fisher Ada
            b)Alan Turing
            c)John McCarthy
            d)Allen Newell''')
            ai = input("a/b/c/d")
            if ai == "a":
                print("Correct!")
                skills = skills + 1
                print("skill count-", skills)
            else:
                print("Wrong Answer. Work Harder")
        elif int(spec) == 2:
            print('''Q.Which of the following is the most important language for Data Science?
            a) Java
            b) Ruby
            c) R
            d) None of the mentioned''')
            ds = input("a/b/c/d")
            if ds == "c":
                print("Correct!")
                skills = skills + 1
                print("skill count-", skills)
            else:
                print("Wrong Answer. Work Harder")
        elif int(spec) == 3:
            print('''Q.What is the term for when a blockchain splits?
            a) fork
            b) split
            c) break
            d) sidechain division''')
            bc = input("a/b/c/d")
            if bc == "a":
                print("Correct!")
                skills = skills + 1
                print("skill count-", skills)
            else:
                print("Wrong Answer. Work Harder")
        elif int(spec) == 4:
            print('''Q.Which three companies dominate the video game industry worldwide?
             a. Sony, Ampex, Nokia
             b. Microsoft, IBM, Sony
             c. Sony, Nintendo, Microsoft
             d. Ubisoft, Sony, Bethesda Studios''')
            vr = input("a/b/c/d")
            if vr == "a":
                print("Correct!")
                skills = skills + 1
                print("skill count-", skills)
            else:
                print("Wrong Answer. Work Harder")
        else:
            print('''Q.Which one of the following can be considered as the class of computer threats?

            a) Dos Attack
            b) Phishing
            c) Soliciting
            d) Both a and c''')
            cx = input("a/b/c/d")
            if cx == "a":
                print("Correct!")
                skills = skills + 1
                print("skill count-", skills)
            else:
                print("Wrong Answer. Work Harder")
        print('''Now for a final exam we will have a quiz on python:''')
        print('''This is a 5 question quiz:

        Q1.predict Output
        Text= "Hello Bennett"
        ¡ = (ord(Text[0])-ord(Text[6]))
        j = (ord(Text[5])-32)
        print(Text[i:j]+" "+Text[j:i])
        a. Bennett Hello 
        b. Hello Bennett
        c. Error
        d. None of these 
        ''')
        Q1 = input("a/b/c/d")
        if Q1 == "d":
            print("Correct!")
            skills = skills + 1
            print("skill count-", skills)
        else:
            print("Wrong Answer")
        print("")
        print('''Q2.What is the value of C of following sample code for N =7 ?
        N = eval (input())
        C=0
        while(n):
              if(n>5):
                   C=C+n-1
                   n=n-1
              else:
                   break
        print(c)
        a. 11
        b. Syntax Error 
        c. 12
        d. 10''')
        Q2 = input("a/b/c/d")
        if Q2 == "b":
            print("Correct!")
            skills = skills + 1
            print("skill count-", skills)
        else:
            print("Wrong Answer")
        print("")
        print('''Q3.What is the value of N printed in the following sample code?
        for N in range(10, 14):
               if N%10==1:
                   print(N)
        a. 10,11,13
        b. None of these
        c. 11,13
        d. 10,12,13
        e. 11''')
        Q3 = input("a/b/c/d")
        if Q3 == "e":
            print("Correct!")
            skills = skills + 1
            print("skill count-", skills)
        else:
            print("Wrong Answer")
        print("")
        print('''Q4.In a Python program, a control structure,
        Select one:
        a. Defines program-specific data structures
        b. Directs the order of execution of the statements in the program 
        c. Dictates what happens before the program starts and after it terminates
        d. Manages the input and output of control characters''')
        Q4 = input("a/b/c/d")
        if Q4 == "b":
            print("Correct!")
            skills = skills + 1
            print("skill count-", skills)
        else:
            print("Wrong Answer")
        print("")
        print('''Q5.Which of the following operators has the highest precedence?
        Select one:
        a. *
        b. () 
        c. ++
        d. >>''')
        Q5 = input("a/b/c/d")
        if Q5 == "b":
            print("Correct!")
            skills = skills + 1
            print("skill count-", skills)
        else:
            print("Wrong Answer")
        print("")
        print("Now for the results.Your skills =",
        skills)
        print("Congrats on competing the game!!!")
        print("Thank you for playing")


