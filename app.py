#Run Code btn doesn't work with input. Run with << python3 app.py >> in terminal
import random

score = 0
number_of_qs = int(input('How many practice problems would you like?  '))

for i in range(number_of_qs):
    num1 = random.randint(1,12)
    num2 = random.randint(1,12)
    answer = num1 * num2

    attempt = int(input(f'{num1} * {num2}  '))

    if attempt == answer:
        print(f'Correct! guess:{attempt} answer:{answer}')
        score +=1
    else:
        print(f'Incorrect, guess:{attempt} answer:{answer}')
        continue

score_percentage = int((score / number_of_qs) * 100)

print(f'Thanks for practicing! \nYou got {score} / {number_of_qs} correct. \nFinal score: {score_percentage}%')
