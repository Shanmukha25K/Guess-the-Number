import random
nums = random.randint(1,100)
print('Welcome! Guess the number between 1 to 100. Let\'s Gooo!')

def loop(inp):     
        if inp not in range(1,101):
            print('Invalid input')  

        elif inp > nums:
            print('Wrong answer. It is lesser than you think')

        elif inp < nums:
            print('Wrong answer. It is greater than you think')

        elif inp == nums:
            print('Correct answer')
            exit()

for i in range(1,6):
    inp = int(input('Enter the value: '))
    loop(inp)
    print('chances left ',5-i)

print('Correct answer is ',nums)
    
