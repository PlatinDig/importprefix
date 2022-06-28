import pynetbox
import ipaddress
import openpyxl
oldPrfx=''

def chekPrefix(subnet):
    ipn = ipaddress.IPv4Interface(subnet)
    prfx = ipn.network
    print(prfx)
    return prfx

def addingToNetBox(prfx):
    netbox = pynetbox.api(
        'http://localhost:8000',
        token='0123456789abcdef0123456789abcdef01234567'
    )
    # print('ведите префикс')
    new_prfx = netbox.ipam.prefixes.create({"prefix": str(prfx), "status": "active"})
    # new_device = nb.dcim.devices.create(**device_parameters)
    print(new_prfx)

print('Скрипт запущен')
#for j in range(2,7):
book = openpyxl.load_workbook(filename="/Users/mihailivanov/Desktop/IPTEST.xlsx") #Указать путь к файлу
sheet = book['Лист1'] # Указать книгу из которой считывать столбцы
for i in range(2,7):  # X Количество строк
    subnet = sheet['A' + str(i)].value #
    print(subnet)
    prfx = chekPrefix(subnet)
    if prfx != oldPrfx:
        addingToNetBox(prfx)
    oldPrfx = prfx