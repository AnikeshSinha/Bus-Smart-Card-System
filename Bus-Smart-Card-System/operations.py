from ast import Break  # import the break statement
import json            # import the json module
import string          # import the string module
import random          # import the random module
from json import JSONDecodeError # import the json module
from datetime import datetime ,time # import the datetime module

def SmartCardID(): # generate a random card id

    # Generate a random string of length 6
    # with letters and numbers
    # and return it

    Card_ID = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return Card_ID # return the card id

def Register(Travellers_Json_file,FullName,Email,Password,Money): # Register a new user

    with open(Travellers_Json_file, 'r+', encoding = 'utf-8') as f: 
        # open the file in read and write mode

        d = { # create a dictionary
            'FullName': FullName,       # add the key and value
            'Email': Email,             # add the key and value
            'Password': Password,       # add the key and value
            'Money': Money,             # add the money to the dictionary
            'Card_ID': SmartCardID(),   # generate a random card id
            'Register_Date': datetime.now().strftime("%d/%m/%Y") # get the current date
        }
        try:             # try to load the data from the file
            data = json.load(f)         # load the data from the file

            # Add the new user to the data

            if d not in data:           # if the user is not in the data
                data.append(d)          # add the user to the data

                # Overwrite the old data with the new data

                f.seek(0)               # move the cursor to the beginning of the file
                f.truncate()                  # truncate the file
                json.dump(data, f, indent=4)  # write the data to the file

        except JSONDecodeError:       # if the file is empty

            # If the file is empty, create a new list

            l = []                      # create a new list
            l.append(d)                 # add the user to the list
            f.seek(0)                   # move the cursor to the beginning of the file
            json.dump(l, f, indent=4)   # write the data to the file
        

def Login(Travellers_Json_file,Email,Password):      # Login a user  
    d = 0
    with open(Travellers_Json_file, 'r+', encoding = 'utf-8') as f: 
        # open the file in read and write mode

        try:
            data = json.load(f)
        except JSONDecodeError:
            return False
        for i in range(len(data)):
            if data[i]['Email'] == Email and data[i]['Password'] == Password:  
                # if the user is in the data
                d = 1
                break
        if d == 0:
            return False
        else:
            return True

def Recharge(Travellers_Json_file, transactions_Json_file ,Card_ID,Money): 
    # recharge the user's account

    fp = open(Travellers_Json_file, 'r+', encoding = 'utf-8')
    try:
        jsonData = json.load(fp)
    except JSONDecodeError:
        return False

    for i in range(len(jsonData)):
        if jsonData[i]['Card_ID'] == Card_ID:  # if the user is in the data

            jsonData[i]['Money'] = float(jsonData[i]['Money']) + float(Money) # add the money to the user's account

            break
    fp.seek(0)
    fp.truncate()
    json.dump(jsonData, fp, indent=4)
    fp.close()

    fp = open(transactions_Json_file, 'r+', encoding = 'utf-8') 
    try:
        jsonData = json.load(fp)
    except JSONDecodeError:
        return False

    d = { # create a dictionary
        'Card_ID': Card_ID,              # add the key and value
        'Money': Money,                  # add the money to the dictionary
        'Date': datetime.now().strftime("%d/%m/%Y"),  # get the current date
        'Time': datetime.now().strftime("%H:%M:%S")   # get the current time
    }
    jsonData.append(d)
    fp.seek(0)
    fp.truncate()
    json.dump(jsonData, fp, indent=4)
    fp.close()
    return True


def JourneyStarted(Travellers_json_file , Card_ID , Your_total_Stops): # start a journey
    now = datetime.now()
    now_time = now.time()

    fare = 0    # the fare of the journey

    if now_time >= time(23,00) or now_time <= time(6,00):
         # if the journey is between midnight and 6am

        fare = 0.60 * (Your_total_Stops)
        if Your_total_Stops > 5: 
            # if you have more than 5 stops then you will get 20% long distance discount 
            discount = fare * 20 / 100
            fare = fare - discount
            if (datetime.today().weekday() == 5) or (datetime.today().weekday() == 6): # if today is a weekend day discount extra 10%
                discount = fare * 10 / 100
                fare = fare - discount

    elif now_time > time(6,00) and now_time < time(23,00): 
        # if the journey is between 6am and midnight

        fare = 0.80 * (Your_total_Stops)  # the fare of the journey

        if Your_total_Stops > 5: 

            # if you have more than 5 stops then you will get 20% long distance discount
            discount = fare * 20 / 100   # calculate the discount
            fare = fare - discount       # calculate the fare

            # if today is a weekend day discount extra 10%
            if (datetime.today().weekday() == 5) or (datetime.today().weekday() == 6):  
                discount = fare * 10 / 100   # calculate the discount
                fare = fare - discount       # calculate the fare
    
    with open(Travellers_json_file, 'r+', encoding = 'utf-8') as f:
        try:
            data = json.load(f)
        except JSONDecodeError:
            return False
        for i in range(len(data)):

            if data[i]['Card_ID'] == Card_ID: 
                # if the user is in the data

                if float(data[i]['Money']) < 10:  
                    # if the user has less than 10 $ money
                    print("You don't have enough money 💵 to start Awesome journey 🚌")
                    return False

                else:
                    total = float(data[i]['Money']) - float(fare) 
                    # deduct the fare from the user's account

                    data[i]['Money'] = round((total),2) 
                    # round the money to 2 decimal places

                    print(f"Your 💵 Fare is: ${fare} Cents")  # print the fare
                    print(f"Your 💵 Total $ Left in your Smart Card : ${data[i]['Money']} Cents") # print the total

                    if data[i]['Money'] < 0:
                        print("You don't have sufficient balance 💵 to complete this Awesome Journey 🚌")
                        return False
                    break

        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=4)
        return True


    

    
    



        




    


