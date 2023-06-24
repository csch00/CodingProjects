"""
Input statements
  
    input() <--- 'text from console'
    Assign input to a variable: 
      variable_name = input('prompt')
        [console]
          'Prompt' --> 'user_input' --> input() --> variable_name
          variable_name = 'user_input'
        
        user_input will be interpreted as a string by default
      
"""

"""
Attept 1: needed to convert 'guess' into an integer
  
    correct_num = 8
    guess = input("Put guess between 0 and 10 here.")
    if guess != correct_num:
      print("Stoopid")
    else:
      print("Ya smaart")
  
      //guess = 7 --> stoopid
      //guess = 8 --> stoopid **
    
"""

#Correct attempt

correct_num = 8
guess = int(input("Guess which number between 0 and 10 I am thinking of.  If you get it wrong, then you are obvi stoopid."))
if guess != correct_num:
  print("Stoopid")
else:
  print("Ya smaart")