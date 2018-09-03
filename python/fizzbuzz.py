#coding=utf-8

FizzBuzz = []
Fizz = []
Buzz = []
for num in range(0,101):
  # print('数字是%d' % num)
  if num % 3 == 0 and num % 5 == 0:
    # print('数字是%d,FizzBuzz' % num)
    FizzBuzz.append(num)
    continue
  if num % 3 == 0:
    # print('数字是%d,Fizz' % num)
    Fizz.append(num)
    continue
  if num % 5 == 0:
    # print('数字是%d,Buzz' % num)
    Buzz.append(num)


FizzBuzz.append('FizzBuzz')
Fizz.append('Fizz')
Buzz.append('Buzz')
print(FizzBuzz,Fizz,Buzz)