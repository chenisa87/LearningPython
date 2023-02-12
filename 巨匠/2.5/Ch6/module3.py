import random

fruits = ['香蕉', '蘋果', '橘子', '西瓜']
mychoice = random.choice(fruits)
print(fruits)
yourchoice = input('請選擇上列水果: ')
if(mychoice==yourchoice):
    print('你的選擇和我相同!')
else:
    print('你的選擇和我不同!我選'+mychoice)
