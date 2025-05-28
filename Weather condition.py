def weather_condition(temp):
    if temp >  30 :
        print("It's very hot")
    elif temp >= 20 and (temp <= 10):
        print("It's normal")
    else :
        print("It's very cold") 


temp = int(input("Enter the temp"))
weather_condition(temp)