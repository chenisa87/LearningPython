def get_sum(a, b=3, c=5):
    return a + b + c

x = get_sum(1, 2, 3)
print("get_sum(1, 2, 3) ->", x)

y = get_sum(1, 2)
print("get_sum(1, 2) ->", y)

z = get_sum(1)
print("get_sum(1) ->", z)

w = get_sum()
print("get_sum() ->", w)
