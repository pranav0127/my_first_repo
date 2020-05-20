#while loop
i = 0
while i <= 5:
    print("*" * i)
    i = i + 1
print("done")

i = 0
while i < 6:
    print(i)
    i+=1
print("done")

i = 0
while i <= 5:
    print(" * * " * i)
    print("" * i)
    i = i + 1
print("done")


#build a guess game with while loop
secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count+=1
    if guess == secret_number:
        print("you have won")
        break
else:
    print("you have lost")

"""
CAR GAME
>help
start = to start the car
stop = to stop the car
quit = to exit

>asd
i don't understand this
>start
car started , ready to go
>stop
car stopped
"""


command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("car started...")
    elif command == "stop":
        print("car stopped")
    elif command == "help":
        print("""
Start = to start the car
stop = to stop the car
quit = to quit        
        """)
    elif command == "quit":
        break
    else:
        print("i don't understand this")




#if we write start instruction twice then it should say cas has already stared and same with stop instruction


command = ""
started = True
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("the car is already start")
        else:
            print("car started...")
    elif command == "stop":
        if not started:
            print("the car is already stopped")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print("""
Start = to start the car
stop = to stop the car
quit = to quit        
        """)
    elif command == "quit":
        break
    else:
        print("i don't understand this")




