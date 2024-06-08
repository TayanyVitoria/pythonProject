import math
a = float(input('Digite ângulo que você quer:'))
sen = math.sin(math.radians(a))
print('O seno desse ângulo é {:.2f}'.format(sen))
cos = math.cos(math.radians(a))
print('O cosseno desse ângulo é {:.2f}'.format(cos))
tan = math.tan(math.radians(a))
print('A tangente desse ângulo é {:.2f}'.format(tan))
