data = [x for x in range(10) ]
res = list(filter(lambda x:  not x%2, data ))
print(res)



data = '1 2 3 8 37 38'.split()

res = map(int, data)
res = filter(lambda x:  not x%2, res )
res = list(map(lambda x: (x, x**2), res))
print(res)