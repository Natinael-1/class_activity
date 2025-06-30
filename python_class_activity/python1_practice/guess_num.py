def guess():
    while True:
         x = 39
         number = int(input("Guess the number between 10 and 50: "))
         if number == x:
             print("You got it correctly!")
             break

            
         elif number <= 30:
             print("Oops your number is far behind")
             continue
        
         elif number >30 and number <= 38:
             print("Oh! You almost got it ")
             continue
        
         elif number >39:
             print("Ah! You are going behond the number")
             continue
        
guess()    
   