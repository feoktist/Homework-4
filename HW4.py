# --------------------- МОДУЛЬ 1 -----------------------------

def simple_separator(x):
  a = x * 10
  return a

ukrashenie = (input('Введите ваш элемент декорации: '))
print(simple_separator(ukrashenie))

# -----------------------------------------------------------
def long_separator(count):
  a = '*' * count
  return a
    
length = int(input('Введите длину разделителя из звездочек: '))
print(long_separator(length))

# -----------------------------------------------------------
def separator(simbol, count):
  a = simbol * count
  return a
  
symbol = input('Введите символ декорации: ')
num_repeat = int(input('Введите количество повторений: '))

print(separator(symbol, num_repeat))

# -----------------------------------------------------------
def hw():
  print('**********')
  print('Hello World!')
  print('##########')
  return

hw()

# -----------------------------------------------------------
def hello_who(who):
  print('**********')
  print('Hello ', who,'!')
  print('##########')

name = input('Enter name: ')
print('\n')
hello_who(name)
print('\n')

# -------------------------------------------------
def pow_many(power, *args):
  result = 0
  for num in args:
    result += num
  otvet = result ** power
  return otvet

print(pow_many(1, 1, 2))  
print(pow_many(1, 2, 3))
print(pow_many(2, 1, 1))
print(pow_many(3, 2))
print(pow_many(2, 1, 2, 3, 4))

# -------------------------------------

def print_key_val(**kwargs):
  for k, v in kwargs.items():
    print(k, ' --> ', v)
  
  
  
   

print_key_val(name = 'Max', age = 21)
print('\n')
print_key_val(animal = 'Cat', is_animal = True)
print('\n')

# ----------------------------------------------

def my_filter(iterable, function):
  res = filter(function, iterable)
  res = list(res)
  return res

a = [1,2,3,4,5]
b = ['a', 'b', 'c', 'd', 'e']



f0 = lambda x: x > 3
f1 = lambda x: x == 2
f2 = lambda x: x != 3
f3 = lambda x: x in 'abba'

print(my_filter(a, f0))
print(my_filter(a, f1))
print(my_filter(a, f2))
print(my_filter(b, f3))




# ======================= MODULE 2 =====================================

import random

years = {'Alex':1968, 'Bob': 1978, 'Charlie': 1988}
months = {'Alex' : 4, 'Bob': 3, 'Charlie': 5}
days = {'Alex':22, 'Bob': 1, 'Charlie': 25}
yob = years.keys()

person = random.choice(list(yob))

# -----------------------------------------------------------
def guessworks(w_data, dude_name, say):
  while say != w_data[dude_name]:
    print('Wrong answer! Try again! ')
    say = int(input(f'Enter your answer: '))
    if say == w_data[dude_name]:
      print('Gotcha!')
      print(10 * '-')
# -----------------------------------------------------------
answer = int(input(f'Enter YoB for writer {person}: '))
print(40 * '-')
guessworks(years, person, answer)

answer = int(input(f'Now guess MoB for writer {person}: '))
print(40 * '-')
guessworks(months, person, answer)

answer = int(input(f'Now guess DoB for writer {person}: '))
print(40 * '-')
guessworks(days, person, answer)

#================= MODULE 3 ========================================



user_account = 0
purchases = []
history = {}
while True:
    print('\n')
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    
    choice = input('Выберите пункт меню: ')
    print('\n')

    if choice == '1':
      account_topup = int(input('Введите сумму пополнения: '))
      user_account = user_account + account_topup
      
        
    elif choice == '2':
      sum_purchase = int(input('Введите сумму покупки: '))
      if sum_purchase > user_account:
        print('Недостаточно средств')
      else:
        stuff = input('Введите название покупки: ')
        purchases.append(stuff)
        user_account = user_account - sum_purchase
        history[stuff] = sum_purchase


        
    elif choice == '3':
      
      print('Funds left: ', user_account)
      
      print('History of purchases: ')
      for k, v in history.items():
        print(k, v)

        
    elif choice == '4':
      break
        
    else:
        print('Неверный пункт меню')







