import os
# print(os.getcwd())
# os.mkdir('Movies')
# os.chdir('D:\stuff')
# print(os.path.exists('movies'))

# if os.path.exists('movies'):
#     print('Already Exist')
# else:
#     os.mkdir('movies')    

# open('file.txt','a').close()
# os.mkdir('D:\stuff\movies')

# print(os.listdir())

# for item in os.listdir():
#     path =os.path.join(os.getcwd(),item)
#     print(path)    

for item in os.listdir('d:\scan'):
    path =os.path.join('d:\scan',item)
    print(path)    