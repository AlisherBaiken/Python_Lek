# list = []
# for i in range(1, 21):
#     if (i%2 ==0):
#      list.append(i)
# print(list)

def f(x):
    return x**3

# list = [i for i in range(1, 21) if i % 2 == 0]
# list = [(i,i) for i in range(1, 21) if i % 2 == 0] # spisok kartejei  
list = [f(i) for i in range(1, 21) if i % 2 == 0] # vozvedenie v tret stepen
list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0] # kortej pokazyvaet chislo i ego tretiu chislo 

print(list)


