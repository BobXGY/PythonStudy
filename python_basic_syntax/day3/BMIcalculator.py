#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# BMI calculator

height = input('请输入你的身高(m)')
weight = input('请输入你的体重(kg)')

bmi = float(weight) / pow(float(height), 2)
print('BMI:{:.2f}'.format(bmi))

who, nat = '', ''

if bmi < 18.5:
    who, nat = '偏瘦', '偏瘦'

elif 18.5 <= bmi < 24:
    who, nat = '正常', '正常'

elif 24 <= bmi < 25:
    who, nat = '正常', '偏胖'

elif 25 <= bmi < 28:
    who, nat = '偏胖', '偏胖'

elif 28 <= bmi < 30:
    who, nat = '偏胖', '肥胖'

elif bmi >= 30:
    who, nat = '肥胖', '肥胖'

print('{}(who),{}(nat)'.format(who, nat))
