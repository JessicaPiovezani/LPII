idade_mulheres = []
idade_homens = []

print("Cadastro idade mulheres")
for i in range(2):
    idade = int(input("Digite a idade: "))
    idade_mulheres.append(idade)

print("\nCadastro idade homens")
for i in range(2):
    idade = int(input("Digite a idade: "))
    idade_homens.append(idade)

mais_velhos = max(idade_homens) + max(idade_mulheres)
print("\nA soma de idades da mulher mais velha e do homem mais velho é de:", mais_velhos)

mais_novos = min(idade_homens) + min(idade_mulheres)
print("\nA soma de idades da mulher mais nova e do homem mais novo é de:", mais_novos)