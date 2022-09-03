import random 
#dicee = []
sum =0
timei =0

while True :
        dice = random.randint(1,6)
       
        timei = timei + 1 
        sum = dice + sum
       # print("oh no :( \n")
        print(dice)
        print( "Sum of dice throws : ",sum )
        if dice != 6:
                break
           
        else:
                
                continue
print("the list of dice is :",timei)
#print("Sum of dice throws: ",sum)
