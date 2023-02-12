greet = "Hi,ed"

print(id(greet), "->", greet)

#greet[3]="E"
#greet = greet[:3]+"E"+greet[4:]
greet = greet.replace("e","E")

print(id(greet), "->", greet)
