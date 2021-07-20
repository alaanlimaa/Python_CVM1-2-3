price = float(input('Qual preço do produto? R$'))
final = price - (price * 0.05)
print('O valor final do produto com desconto de 5% é R${:.2f} !'.format(final))
