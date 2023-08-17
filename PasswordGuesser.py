import random
import time  # Don't forget to import time!

my_password = "abcdefghij"
guess_num = 0
done = False

letters = 'abcdefghijklmnopqrstuvwxyz'
start_time = time.time()  # Get the start time

while not done:
    guessed_pw = ""

    for i in range(10):
        guessed_pw += random.choice(letters)
    
    guess_num += 1

    if guessed_pw == my_password:
        end_time = time.time()  # Get the end time
        execution_time = end_time - start_time  # Calculate execution time

        if execution_time > 60:  # Check if it took more than 60 seconds
            print("Took too long to find the password!")
        else:
            print("Found it after", guess_num, "tries within", execution_time, "seconds!")
        
        done = True
