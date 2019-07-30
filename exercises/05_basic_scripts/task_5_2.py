# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

net_mask = input('Enter network and mask: ')
net, mask = net_mask.split('/')

o1, o2, o3, o4 = [int(oct) for oct in net.split('.')]
print_net = f"{o1:<8}  {o2:<8}  {o3:<8}  {o4:<8}\n{o1:08b}  {o2:08b}  {o3:08b}  {o4:08b}"

maski = int(mask)
maskb = '1' * maski + ( '0' * ( 32 - maski ) )
o1 = int(maskb[0:8],2)
o2 = int(maskb[8:16],2)
o3 = int(maskb[16:24],2)
o4 = int(maskb[24:32],2)
print_mask = f"{o1:<8}  {o2:<8}  {o3:<8}  {o4:<8}\n{o1:08b}  {o2:08b}  {o3:08b}  {o4:08b}"

print('Network:\n' + print_net)
print()
print('Mask:\n/' + mask + '\n' + print_mask)
