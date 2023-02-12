import sys
import traceback

def b():
    print('執行b()')
    num1 = 10
    num2 = 0
    try:
        print(num1/num2)
    except:
        cls, msg, trace = sys.exc_info()
        print(cls)
        print(msg)
        traceback.print_tb(trace)

    print('b()結束')   

def a():
    print('執行a()')
    b()    
    print('a()結束')   
    
        
print('執行main()')
a()
print('main()結束')
