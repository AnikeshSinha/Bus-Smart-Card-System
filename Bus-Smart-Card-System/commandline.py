# from json.decoder import JSONDecodeError  # import the JSONDecodeError exception
import operations                    # import the operations module
import json                          # import the json module
from json import JSONDecodeError     # import the JSONDecodeError exception

print("Welcome to Automated Bus Smart Card System app")

c = 1
while True:     # loop until the user enters the correct choice
    print("Press:")
    print("1. Register a new Smart Card user")
    print("2. Login")
    print("3. Exit")
    try:
        c = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number")
        continue
    if c == 1:
        print("Registering a new Smart Card 💳 user :")
        print("Enter your Full name:  ")
        FullName = input()
        print("Enter your email:  ")
        Email = input()
        print("Enter your Password:  ")
        Password = input()
        print("Enter your Money to Recharge:  ")
        Money = input()
        if (len(FullName)*len(Email)*len(Password)) == 0 or '@' not in Email or '.com' not in Email:
            print("Please Enter Valid Data , All fields are required")
            continue
        else:
            operations.Register('Travellers.json' , FullName, Email, Password , Money)
            print("Registration Successful 💰")
    
    elif c == 2:
        print("Login to your Smart Card 💳 user :")
        print("Enter your email:  ")
        Email = input()
        print("Enter your Password:  ")
        Password = input()
        s = operations.Login('Travellers.json' , Email , Password)
        if s == False:
            print("Invalid Email or Password")
            continue
        else:
            print("Login Successful 💰")
            print("Welcome to your Smart Card 💳 user")
            trav = open('Travellers.json' , 'r')
            data = json.load(trav)
            trav.close()
            nam = ""
            for i in range(len(data)):
                if data[i]['Email'] == Email and data[i]['Password'] == Password:
                    nam = data[i]['FullName']
                    Smart_Id = data[i]['Card_ID']
                    break
            print(f'Welcome 🙏: {nam} Your Smard Card ID is :💳  {Smart_Id}' )

            while True:
                print("Press:")
                print("1. Recharge your Smart Card")
                print("2. Start Your Awesome Journey")
                print("3. Journey Completed")
                try:
                    c = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid input. Please enter a number")
                    continue

                if c == 1:
                    print("Enter your Money to Recharge:  ")
                    Money = int(input())
                    if Money <= 0:
                        print("Please Enter Valid Data , All fields are required")
                        continue
                    else:
                        operations.Recharge('Travellers.json' ,'transactions.json', Smart_Id , Money)
                        print("Recharge Successful 💵💵💵💰")

                elif c == 2:
                    print("From which Stops you want to start your journey:  ")
                    fromStops = int(input())
                    print("To which Stops you want to end your journey:  ")
                    toStops = int(input())
                    
                    # check if the stops are in range
                    if (fromStops < 1 or fromStops > 15) or (toStops < 1 or  toStops > 15):  

                        print("Please Enter Valid Stop Between Stops 1 to 15.")
                        continue
                    else:
                        your_total_Stops = abs(toStops) - abs(fromStops)  # calculate the total stops
                        print(f'Your journey will take {your_total_Stops} stops')
                        operations.JourneyStarted('Travellers.json' , Smart_Id , your_total_Stops)  # update the journey started status

                elif c == 3:
                    print("Journey Completed 🚌🚌🚌")
                    print(" Visit Again 🚍🚍🚍")
                    break

                else:
                    print("Invalid Input")
                    continue

    elif c == 3:
        print("Thank you for using our app 💖, Have a nice day 💖")
        break
    else:
        print("Invalid Input ⚔️ , Please Enter a valid input")
        continue
