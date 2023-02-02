def account(name, number, balance = 100):
    return {'name' : name, 'number' : number, 'balance' : balance}

# 顯示 {'name': 'Justin', 'balance': 100, 'number': '123-4567'}
print(account('Justin', '123-4567')) 
# 顯示 {'name': 'Monica', 'balance': 1000, 'number': '765-4321'}
print(account('Monica', '765-4321', 1000))