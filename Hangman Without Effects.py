import turtle # This imports the turtle


turtle.title("Hangman Arsheya Khobiary 18024261") # this will give a title of  the turtle .exe that opens
turtle.setup (800, 800) # this is the size of the turtle that will display the game on another window


a = turtle.Turtle() # this will create a turtle called A

a.color('White') # this is the text colour of the turtle if it writes   

style = ('Courier', 25, 'italic') # this is the style such as the font font size and if it is italic or not

a.write('Welcome to doctor hangman !', font=style, align='center') # this is basically saying print welcome ...  with the font and aligning it to  the center of the size  of the turtle that we have chosen above

turtle.hideturtle() # this will hide the > arrow  key of the turtle

print("")# this is just a print command to ensure it is working well and allowing some space

a.penup() # will take the pen of the turtle upwards
a.goto(0,50) # will take it to a certain area of the size 
a.pendown() #this will being it back down
a.write('Follow the steps on the terminal window to continue!', font=style, align='center') # will ensure it writes follow with the style and alignment again
a.hideturtle()  #will hide the turtle
turtle.bgcolor('blue') # turtle background colour blue 
a.hideturtle()#again hide the arrow


L = turtle.Turtle() #another turtle with thee same comments as above as they have the same rules
L.color('White')
LooseStyle = ('Courier', 50, 'italic')
turtle.hideturtle()
L.hideturtle()

W = turtle.Turtle()
W.color('White')
WStyle = ('courier', 50, 'italic')
turtle.hideturtle()
W.hideturtle()



LG = turtle.Turtle()
LG.color('White')
LGStyle = ('Courier', 20, 'Italic')


def main(): #defining the main parts of thhe game and what it needs to run 
    turtle.clear() 

    
    print ("    ") 

    print("Welcome To the Doctor Hangman! Follow The Steps Below To Get Started!")

    print ("    ")   #Starts new line to ensure it looks clean

    print ("Please enter player 1's Name and Player 2's Name")   

    print ("    ")   #Starts new line to ensure it looks clean

    P1 = input ("Player 1 Please Enter Your Name: ")

    P2 = input ("Player 2 Please Enter Your Name: ")

    print ("    ")   #Starts new line to ensure it looks clean

    print ("Player 1 is : ", P1, "!")

    print ("Player 2 is : ", P2, "!")

    print ("    ")   #Starts new line to ensure it looks clean   

    print (P1, "Please follow all the game rules to ensure it is fair to", P2, "That also goes for you", P2,)

    print ("    ")   #Starts new line to ensure it looks clean

    print ("Please enter the word you want player 2 guess")

    print ("    ")

    print ("    ")
    
    word = list(input("Enter A Word: ") ) #will allow the program to know that the word that they type is = to word

    for i in range(55):

            print ()
# above code will press return 50 times to end up having  to scroll up to see the previous text so ensure they dont see the word that was entered
            a.clear()
# VARIABLES 
    alphabet = "abcdefghijklmnopqrstuvwxyz" # this is the alphabet from a-z and it will be helpful to use when trying to find out if the attempt from the user is right or wrong
    

    secondword = list("*" * len(word))

    finalword = "".join(word)

    letters_guessed = [ ]

    status = [ ] ################################################################################################################################################

    lives = 8

    guessed = False



    print('The word contains', len(word), 'letters.') # this will find out how many letters the word that was entered contains

    print("Word :",(len(word) * '*')) #this will turn the characters into ****** stars to hide from the player


    while ((guessed == False) and (lives > 0)):  # this says while lives is greater than 0 print the following EVERYTIME untill its less than 0
        

        print ("You Have " + str(lives) + " Lives Remaining")  #this will print out a message as well as a variable.

        print ("    ") #leaves a gap

        guess = input("Please enter one letter or full word: ").lower() # this will have a variable run and when its running print out a specific text

        print ("    ") #leaves a gap



        if len(guess) == 1: #if the guess is correct and the it is in the word that the user typed it will run the code below

                

            if guess in word:

                print ("    ")   

                print ("Yes! The Word Contains The Letter : ",     " "   + guess +  " !")

                print(":)")

                letters_guessed += guess




            elif guess not in alphabet: #if the users guess is not in the word that was attempted to guess it will print the following code

                print ("    ")   

                print ("You have not entered a letter.")

                




                

            elif guess in letters_guessed: #if the guess is already guessed it will print this text below

                print ("    ")   

                print ("OOPS... You Have Already Guessed The Letter : ",   " " + guess + " !" )


                

            elif guess not in word: #if the letter is not in the word that they guessed it will print the text below

                print ("    ")  

                print("Sorry .... The Word Does Not Contain The Letter : " ,    " " + guess + " !")

                lives -=1 # if it was wrong then it will minus one life from the lives remaining.

                DrawPart(lives)

    

            else:

                print ("NO IDEA WHY WE GET THIS MESSAGE, should be investigated furthur")



        elif len(guess) <= len(word):
    
            

            if list(guess) == word:# if the user finishes guessing the word or guesses the whole word it will print the text below

                print("Well done, you have guessed the word!")


                guessed = True # if it was guessed then do the code below.

                restart() #this will run the restart code which is below

            else: # if it was not guesssed print the following below

                print ("    ")

                print("Sorry, that was not the word we were looking for :(")

                print ("    ")

                

        else: # anything else happens print this.

            print ("    ")

            print("The length of your guess is not the same as the length of the word we\'re looking for.")

            print ("    ")

        status.clear() ################################################################################################################################################

        LG = " " 

        if guessed == False:

            for letter in word:

                if letter in letters_guessed:

                    status += letter

                    LG += letter

                else :

                    status += "*"

                    LG += "*"

            print (LG)
