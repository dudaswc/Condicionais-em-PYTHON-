1- Faça um programa que leia dois números, calcula e imprime a soma.
Caso a soma seja par, calcula e imprime a metade da soma.

numero1=float(input("Digite o primeiro número: "))
numero2=float(input("Digite o segundo número: "))
soma=numero1+numero2
print("A soma é:", soma)

if soma%2==0:
    print("A soma é par:", soma/2)


2- Escreva um algoritmo que leia os valores de dois lados adjacentes de uma figura geométrica e informe se eles representam um quadrado perfeito ou um retângulo. 
Caso represente um retângulo, informe o tamanho do maior lado.
*Quadrado perfeito é aquele que possui todos os lados iguais.

lado1=float(input("Digite o valor do lado 1:"))
lado2=float(input("Digite o valor do lado 2:"))

if lado1==lado2:
    print("Oba, quadrado perfeito!")
else:
    print("Oba, é um retângulo")
    if lado1>lado2:
       print("O lado 1 é maior e apresenta o valor de:", lado1)
    else:
       print("O lado 2 é maior e apresenta o valor de:", lado2)

3- Faça um programa que leia dois números e calcule a divisão do primeiro pelo segundo. 
Porém, se o usuário digitar zero para o segundo número, não realize o cálculo e apresente uma mensagem de erro “Não pode ser feita divisão por zero!”.

numero1=float(input("Digite número 1:"))
numero2=float(input("Digite número 2:"))
if numero2==0:
     print("Não pode ser feita divisão por zero!")
else:
    divisao=float(numero1/numero2)
    print("A divisão é:", divisao)

4- Faça um programa que solicite ao usuário que digite um valor para a variável num. Verifica o número digitado e informa se o é positivo, negativo ou zero. 
Caso o número seja positivo, apresente o seu dobro. Caso o número seja negativo, informe se ele é par ou ímpar.

num=float(input("Digite o número: "))
dobro=num*2

if num>0:
    print("O número é positivo!")
    print("Seu dobro é:", dobro)
elif num<0:
    print("O número é negativo")
    if num%2==0:
       print("O número é par")
    else:
        print("O número é ímpar")
else:
    print("O número é 0")

5- Ler dois valores e um código de condição. Se o código for “c” os valores devem ser escritos em ordem crescente. 
Se o código for “d”, deve-se escrevê-los em ordem decrescente.

num1=float(input("Digite o primeiro número:"))
num2=float(input("Digite o segundo número:"))
codigo=input("Digite o código:")

if codigo=="c":
    if num1>num2:
        print(num2,"-",num1)
    else:
        print(num1,"-", num2)
elif codigo=="d":
    if num1<num2:
        print(num2,"-",num1)
    else:
        print(num1,"-", num2)

6- Um posto está com uma promoção, de forma que oferece os seguintes descontos, de acordo com a quantidade abastecida:
● de 20 a 30 litros o desconto é de 5%; e
● acima de 30 litros o desconto é de 10%.
Elabore um algoritmo que leia a quantidade de litros e o tipo de combustível (A - Álcool ou G - Gasolina), calcule e imprima o valor a ser pago, 
sabendo-se que o preço do litro da gasolina é de R$ 7.00 e o preço do litro do álcool é de R$ 5.00.

qtd=float(input("Digite a quantidade de litros:"))
tipo=input("Digite o tipo de combustível:")
gasolina=7
alcool=5

if qtd<20:
    if tipo=="Gasolina":
        print("O valor deu:", qtd*7, "reais")
    elif tipo=="Alcool":
        print("O valor deu:", qtd*5, "reais")
elif 20<=qtd<=30:
    if tipo=="Gasolina":
        print("O valor deu:", qtd*7*0.95, "reais")
    elif tipo=="Alcool":  
        print("O valor deu:", qtd*5*0.95, "reais")
else:
    if tipo=="Gasolina":
        print("O valor deu:", qtd*7*0.90, "reais")
    elif tipo=="alcool":
        print("O valor deu:", qtd*5*0.90, "reais")

7- Uma companhia de saneamento calcula o valor da conta de água de acordo com o tipo de consumidor:
- Residencial: R$ 5.00 de taxa mais R$ 0.05 por m³ gasto;
- Comercial: R$ 500.00 para os primeiros 80 m³, acrescido de R$ 0.25 por m³ gastos acima dos 80 m³;
- Industrial: R$ 800.00 para os primeiros 100 m³, acrescido de R$ 0.04 por m³ gastos acima dos 100 m³.
Baseando-se nessas informações, escreva um algoritmo que leia o tipo do cliente e o seu consumo de água em metros cúbicos. 
Depois, calcule e apresente a conta de água a ser paga pelo cliente.

cliente=input("Insira o tipo do cliente: ")
consumo=float(input("Digite o consumo em m³: "))
residencial=5+0.05*consumo
comercial=(consumo-80)*0.25+500
industrial=(consumo-100)*0.04+800

if cliente=="Residencial":
    print("O valor da conta de água foi:", residencial, "reais")
elif cliente=="Comercial":
    if consumo<=80:
        print("O valor da conta de água foi:", 500, "reais")
    else:
        print("O valor da conta de água foi:", comercial, "reais")
else:
    if consumo<=100:
        print("O valor da conta de água foi:", 800, "reais")
    else:
        print("O valor da conta de água foi:", industrial, "reais")
  
8- Usando apenas as instruções vistas até o momento, escreva um algoritmo que receba a data de aniversário de duas pessoas (pessoa1 e pessoa2), 
sendo que a data consiste em dia, mês e ano (três variáveis separadas). Baseando nestas datas, informe se as duas pessoas têm a mesma idade ou,
em caso negativo, informe qual é a mais velha.

nome1=input("Digite seu nome:")
dia1=int(input("Digite apenas o dia do seu aniversário:"))
mes1=int(input("Digite apenas o mês do seu aniversário:"))
ano1=int(input("Digite apenas o ano do seu aniversário:"))

nome2=input("Digite seu nome:")
dia2=int(input("Digite apenas o dia do seu aniversário:"))
mes2=int(input("Digite apenas o mês do seu aniversário:"))
ano2=int(input("Digite apenas o ano do seu aniversário:"))

if (ano1-ano2)<0:
    print(nome2, "é mais velho(a)")
elif (ano1-ano2)>0:
    print(nome1, "é mais velho(a)")
elif ano1==ano2:
     if mes1>mes2:
        print(nome2, "é mais velho(a)")
     elif:
          print(nome1, "é mais velho(a)")
elif ano1==ano2:
     if mes1==mes2:
     elif dia1>dia2:
          print(nome2, "é mais velho(a)")
          else:
               print(nome1, "é mais velho(a)")
else:
    print("As duas pessoas têm a mesma idade.")
    
