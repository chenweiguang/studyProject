#!coding=utf-8

'''
和猜数字一样，不过这次是设计一个能猜数字的AI
功能描述：用户输入一个单位以内的数字，AI要用最少的次数猜中，并且显示出猜的次数和数字
'''

step = 1
num = int(input("请输入你的数字:"))

guess = num / 2
middle = num / 4

while num != guess:
  #print('第%d次猜测' % step)
  if guess < num:
     guess += middle
  elif guess > num:
      guess -= middle
  middle /= 2
  if middle == 0:
      middle = 1
  step += 1
print('num is %d' % guess)
print('the total step is %d' % step)
