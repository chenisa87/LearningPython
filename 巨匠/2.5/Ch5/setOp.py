users={'Mary','Nicole','Justin'}
print("User 集合:", users)

users.add('Sean')
print("加入Sean")
print("User 集合:", users)
users.add('Mary')
print("加入Mary")
print("User 集合:", users)

users.remove('Sean')
print("移除Sean")
print("User 集合:", users)
#users.remove('Sean')

users.discard('Mary')
print("丟棄Mary")
print("User 集合:", users)
#users.discard('Mary')

popped = users.pop()
print("彈出:", popped)
print("User 集合:", users)
print("清空:", users.clear())
print("User 集合:", users)
#users.pop()
#print("User 集合:", users)
