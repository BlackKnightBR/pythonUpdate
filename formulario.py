'''
    Crie um formulário que pergunte nome, idade, altura cpf, endereço, email e telefone e
    os imprima em um formulário organizado.

 '''
print('Bem vindo!')
print('_________________________________________')
name = input('Digite seu nome')
age = input('Digite sua idade')
height = input('Digite sua altura')
weight = input('Digite seu peso')
email = input('Digite seu email')
tel = input('Digite seu telefone')
print('_________________________________________')
print('_________________________________________')
print('Formulário de cadastro industrias pom pom')
print('_________________________________________')
print('Sua informação pessoal:')
print('Seu nome: ', name)
print('Idade: ', age, 'Altura: ', height)
print('_________________________________________')
print('Informação de contato:')
print('Email: ', email)
print('Telefone: ', tel)
print('_________________________________________')
print('_________________________________________')

'''
    Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e decide
    se ela está apta a entrar no exercíto (18 a 30 anos), pesar mais ou igual a 60kg
    e medir mais ou igual a 1,70 metros.
 '''
if(int(age) >= 18 and int(age) <= 30 and int(weight) <= 60 and float(height) <= 1.70):
    print('Você está apto a entrar no exercíto')

print('_________________________________________')
print('_________________________________________')
