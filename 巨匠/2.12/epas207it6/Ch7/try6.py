num1 = 10
num2 = 0
nums = [1,3,5,7,9]
try:
    print(num1/num2)
    print(num1*num3)
    print(nums[100])
except ZeroDivisionError:
    print('Error發生，除以0')
except NameError:
    print('Error發生，使用沒有宣告過的變數')
except IndexError:
    print('Error發生，索引值超出範圍')
except:
    print('Error發生')
finally:
    print('結束')