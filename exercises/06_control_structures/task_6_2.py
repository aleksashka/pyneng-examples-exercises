# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip = input('Enter IP address: ')
o1 = int(ip.split('.')[0])

if o1 >= 1 and o1 <= 223:
    ip_type = 'unicast'
elif o1 >= 224 and o1 <= 239:
    ip_type = 'multicast'
elif ip == '255.255.255.255':
    ip_type = 'local broadcast'
elif ip == '0.0.0.0':
    ip_type = 'unassigned'
else:
    ip_type = 'unused'

print(ip_type)
