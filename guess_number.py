import random

def guess_number(x):
    print("=================")
    print("Welcome to the game!")
    print("=================")
    print(f"Think in a number betwen 1 and {x}")
    lower_limit = 1
    upper_limit = x
    respuesta = ""
    # We don't know the number of iterations that the computer needs to guess the number entered by the user
    while respuesta != "c":
        if lower_limit != upper_limit:
            prediction =  random.randint(lower_limit, upper_limit)
        else:
            prediction = upper_limit # Could be the lower_limit
        
        respuesta = input(f"My prediction is {prediction}. if it's bigger enter (A). If it's lower enter (B). If it's correct enter (C) : ").lower()

        if respuesta == "a":
            upper_limit = prediction-1 # we decrease one because prediction is not the answer
        elif respuesta == "b":
            lower_limit = prediction+1
    print(f"The computer guessed you number: {prediction}")


guess_number(10)