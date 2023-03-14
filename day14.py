from random import randint
import random
# from replib import clear 

data = [
    {
        'name':"Virat kohli",
        'followers':280,
        'description':"cricketer",
        'country':"india"        
    },
    {
        'name':"Ram Charan",
        'followers':80,
        'description':"actor",
        'country':"india"        
    },
    {
        'name':"lionel messi",
        'followers':380,
        'description':"footballer",
        'country':"argentina"        
    },
    {
        'name':"Scarlet johnasson",
        'followers':100,
        'description':"actoress",
        'country':"usa"        
    },
    {
        'name':"Vladamir putin",
        'followers':20,
        'description':"President",
        'country':"Russia"        
    },
    {
        'name':"shakira",
        'followers':70,
        'description':"singer",
        'country':"spain"        
    },
    {
        'name':"ema watson",
        'followers':50,
        'description':"actoress",
        'country':"britain"        
    },    
]

score = 0
game_over = False
b = random.choice(data)

while not game_over:
    a = b
    b = random.choice(data)
    b = random.choice(data)
    while a ==b:
        b = random.choice(data)

    def format_data(acc):    
        name = acc["name"]
        description = acc["description"]
        country = acc["country"]
        return f"{name}, a {description}, from {country}"

    def check_ans(a_follower,b_follower,guess):
        if a_follower > b_follower:
            return guess =="a"
        else: 
            return guess =="b"
        

    print(f"compare A: {format_data(a)}")
    print(f"--------------- VS ---------------")
    print(f"against B: {format_data(b)}")

    guess = input("type a guess")
    a_follower = a["followers"]
    b_follower = b["followers"]
    is_correct = check_ans(a_follower,b_follower,guess)

    # clear()
    
    if is_correct:
        score = score +1
        print(f"u r right, currently score is {score}")
    else:
        game_over = True
        print("u lose !!!")


      
        

    
