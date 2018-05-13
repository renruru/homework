# file = open("ceshi.txt",'w')
# file.write("wwwwwww")
# file.close()

# with open("ceshi.txt",'r') as file2:  #读 参数为长度
#     # file2.write("aaaaaaaa")
#     print(file2.read(10))

# with open("ceshi.txt",'w') as file2: #写
#     file2.write("aaaaaaaa")
  

# with open("ceshi.txt",'r') as file2:  #读 参数为长度
#     # file2.write("aaaaaaaa")
#     file2.seek(0,0)
#     print(file2.tell())  #tell方法表示当前的光标位置


# import os
# file = os.remove('111.txt')
# print(file)

# file1 = open('111.txt','w')
# file1.close()

# print(os.getcwd()) #获取当前的路径
# os.chdir('D:') #切换路径
# os.system('python -V') #终端操作
# os.mkdir('ru') #创建一个文件夹
# os.rmdir('ru')  #移除文件夹


import os
import subprocess

# def openfile():
#     file = open('D:/hello/log.txt','a+')
#     file.write(str(os.system('python -V')))
#     file.close()

# if os.path.exists('D:/hello'):
#     openfile()
# else:
#     os.mkdir('D:/hello')
#     openfile()


# os.remove('D:\hello\log.txt')
# os.rmdir('D:\hello')

try:
    os.mkdir('D:/hello')
except Exception as ms:
    print(ms)
finally:
    file = open('D:/hello/log.txt','a+')
    # file.write(str(os.system('python -V')))
    filea = subprocess.Popen('python -V',stdout=subprocess.PIPE)
    fileb = filea.stdout.read()
    file.write(str(fileb))
    file.close()
