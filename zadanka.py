#Zadanie 1 - input PRACTICEPYTHON.ORG
'''
print ("Hello, my name is Miłosz and I'm 22 years old. What is your name?")
name = input('Tap your name here:')
print('Nice too meet you', name, 'How old are you?')
age = int(input('Tap your age here:'))
old = 100 - age
year = int 
year = 2019 + old
print("You have", old,"years left, untill you're going too be 100 years old in", year)
print('And one more thing. Can you choose a random number?')
number = int(input('Tap your number here:'))

print(("You have", old,"years left, untill you're going too be 100 years old in", year) *number)
'''

#Zadanie 2
'''
number = int(input('Choose a random number:'))
even = number % 2
if even % 4 ==0:
    print('surprise')
elif even ==0:
    print ('even')

else:
    print('odd')

'''

#Zadanie 3
'''
a = [1,1,2,3,5,8,13,21,34,55,89]

for nums in a:
    if nums <5:
        print(nums)
    else:
        pass

nowa =[]

for nums in a:
    if nums <5:
        nowa.append(nums)
        print (nowa)
    else:
        pass

print({nums for nums in a if nums <5})

print('Hello, choose a number:')
number = int(input())
print([nums for nums in a if nums<number])
'''

#Zadanie4
'''
number = int(input('Choose a number:'))
x = []
a = range(2,11)
for i in a:
    if number % i ==0:
        x.append(i)
    else:
        pass
print(x)
'''

#Zadanie 5
'''
a = [ 1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
c = []
for i in a:
    if i in b:
        print(i)
        c.append(i)
    else:
        pass
print(c)

import random

d = random.sample(range(1, 100))
e = random.sample(range(1, 100))
print(d)
'''
#zadanie 6
'''
string = str(input("Tap in a random word:"))
pal = string[::-1]
if pal ==string:
    print('This word is palindrome')
else:
    print('This word is not palindrome')
'''

#zadanie 7
'''
a = [1,4,9,16,25,36,49,64,81,100]
b = []
for i in a:
    if i%2 ==0:
        b.append(i)
        print('This element is even:', i)
    else:
        print('This element is odd', i)
print(b)
'''

#zadanie8
'''
import sys


user1 = input('Player 1, CHOOSE paper, rock or scissors:')
user2 = input('Player 2, CHOOSE paper, rock or scissors:')

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

'''
'''
import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))

'''

#Zadanie 9
'''
import random

a = int(random.randint(1, 9))
takes = 0
while True:
    b = int(input('Choose a random number between 1 and 9: '))
    takes +=1
    if a==b:
        print('You won')
        print('Takes number: ', takes)
        break
    elif a<b:
        print('The number you chosen is too high')
    elif a>b:
        print('The number you chosen is too low')
    elif b=="exit":
        break

    '''

#Zadanie 10
'''
import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [i for i in a if i in b]
print(c)

d = random.sample(range(1,50), 10)
e = random.sample(range(1,50), 11)
print(d,e, sep='\n')
f = [i for i in d if i in e]
print(f)
'''

#Zadanie 11 - Not done
'''
a = list(range(1,10))
print(a)

num = int(input('Podaj liczbe'))
lista = list(range(1, num))
for i in lista:
    if num%i == 0:
        print('Not prime')
    elif num%i != 0:
        print('Number', num, 'Is prime')
'''

#Zadanie 12
'''
a = []
while len(a)<6:
    lista = input('Podaj 5 liczb po przecinku:'+'\n')
    a.append(lista)
    print(a)

def funkc(x):
    return [x[0], x[-1]]
print(funkc(a))
'''

#Zadanie 13

'''
def Fibonnaci():
    a = int(input('How many Fibonnaci numbers you want to generate?:'+'\n'))
    f = []
    if a ==0:
        print('Fibonnaci = ', f)
    elif a ==1:
        f = [1]
        print('Fibonnaci =', f)
    elif a ==2:
        f = [1,1]
        print('Fibonnaci =', f)
    elif a>2:
'''
'''
a=int(input('Please input number: '))
if a==1:
    b=[1]
elif a!=1:
    b=[1,1]
    for i in b:
        if len(b)<a:
            i= b[-1]+b[-2]
            b.append(i)
            print(b)
'''     
#Zadanie 14
'''
a = []
b=[]
while len(a) < 6 and len(b) <6:
    z = input('Podaj liczbe:')
    x = input('Podaj liczbe2:')
    a.append(z)
    b.append(x)

print(a)
print(b)
'''
'''
import random
a = random.sample(range(1,50), 20)
b = random.sample(range(1,50), 20)
print(a, b, sep='\n')
c=[]
def wspolne(arg1, arg2):
    for i in arg1:
        if i not in arg2:
            c.append(i)
    return c
        
wspolne(a, b)
print(c)
'''
'''
import random
a = [1,2,2,3,3,4,4,5,5,6,6,6]
a = set(a)
print(a)
'''

#Zadanie 15
'''
in = str(input('Write somthing:'))
spl = in.split()
c = spl[::-1]
print(c)
'''

#Zadanie random
'''
import random
r = int(input('Podaj liczbę osób: '))
liczba = random.randint(1, r)
print(liczba)
'''
'''
import random
def losowanko(arg1):
    liczba = random.randint(1, arg1)
    print('Liczba', liczba)
losowanko(8)
'''
'''
import random

l = []

while True:
    uczestnicy = str(input('Podaj imiona uczestników. Jeżeli dodałeś już wszystkich wpisz break: '))
    if 'break' in uczestnicy:
        break
    else:
        l.append(uczestnicy)
        print(l)

losowanko = random.choice(l)
print(losowanko)
'''

#Zadanie 16

'''
import random
a= list(range(0,10))
b = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
c = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
d = ['~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']',':',';','"','<','>',',','.','?','/']
e = a+b+c+d
f=[]
proba = int(input('Podaj liczbę znaków. Im więcej znaków podasz tym hasło będzie silniejsze: '))

ran = range(0, proba)
print(ran)
for i in ran:
    if i <= proba:
        g = random.choice(e)
        f.append(g)
    elif i>proba:
        break

print(f)
'''

#Zadanie 17

