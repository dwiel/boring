import itertools
import random

symbol = "*"
format = "{x} {symbol} {y}"
x_low = 2
x_high = 9
y_low = 1
y_high = 12

x = set(range(x_low, x_high + 1))
y = set(range(y_low, y_high + 1))

problems = itertools.product(x, y)
problems = list(problems)
problems = [(x, y, eval(format.format(x=x, y=y, symbol=symbol))) for x, y in problems]

print(f"{len(problems)} total problems")

correct = 0
total = 0
random.shuffle(problems)
for x, y, answer in problems:
    print(format.format(x=x, y=y, symbol=symbol))
    student_answer = input().strip()
    
    if student_answer == str(answer):
        print("correct")
        correct += 1
    else:
        print(f"incorrect. correct answer is: {answer}")
    total += 1

    print(f"{correct} correct out of {total}: ({correct/total * 100:.00f}% correct)")
