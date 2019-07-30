# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip_s = input('Enter IP address: ')

if ip_s == '' or not '.' in ip_s:
    print('Wrong IP entered')
    quit()

# IP in the form of a list of strings
ip_ls = ip_s.split('.')
if len(ip_ls) != 4:
    print('Wrong IP entered')
    quit()
ip_li = [int(oct) for oct in ip_ls]
ip_s = ''
for oct in ip_li:
    if oct >= 0 and oct <= 255:
        # Allow entering leading zeroes
        ip_s = ip_s + '.' + str(oct)
    else:
        print('Wrong IP entered')
        quit()
ip_s = ip_s.strip('.')

o1 = ip_li[0]
if o1 >= 1 and o1 <= 223:
    ip_type = 'unicast'
elif o1 >= 224 and o1 <= 239:
    ip_type = 'multicast'
elif ip_s == '255.255.255.255':
    ip_type = 'local broadcast'
elif ip_s == '0.0.0.0':
    ip_type = 'unassigned'
else:
    ip_type = 'unused'

print(ip_type)