# the code above consists of a couple of important code where if it is not been guessed keep it as a star(*) if it was revealed allow the letter.


        if status == word:

            print ("    ")

            print ("well done you have guessed the word!")

            print ("    ")
#if the status is the same as word which was entered in as it revealed itself fromm the stars then print the message above and below from the turtle.
            turtle.clear() #this will remove the previous turtle

            W.write('YOU WIN!', font= LooseStyle, align='center') # this will have a clear screen when the user wins and type the following with the specific style which was chosen and area

            W.penup()

            W.goto(0,50)

            W.pendown()

            

            turtle.clear()#this will remove the previous turtle

            #PUT MUSIC HERE IF WON

            

            print("  ")

            guessed = True  # if won then run the restart

            restart() #restart code is below.

            

        elif lives == 0: # if the lives run out then the turtle will be clear for another one so it prints the code below

            print ("Unfortunately You Ran Out Of Lives. The Word Was : ", finalword) # will say you ran out of lives and the word was the variable.

            turtle.clear()#this will remove the previous turtle

            L.write('YOU LOOSE!', font= LooseStyle, align='center') # another turtle will appear and let the user know they lost.

            L.penup()

            L.goto(0,50)

            L.pendown()

            turtle.clear()
           

            print ("    ")

            restart()





def restart(): #this is the restart command where it will give the user a option below

    answer = input("Would you like to play again? yes/no").lower() #either they want to restart or not

    print ("    ")#leaves a gap to  ensure it looks nice.

    if (answer) == "Y" or (answer) == "y" or (answer) == "Yes" or (answer) == "yes" or (answer) == "YES" :
        turtle.clear()
        L.clear()
        L.hideturtle()
        LG.clear()
        W.clear()
        main()
# if the answer above is anything apart from yes it will print  the code below however if it is any of them on top it will restart the whole program with the turtle cleared.
    else:

        print ("    ")

        print ("    ")

        print ("Thankyou For Playing Hangman!")

        print ("By : Arsheya Khobiary - 18024261")

        pass

    # if the user doesnt want to play anymore they will have the above message left for them in the terminal.




#the below code is my turtle.



def DrawPart(lives):

    a = turtle.Turtle()

    a.clear()
    a.hideturtle()
    turtle.hideturtle()

    LG.penup()

    LG.goto(-250,330)
  #  LG.write('test ' ,  font=style, align='Right')   JUST A TEST CODE 
    LG.goto(0,301)
    LG.hideturtle()
    
    a.hideturtle()
    
    





    if (lives == 7): #this draws the YELLOW FRONT BUMPER

        turtle.fillcolor('Yellow')

        turtle.begin_fill()

        for i in range(4):

            turtle.forward(90)

            turtle.right(90)

        turtle.end_fill()

        turtle.left(90)

        

    elif (lives == 6): #this draws the YELLOW BACK BUMPER

        turtle.fillcolor('Yellow')

        turtle.begin_fill()

        turtle.forward(80)

        for i in range(3):

            turtle.left(90)

            turtle.forward(170)

        turtle.end_fill()

        

    elif (lives == 5): #this draws the BLACK FRONT TIRE

        turtle.penup()

        turtle.forward(20)

        turtle.right(90)

        turtle.pendown()

        turtle.fillcolor('black')

        turtle.begin_fill()

        turtle.circle(25)

        turtle.end_fill()

        

    elif (lives == 4): #this draws the BLACK BACK TIRE

        turtle.penup()

        turtle.right(90)

        turtle.forward(90)

        turtle.right(90)

        turtle.pendown()

        turtle.fillcolor('black')

        turtle.begin_fill()

        turtle.circle(25)

        turtle.end_fill()

        

    elif (lives == 3): #this draws half of the CROSS

        turtle.penup()

        turtle.forward(90)

        turtle.pendown()

        turtle.fillcolor('red')

        turtle.begin_fill()

        turtle.forward(20)

        turtle.right(90)

        turtle.forward(20)

        turtle.left(90)

        turtle.forward(10)

        turtle.left(90)
        
        turtle.forward(20)

        turtle.right(90)

        turtle.forward(20)

        turtle.left(90)

        turtle.forward(10)

        turtle.left(90)

            

    elif (lives == 2): #this draws the second part of the CROSS 

        turtle.forward(20)

        turtle.right(90)

        turtle.forward(20)

        turtle.left(90)

        turtle.forward(10)

        turtle.left(90)

        turtle.forward(20)

        turtle.right(90)

        turtle.forward(20)

        turtle.left(90)

        turtle.forward(10)

        turtle.left(90)

        turtle.end_fill()

    elif (lives == 1): #this draws the driver window
        

        turtle.penup()

        turtle.right(90)

        turtle.forward(80)

        turtle.right(90)

        turtle.forward(10)

        turtle.pendown()

        turtle.fillcolor('lightblue')

        turtle.begin_fill()



        for i in range (2):

            turtle.forward(30)

            turtle.left(90)

            turtle.forward(70)

            turtle.left(90)
            
        turtle.end_fill()

            

    elif (lives == 0): # this will draw the final red siren 

        turtle.penup()

        turtle.right(90)

        turtle.forward(40)

        turtle.right(90)

        turtle.forward(90)

        turtle.pendown()

        turtle.fillcolor('red')

        turtle.begin_fill()

        for i in range (2):

            turtle.forward(10)

            turtle.left(90)

            turtle.forward(35)

            turtle.left(90)

        turtle.end_fill()
    
            

        LG.clear() #this will finally clear everything if the restart happens.

main()

restart()



# Thankyou.... this one is without the affects. and with the comments the program is exactly the same probably
#diffrerent enter or return spaces between them. the only difference is one is in a zip file and that has sounds which was tested and ensured they all work
#hope you can check that one aswell just as it has music which is better.





