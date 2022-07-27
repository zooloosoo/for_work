import os


path = input('Введите адрес папки:\n')
os.chdir(path)
file_list = ['.'.join(x.split('.')[:-1]) for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
file = open("names.txt", "w")
for k in file_list:
    file.write(k + '\n')
file.close()
