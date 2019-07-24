# -*- coding: utf-8 -*-
'''
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip = '192.168.3.1'

octets = ip.split('.')

o1,o2,o3,o4 = [int(oct) for oct in octets]

template = f"""{o1:<8}  {o2:<8}  {o3:<8}  {o4:<8}
{o1:08b}  {o2:08b}  {o3:08b}  {o4:08b}"""

print(template)
