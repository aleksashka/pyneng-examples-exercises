# -*- coding: utf-8 -*-
'''
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

# Parse user input
net_mask = input('Enter network/prefix: ')
net_ds, mask_ps = net_mask.split('/') # Network as dotted-decimal string
                                      # Mask as prefix string

# Convert dotted-decimal network to an integer
o1, o2, o3, o4 = [int(oct) for oct in net_ds.split('.')] # Network as octets
net_i = o1*256**3 + o2*256**2 + o3*256**1 + o4*256**0    # Network as an integer

# Print input network in decimal and binary forms
net_template = f"{o1:<8}  {o2:<8}  {o3:<8}  {o4:<8}\n{o1:08b}  {o2:08b}  {o3:08b}  {o4:08b}"
print('Input network:\n' + net_template)

# Convert mask from prefix to binary to integer
mask_pi = int(mask_ps)                               # Mask as prefix integer
mask_bs = '1' * mask_pi + ( '0' * ( 32 - mask_pi ) ) # Mask as binary string
o1 = int(mask_bs[0:8],2)
o2 = int(mask_bs[8:16],2)
o3 = int(mask_bs[16:24],2)
o4 = int(mask_bs[24:32],2)
mask_i = o1*256**3 + o2*256**2 + o3*256**1 + o4*256**0 # Mask as an integer
# Prepare template to print mask later
print_mask = f"{o1:<8}  {o2:<8}  {o3:<8}  {o4:<8}\n{o1:08b}  {o2:08b}  {o3:08b}  {o4:08b}"

# Apply mask to network and print network and mask in decimal and binary forms
net_i = net_i & mask_i        # Network AND mask to zeroize host bits
net_bs = format(net_i,'032b') # Binary format, padded with 0 to 32
o1 = int(net_bs[ 0: 8],2)
o2 = int(net_bs[ 8:16],2)
o3 = int(net_bs[16:24],2)
o4 = int(net_bs[24:32],2)
print_net = f"{o1:<8}  {o2:<8}  {o3:<8}  {o4:<8}\n{o1:08b}  {o2:08b}  {o3:08b}  {o4:08b}"

print('Output network:\n' + print_net)
print('Mask:\n' + print_mask)
