
#coding=utf8

'''猜字游戏
        1.让玩家输入猜数字，根据提示最终找到匹配的数字获取奖励
        2.每次都是生成的数字，不固定。
        3.游戏次数为3
'''
import random
import sys
secret = random.randint(1,9)
print(secret)
print("我们玩个猜数字游戏吧，请在0到9选一个")

frequency = 1
guess = input("请输入你猜的数字:")
num = int(guess)

if num != secret:
  if num < secret:
    print("猜错了，小了，在猜猜")
  else:
    print("猜错了，大了,在猜猜")
else:
    print("运气真的好哟,我们真是心有灵犀")
    sys.exit(0)

while frequency != 3:

  frequency = frequency + 1
  guess = input("请输入你猜的数字:")
  num = int(guess)

  if num == secret:
     print("运气真的好哟")
     print("我们真是心有灵犀")
     sys.exit(0)
  else:
    if num < secret:
      print("猜错了，小了，在猜猜")
    else:
      print("猜错了，大了,在猜猜")
print("机会已用完")
print("在玩一次吧")