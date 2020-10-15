valor_produto = float (input("Valor do produto: "))
valor_desconto = float (input ("Digite o valor do desconto: "))
valor_produto  = valor_produto - valor_desconto
valor_recebido = float (input("Valor a ser trocado: "))
troco = valor_recebido - valor_produto
print("O valor do troco será de:", troco)

