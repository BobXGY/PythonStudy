#python123.io
#currency

money = input()
if money[0] == 'R':
    print('USD{:.2f}'.format(eval(money[3::])/6.78))
elif money[0] == 'U':
    print('RMB{:.2f}'.format(eval(money[3::])*6.78))