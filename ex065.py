while True:
    num = int(input('Digite a tabuada que você quer ver?'))
    if num < 0:
        break
    print('=-'*20)
    for c in range(1, 10):
        print('{} x {} = {}'.format(num, c, num*c))
    print('=-'*20)