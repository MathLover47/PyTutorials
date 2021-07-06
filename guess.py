import random
x = random.randint(0,9)
max_attempts = 3
No_of_attempts = 0
while  No_of_attempts < max_attempts:
    guess = int(input("guess it(0-09) for attempt"+ str(No_of_attempts+1)+" :"))
    if guess == x:
        print("you've guessed correctly congradulations !!!!!!")
        break
    No_of_attempts += 1
else:
    print("you run out of attempts you lost chance")