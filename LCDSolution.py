# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 4:52:13 2018

@author: Orion
"""    
while True:
    datainput = input('Ingrese tamaño y numero \'size,###\': ')
    if datainput == '0,0': break;#Condicion de finalización    
    while True:
        try:
            size = int(datainput.split(',')[0])#Separando el tamaño
            number = int(datainput.split(',')[1])#Separando el numero
            break;
        except:
            print('No es un numero valido')
   
        
    print('Tamaño: ' + str(size) +' Numero: '+ str(number))
    
    sizerow = size*2 +3
    sizecol = size + 2
    
    for i in range(sizerow):#Recorriendo las filas 
        for j in str(number):
            if j == '0':
                if i in [0,sizerow-1]:
                    print('*' + '-'*sizecol + '* ',end='')#Segmento centro 
                else:
                    print('|' + ' '*(sizecol) + '| ',end='')#Segmento doble vertical
            if j == '1':#Numero 1
                if i in [0,sizerow//2,sizerow-1]:
                    print('* ',end='')
                else:
                    print('| ',end='')
            if j == '2':#Numero 2
                if i in [0,sizerow//2,sizerow-1]:
                    print('*' + '-'*sizecol + '* ',end='')#Segmento centro 
                elif i > 0 and i < sizerow//2:
                    print(' '*(sizecol+1) + '| ',end='')#Segmento derecha
                else:
                    print('|' + ' '*(sizecol+2),end='')#Segmento izquierda
            if j == '3':#Numero 3
                if i in [0,sizerow//2,sizerow-1]:
                    print('*' + '-'*sizecol + '* ',end='')#Segmento centro 
                else:
                    print(' '*(sizecol+1) + '| ',end='')#Segmento derecha
            if j == '4':#Numero 4
                if i == 0:
                    print('*' + ' '*(sizecol) + '* ',end='')#Segento centro vacio
                elif i > 0 and i < sizerow//2:
                    print('|' + ' '*(sizecol) + '| ',end='')#Segmento doble vertical
                elif i == sizerow//2:
                    print('*' + '-'*sizecol + '* ',end='')#Segmento centro
                else:
                    print(' '*(sizecol+1) + '| ',end='')#Segmento  derecha
            if j == '5':#Numero 5
                if i in [0,sizerow//2,sizerow-1]:
                    print('*' + '-'*sizecol + '* ',end='')#Segmento centro
                elif i > 0 and i < sizerow//2:
                    print('|' + ' '*(sizecol+2),end='')#Segmento izquierda
                else:
                    print(' '*(sizecol+1) + '| ',end='')#Segmento  derecha
            if j == '6':#Numero 6
                if i in [0,sizerow//2,sizerow-1]:
                    print('*' + '-'*sizecol + '* ',end='')#Segmento centro
                elif i > 0 and i < sizerow//2:
                    print('|' + ' '*(sizecol+2),end='')#Segmento izquierda
                else: 
                    print('|' + ' '*(sizecol) + '| ',end='')#Segmento doble vertical
            if j == '7':#Numero 7
                if i == 0:
                    print('*' + '-'*sizecol + '* ',end='')#Segmento centro
                else:
                    print(' '*(sizecol+1) + '| ',end='')#Segmento  derecha
            if j == '8':#Numero 8
                if i in [0,sizerow//2,sizerow-1]:
                    print('*' + '-'*sizecol + '* ',end='')#Segmento centro
                else:
                    print('|' + ' '*(sizecol) + '| ',end='')#Segmento doble vertical
            if j == '9':#Numero 9
                if i in [0,sizerow//2,sizerow-1]:
                    print('*' + '-'*sizecol + '* ',end='')#Segmento centro
                elif i > 0 and i < sizerow//2:
                    print('|' + ' '*(sizecol) + '| ',end='')#Segmento doble vertical
                else:
                    print(' '*(sizecol+1) + '| ',end='')#Segmento  derecha
        print('')
print('FIN DE PROGRAMA')