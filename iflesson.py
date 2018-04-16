#-*- coding: UTF-8 -*- 
grade = int(raw_input("请输入成绩:"))
# grade = 70
print(grade)
if 80 <= grade <= 100:
    print('good!')
elif 60 <= grade < 80:
    print('just so so!')
elif 0 < grade < 60:
    print('bad!')
else:
    print('erro')