def number(n,b):
    for i in range(n):
        print("{0:^50}".format(b*(2*i-1)))
    print()

def main():
    number(int(input("")),str(input("")))
main()