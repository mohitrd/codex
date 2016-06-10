#IPND Stage 2 Fill-In-The-Blanks Quiz
#This project is a Fill-in-the-Blanks game.
#This game will present a user with a paragraph containing several blanks.
#The user will then be asked to fill in each blank appropriately to complete
#the paragraph. The user wins if all blanks are filled correctly.

# empty blanks
blanks = ["__1__", "__2__", "__3__", "__4__"] #for replacing blanks need to be same in the question and here, in the list this had two underscores on both sides initially


# Novice Level
#Insert 25 cents
easy_level = '''A __1__ consists of one whole beat. You make a __1__ by combining 
a down and up beat. Two whole beats will then create a __2__. This will then cause 
a down and up beat twice. If you add a dot exactly after a __2__ then this will increase
the duration of the note by half of its original value. What is created then is known as 
a __3__. Furthermore, two __2__s create a __4__ in music.'''


# Medium Level
# Insert 25 cents
medium_level = '''In music, silence occurs. A __1__ denotes one beat of silence. If you 
add two __1__s together, you will then create what is generally known as a __2__. However, if 
you take half the value of a __1__, you will create an __3__. If you want to stop playing for slightly 
longer than this, than you will have to come across a __4__ which signals four whole beats in length.'''


# Difficult Level
# Insert 25 cents
hard_level = '''Notes on a music sheet go inside what musicians call measures. Four __1__s usually 
go inside of a standard measure. Two __2__s typically are written inside of a measure. If you then 
put a __1__ by a __3__ you will then create a complete meaure. You only need to add one __4__ 
inside of a measure to make it complete.'''



# Music Answer Key
easy_level_answers=["quarter note", "half note", "dotted half note", "whole note"]
medium_level_answers=["quarter rest", "half rest", "eighth rest", "whole rest"]
hard_level_answers=["quarter note", "half note", "dotted half note", "whole note"]

print "Welcome to The Music Theory Fill-in-the-Blanks Game"

user_prompt=raw_input("Select a Musical Theory Level:easy, medium, or hard")
def select_level(user_prompt):
    if user_prompt == "easy":
        return easy_level
    if user_prompt == "medium":
        return medium_level
    if user_prompt == "hard":
        return hard_level
        
#print select_level(user_prompt)     


def select_answers(user_prompt):
    if select_level(user_prompt)==easy_level:
        return easy_level_answers
    if select_level(user_prompt)==medium_level:
        return medium_level_answers
    if select_level(user_prompt)==hard_level:
        return hard_level_answers
        
    
"""
    This Function checks if user's answer matches the actual game answer and if the response is correct or wrong.
    :inputs: user_answer: user's answer; answer: game answer;
            game_answer_index : game answer's index
    :output: user_answer
"""
def confirm_answer(user_answer, answers, answer_set_index):
    
    if user_answer==answers[answer_set_index]:
        return "Correct"
        
    return "Incorrect"  


def play_game(user_prompt):
    level=select_level(user_prompt)
    answers=select_answers(user_prompt)
    blanks_set_index=0
    count=0
    answer_set_index=0
    while blanks_set_index<len(blanks):
        #while answer_set_index<len(answers):
            user_answer=raw_input("Please fill in the correct answer for " + blanks[blanks_set_index])# the user will fill in the first blank.
            res=confirm_answer(user_answer, answers, answer_set_index) #storing this value in variable res to avoid redundant writing
            print res
            
            while res=="Incorrect": #if the answer checks out as "Incorrect":user tries again.
                user_answer=raw_input("Incorrect response. Please fill in the correct answer for " + blanks[blanks_set_index])
                res=confirm_answer(user_answer, answers, answer_set_index)

                
            if res=="Correct":
                print "Awesome, Musician! Your answer is correct!"
                count=count+1
                level=level.replace(blanks[blanks_set_index],user_answer)
                print level
                blanks_set_index+=1
                answer_set_index+=1
            if count==4: #checks if all the four blanks are answered
                print "Excellent job. You are now a MASTER MUSICIAN!!! "
                print "You have graduated from Concert Band to Symphonic Honors Band!!!"
                exit()

          



        # if the user answers correctly,a message indicating the answer is correct will appear, and music theory game w           
               
               
               
                
                    
   


game_over = "Game Over!!"

print play_game(user_prompt)