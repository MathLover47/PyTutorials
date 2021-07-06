import math
import random
max = 100
min = 1
print("This program for simulating guessing number from 1 to 100 in binary search")
guessed = False
number = random.randint(1,100)
attempts = 1
while not guessed:

    mid = max + min // 2
    guessedNumber = random.randint(min,max)
    attempts +=1
    if guessedNumber == number :
        print(f'you guessed correctly in this {attempts } times it is really {mid}')
        guessed = True
        break



    if  guessedNumber < number :
        print(f'number {number} is greater than {mid}')
        min = mid +1
    elif guessedNumber  > number :
        print(f'number {number}is less than {mid}')
        max = mid -1
    if min > max :
        print("unhandled error")
        break
    attempts += 1
