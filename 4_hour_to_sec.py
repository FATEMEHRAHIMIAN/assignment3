

from select import select


select_1 = input("Do you want to convert\n (1) hours to seconds? \n  or \n (2)seconds to hours? \n ")
if select_1== "1":
        #hour to secound 
        hour= int(input("Enter your hour: \n"))
        minute= int(input("Enter your minute: \n"))
        secound= int(input("Enter your secound: \n"))
        hour_c = hour * 3600
        minute_c = minute*60
        to_secound = int(hour_c + minute_c + secound)
        print ("your time is " , hour,":",minute,":",secound)
        print("your time in secound is :",to_secound)
elif select_1 == "2" :
        secound= int(input("Enter your secound: \n"))
        hour = secound // 3600
        # to_secound = (hour*60)+(minute*60)+secound
        minute = (secound - (hour * 3600 ) )//60
        secound_time =( secound -  ((hour *3600) - (minute * 60) )) %60 
        print(" your time is", hour,":",minute,":",secound_time)
else :
    print("nothing :( ")