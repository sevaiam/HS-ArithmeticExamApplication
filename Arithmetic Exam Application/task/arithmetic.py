# write your code here
from random import randint
from random import choice


def create_task(task_lvl=1):
    new_task = ''
    if task_lvl == 1:
        operators = '+', '-', '*'
        new_task += str(randint(2, 9)) + ' '
        new_task += choice(operators) + ' '
        new_task += str(randint(2, 9))
    elif task_lvl == 2:
        new_task = str(randint(11, 29))
    return new_task


def check_user_input(u_solution, min_val=-1000, max_val=10000):
    try:
        correct_solution = int(u_solution)
        if min_val <= correct_solution <= max_val:
            return correct_solution
        return False
    except ValueError:
        print('Incorrect format.')
        return False

level = input('''Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29''')
while not check_user_input(level, 1, 2):
    level = input('''Which level do you want? Enter a number:
    1 - simple operations with numbers 2-9
    2 - integral squares of 11-29''')
level = check_user_input(level, 1, 2)

task_counter = 0
correct_answers = 0
while task_counter < 5:
    task = create_task(task_lvl=level)
    print(task)
    if level == 1:
        solution = eval(task)
    elif level == 2:
        solution = eval(task) ** 2
    user_solution = input()
    while not check_user_input(user_solution):
        user_solution = input()
    user_solution = check_user_input(user_solution)
    if solution == user_solution:
        print('Right!')
        correct_answers += 1
    else:
        print('Wrong!')
    task_counter += 1

print('Your mark is ', correct_answers, '/', task_counter)
save_prompt = input('Would you like to save your result to the file? Enter yes or no.')
if save_prompt.lower() in 'yes':
    user_name = input('What is your name?')
    if level == 1:
        level_desc = 'simple operations with numbers 2-9'
    elif level == 2:
        level_desc = 'integral squares 11-29'
    user_text = f'{user_name} {correct_answers}/{task_counter} in level {level} ({level_desc}).'
    with open('results.txt', 'a') as file:
        file.write(user_text)
        print('The results are saved in "results.txt".')

