#python123.io
#lenthConverter

lenth = input()
if lenth[-1] == 'm':
    print('{:.3f}in'.format(eval(lenth[0:-1])*39.37))
elif lenth[-1] == 'n':
    print('{:.3f}m'.format(eval(lenth[0:-2])/39.37))