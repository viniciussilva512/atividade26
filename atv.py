# Exercício Python 26: Desenvolva um programa que leia o primeiro termo e a razão de uma Pogreçao Aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input("Digite o primeiro termo da Progressão Aritmética: "))
razao = int(input("Digite a razão da Progressão Aritmética: " ))

termo_atual = primeiro_termo 

print("OS 10 primeiros termos da Progressão Aritmética são: ")
for _ in range(10):
    print(termo_atual, end=' ')
    termo_atual += razao 