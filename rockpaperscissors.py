import random

rps = ['rock','paper','scissors']
lost = 0
won = 0
draw= 0
while True:
    p1 = str(input('Choose between paper, rock scissors:  \n'))
    ch = random.choice(rps)
    print(ch)
    if p1 == 'rock':
        if ch == 'rock':
            print('Draw')
            draw +=1
        elif ch == 'scissors':
            print('p1 won')
            won +=1
        elif ch == 'paper':
            print('You lost')
            lost +=1
    elif p1 == 'scissors':
        if ch =='scissors':
            print('Draw')
            draw +=1
        elif ch =='paper':
            print('P1 won')
            won +=1
        elif ch == 'rock':
            print('You lost')
            lost +=1
    elif p1 == 'paper':
        if ch =='paper':
            print('Draw')
            draw +=1
        elif ch =='scissors':
            print('You lost')
            lost+=1
        elif ch =='rock':
            print('You won')
            won +=1
    elif p1 == 'break':
        break


print('You won: ', won, 'times \n','You lost: ', lost,'times \n', 'You draw: ', draw, 'times')
