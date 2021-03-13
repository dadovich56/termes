import sys
from colorama import Fore
import os
banner = '''
▀█▀ █▀▀ █▀█ █▀▄▀█ █▀▀ █▀
░█░ ██▄ █▀▄ █░▀░█ ██▄ ▄█'''
print(Fore.GREEN + banner)
d = input('создать сессию или подключиться к чужой? создать/подключиться:')
if(d=='подключиться'):
 a = input('введите хост:')
 b = input('введите порт:')
 print('для отключения ctrl + c')
 os.system("ncat " + a + " " + b)
elif(d=='создать'):
 ba = input('укажите порт:')
 print('для отключения ctrl + c')
 os.system("ncat -l -p " + ba)
else:
 print('введите один из данных аргументов')
