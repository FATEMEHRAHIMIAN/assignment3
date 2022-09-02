correct_password = 1234
inverse_password = 4321
tryw = 0
if tryw >= 3 :
    print("YOUR ACCOUNT IS LOCKED!")       
else:
    while tryw < 3:
        admittance = int(input("Enter your password following the security instructions ..\n"))
        if ( 999 < admittance < 10000 ):
            if admittance == correct_password:
                print("welcome .")
                tryw = tryw+1
                break
            elif admittance == inverse_password:
                print("The password is wrong, we called the police.. \n")
           
                tryw = tryw+1

            else:
                print("try again..")
                tryw = tryw + 1
    
        else:
                print("You entered less than four digits.. \n")   

