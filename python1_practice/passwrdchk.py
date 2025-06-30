x = 0
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password = "python1234"

counter = 0

while True:
    check = input("Enter the password: ")
    x = 0
    for i in check:
        for j in digits:
            if i == j:
                x += 1

    
    if x == 0:
        print("Error: Need a digit.")
        continue
    if check == password:
        print("The password you entered is correct")
        exit()
    else:
        print("Access denied.")
        counter += 1
    if counter > 1:
        print("You tried multiple times. Please try again but take care!!!")
