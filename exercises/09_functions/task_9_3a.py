# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config_filename):
    intf_a = {}
    intf_t = {}
    intf = ''
    mode = ''
    vlan = ''
    with open(config_filename, 'r') as src:
        for line in src:
            if line.startswith('interface ') and 'Ethernet' in line:
                intf = line.split()[1]
                mode = ''
                vlan = ''
            elif 'switchport mode' in line:
                mode = line.split()[-1]
            elif ' access vlan ' in line or ' allowed vlan ' in line:
                vlan = line.split()[-1]
            elif not line.startswith(' '):
                if mode != '' and vlan != '':
                    if mode == 'access':
                        intf_a[intf] = int(vlan)
                    elif mode == 'trunk':
                        intf_t[intf] = [ int(i) for i in vlan.split(',') ]
                    else:
                        print('SOMETHING WENT WRONG')
                elif mode == 'access':
                    intf_a[intf] = 1
                mode = ''
                vlan = ''
    result = (intf_a, intf_t)
    return result

get_int_vlan_map('config_sw2.txt')
