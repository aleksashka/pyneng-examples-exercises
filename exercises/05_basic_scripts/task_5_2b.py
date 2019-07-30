# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

# Parse user input
net_mask = argv[1]
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
