#coding=utf-8
'''
另一道经典编程题。

功能描述：遍历并打印0到100，如果数字能被3整除，显示Fizz；
如果数字能被5整除，显示Buzz；如果能同时被3和5整除，就显示FizzBuzz。
结果应该类似：0,1,2，Fizz，4，Buzz，6……14，FizzBuzz，16……
'''
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