# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

vlan = input('Enter VLAN number: ')
template = ' {:<4} {:>16}   {}'
with open('CAM_table.txt', 'r') as src:
    lines = src.readlines()
    flines = []
    for line in lines:
        if 'DYNAMIC' in line:
            vmi = line.split()
            vmi.remove('DYNAMIC')
            if vmi[0] == vlan:
                vmi[0] = int(vmi[0])
                flines.append(vmi)
    flines.sort()
    for line in flines:
        print(template.format(*line))
