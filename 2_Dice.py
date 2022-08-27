import random as Ran
dicee = []
while True :
    dice = Ran.randint(1, 6)
    dicee.append(dice)
    if  6 in dicee :
            print("oh yessss :))) \n")
            num= str(sum(dicee))
            print( "Add up the numbers of the dice game is : ",num )
            break
    else:
        continue
       
print("the list of dice is :",dicee)
print("Number of dice rolls is: ",(len(dicee)))