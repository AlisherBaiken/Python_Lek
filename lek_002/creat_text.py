# with open('file.text', 'w') as data:
#     data.write("Line1\n")
#     data.write("Line2\n")

color = ['red','blue', 'green']
data = open('file.text', 'a')
data.writelines(color) # razdilitelei ne budet
data.close()

exit()

path = 'file.text'
data = open(path, 'r')
for line in data:
    print(line)
data.close()    