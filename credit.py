userInput =  input("Input Credit Card: ") 
cards =  {"AMEX":3, 'VISA':4, "MASTERCARD":5}

if len(userInput) > 16 or len(userInput) < 15:
    print("INVALID")
else:
    
    for key, value in cards.items():
    # print(f"Key: {key} , Value:{value}")
        if(int(userInput[0]) == value):
            print(key)
        else:
            print("INVALID")
    

 
 
    
