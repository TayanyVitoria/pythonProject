produto = float(input('Digite o preço do produto:'))
print('FORMAS DE PAGAMENTO:\n[1]Á vista (dinhero ou cheque)\n[2]Á vista no cartão\n[3]2x no cartão\n[4]3x ou mais no cartão')
pagamento = int(input('ESCOHA A FORMA DE PAGAMENTO DIGITANDO APENAS O NÚMERO:'))
if pagamento == 1:
    des = produto - (10/100)
    print('O valor do seu produto com 10% de desconto pela forma de pagamento ficou: R${:.2f}'.format(des))
elif pagamento == 2:
    des = produto - (5/100)
    print('O valor do seu produto com 5% de desconto pela forma de pagamento ficou: R${:.2f}'.format(des))
elif pagamento == 3:
    parcela = produto/2
    print('O valor total do seu pedido é: R${:.2f}, e o valor parcelado em 2x ficou: R${:.2f}'.format(produto,parcela))
elif pagamento == 4:
    juros = produto + (produto * 20/100)
    parcela = int(input('Quantas parcela:'))
    total = juros / parcela
    print('O valor total do seu pedido com o juros pela forma de pagamento é: R${:.2f} e o valor parcelado em {}x ficou {:.2f}'.format(juros, parcela, total))
else:
    print('opção inválida, escolha uma das opções!!!')