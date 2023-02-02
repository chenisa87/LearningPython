n1 = int(input())

def space(n):
    for i in range(n):
        print(" ", end="")
    
def string(n):
    for i in range(n):
        print("*", end="")
    
def all():
    for i in range(1,n1):
        space(n1-i)
        string(i)
        print()

all()