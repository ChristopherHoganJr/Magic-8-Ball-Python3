import random

# Ask the user what the question is
userQuestion = str(input('What is your question for the 8 ball?: '))

# Random number between 0 and 19
randomChoice = random.randint(0,19)

# Fill text for the magic 8 ball game
print('The magic 8 ball says:')

if randomChoice == 0:
    print('It is certain.')
elif randomChoice == 1:
    print('It is decidedly so.')
elif randomChoice == 2:
    print('Without a doubt.')
elif randomChoice == 3:
    print('Yes definitely.')
elif randomChoice == 4:
    print('You may rely on it.')
elif randomChoice == 5:
    print('As I see it, yes.')
elif randomChoice == 6:
    print('Most likely.')
elif randomChoice == 7:
    print('Outlook good.')
elif randomChoice == 8:
    print('Yes.')
elif randomChoice == 9:
    print('Signs point to yes.')
elif randomChoice == 10:
    print('Reply hazy, try again.')
elif randomChoice == 11:
    print('Ask again later.')
elif randomChoice == 12:
    print('Better not tell you now.')
elif randomChoice == 13:
    print('Cannot predict now.')
elif randomChoice == 14:
    print('Concentrate and ask again.')
elif randomChoice == 15:
    print('Don\'t count on it.')
elif randomChoice == 16:
    print('My reply is no.')
elif randomChoice == 17:
    print('My sources say no.')
elif randomChoice == 18:
    print('Outlook not so good.')
elif randomChoice == 19:
    print('Very doubtful.')


    