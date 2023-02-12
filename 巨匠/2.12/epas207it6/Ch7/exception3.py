import sys
import traceback

def b():
    print('執行b()')
    num1 = 10
    num2 = 0
    print(num1/num2)
    print('b()結束')   

def a():
    print('執行a()')
    b()    
    print('a()結束')   
    
        
print('執行main()')
try:
    a()
except:
    cls, msg, trace = sys.exc_info()
    print(cls)
    print(msg)
    traceback.print_tb(trace)
print('main()結束')
