admins={'Justin','David'}
users={'Mary','Nicole','Justin'}

print("admins有%d人" %(len(admins)))
print("users有%d人" %(len(users)))

print("Justin是否為admins:", 'Justin' in admins)
print("David是否為users:", 'David' in users)

print("admins列表:")
for name in admins:
    print(name)
