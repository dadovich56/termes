import sys
import os
banner = '''
▀█▀ █▀▀ █▀█ █▀▄▀█ █▀▀ █▀
░█░ ██▄ █▀▄ █░▀░█ ██▄ ▄█'''
print(banner)
d = input('создать сессию или подключиться к чужой? создать/подключиться:')
if(d=='подключиться'):
 a = input('введите хост:')
 b = input('введите порт:')
 os.system("ncat " + a + " " + b)
 print('для отключения ctrl + c')
elif(d=='создать'):
 ba = input('укажите порт:')
 os.system("ncat -l -p " + ba)
 print('для отключения ctrl + c')
else:
 print('введите один из данных аргументов')
