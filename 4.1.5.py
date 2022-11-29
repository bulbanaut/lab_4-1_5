#! /usr/bin/python3
paws = 64
geese = 32
while geese >= 0:
    print('Гуси: ', geese, '; Кролики: ', int((paws - geese*2) / 4))
    geese = geese - 2