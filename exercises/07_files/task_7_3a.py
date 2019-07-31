# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

template = ' {:<4} {:>16}   {}'
with open('CAM_table.txt', 'r') as src:
    lines = src.readlines()
    flines = []
    for line in lines:
        if 'DYNAMIC' in line:
            vmi = line.split()
            vmi.remove('DYNAMIC')
            vmi[0] = int(vmi[0])
            flines.append(vmi)
    flines.sort()
    for line in flines:
        print(template.format(*line))
