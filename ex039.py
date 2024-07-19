peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
imc = peso / altura**2
if imc <= 18.5:
    print('Seu IMC foi {:.1f}: VOCÊ ESTA ABAIXO DO PESO'.format(imc))
elif imc >= 18.6 and imc <= 25.0:
    print('Seu IMC foi {:.1f}: VOCÊ ESTA NO PESO IDEAL'.format(imc))
elif imc >= 25.1 and imc <=30.0:
    print('Seu IMC foi {:.1f}: VOCÊ ESTA COM SOBREPESO'.format(imc))
elif imc >= 30.1 and imc <= 40.0:
    print('Seu IMC foi {:.1f}: VOCÊ ESTA COM OBSIDADE'.format(imc))
elif imc <= 40.1:
    print('Seu IMC foi {:.1f}: VOCÊ ESTA COM OBSIDADE MORBIDA, CUIDADO.'.format(imc))
else:
    print('Digite um peso e uma altura válida!')