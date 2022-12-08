# A brief description of the project
# Date
# CTI-110 P5HW2 - Math Quiz
# Nizar Alsaidi
#       
import random

def main():
    print('Welcome to Math Quiz\n')
    while True:
        print('MAIN MENU')
        print('-------------------')
        print('1. Adding Random Numbers')
        print('2. Subtracting Random Numbers')
        print('3. Exit\n')
        choice = input('Please choose one of the menu options: ')
        if choice == '1':
            addProblem()
        elif choice == '2':
            subProblem()
        elif choice == '3':
            print('Thank you for playing...\nBye!!')
            break

def addProblem():
    a = random.randint(20,90)
    b = random.randint(20,90)
    print(f' {a}')
    print(f'+{b}')
    print('Enter answer.')
    ans = int(input())
    while ans!=(a+b):
        if ans<(a+b):print('Sorry, guess is too low.')
        else: print('Sorry, guess is too high.')
        ans = int(input('try again:'))
    print('Congratulations!!!! your answer is correct...\n')

def subProblem():
    a = random.randint(20, 90)
    b = random.randint(20, 90)
    if a<b:a,b=b,a
    print(f' {a}')
    print(f'-{b}')
    print('Enter answer.')
    ans = int(input())
    while ans != (a - b):
        if ans < (a - b):
            print('Sorry, guess is too low.')
        else:
            print('Sorry, guess is too high.')
        ans = int(input('try again:'))
    print('Congratulations!!!! your answer is correct...\n')

main()



    
