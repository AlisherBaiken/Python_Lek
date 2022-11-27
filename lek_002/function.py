# import funcii s drugogo faila
#  import i imyz faila

# import hello as h  # as h dlya dalneiwego sokrawenia print(h.f(1))

# print(hello.f(1))


# def new_string(symbol, count):
#     return symbol + count

# print(new_string('!', 5)) # !!!!!
# print(new_stirng('!'))  # Type error missing 1 required


# def concatenatio(*param):
#     res: str = ''  # dlya togo choby rabotat chislami res = 0 togda print(concatenatio(4)) vydast 12 umnojaet
#     for items in param:
#         res += items
#     return res

# print(concatenatio('a', 's', 'd'))
# print(concatenatio('a','1','d'))
# # print(concatenatio(1,2,3,)) TypeErorr

# def fib(n):
#     if n in [1,2]:
#        return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34
# # ################### Korteji ################################
# a = 1, 3, 4, 5
# # a[0] = 12 dlya kortejei ne rabotaet
# print(a)
# print(a[0])
# print(a[-2]) # poluchenie predposlednego chisla
# print(a[-1]) ## poluchenie poslednego chisla
# for item in a:
#     print(item)

######### Slovar ###########################
dictionary = {}
dictionary = \
    {
        'up': 'strelka verh',
        'down': 'strelka vniz',
        'left': 'strelka v levo',
        'right': 'strelka v pravo'
    }
# 'up':'strelka verh','down': 'strelka vniz','lef': 'strelka v levo','right' : 'strelka v pravo'
print(dictionary)
print(dictionary['left'])  # Strelka v levo
for k in dictionary.keys():
    print(k)

######### Mnojestva @##################
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a \
 .union(b) \
 .difference(a.intersec)