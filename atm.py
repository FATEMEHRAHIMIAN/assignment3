correct_password = 1234
inverse_password = 4321
tryw = 0 

while tryw < 4:
    admittance = int(input("Enter your password following the security instructions ..\n"))
    if ( 999 < admittance < 10000 ):
        if admittance == correct_password:
            print("welcome .")
            break
        elif admittance == inverse_password:
            print("The password is wrong, we called the police.. \n")

        else:
            print("try again..")
    
    else:
            print("You entered less than four digits.. \n")        
    tryw = tryw +1        
