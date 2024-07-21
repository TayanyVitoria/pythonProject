print('-='*14)
print('\033[1;32mSEQUÊNCIA DE FIBONACCI\033[m')
print('-='*14)
seq = int(input('Quantos termos você quer ver: '))
contador = 3
t1 = 0
t2 =1
print('{} ➜ {}'.format(t1,t2),end =' ')
while contador <= seq:
    t3 = t1 + t2
    print('➜ {}'.format(t3),end=' ')
    t1 = t2
    t2 = t3
    contador+= 1
print('FIM')