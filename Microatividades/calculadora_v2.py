saida = '' #criando uma variável em branco

def adicao(num1, num2):  #função para somar
    return num1 + num2

def subtracao(num1, num2): #função para subtrair
    return num1 - num2

def multiplicacao(num1, num2): #função para multiplicar
    return num1 * num2

def divisao(num1, num2): #função para dividir
    if num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return num1 / num2

def calculadora(num1, num2, operacao):  #função para definir o tipo de operação
    if operacao == '+' or operacao.lower() == 'adicao': # realiza a função "adicao()" se for digitado os termos + ou "adicao"
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtracao': # realiza a função "subtracao()" se for digitado os termos - ou "subtracao"
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao': # realiza a função "multiplicacao()" se for digitado os termos * ou "multiplicacao"
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisao': # realiza a função "divisao()" se for digitado os termos / ou "divisao"
        resultado = divisao(num1, num2) 
    else:
        resultado = "Operação inválida" 
    
    return resultado

while saida.lower() != 'n': #cria uma estrutura que se repete até a variavel saida ser diferente de 'n'
        numero1 = float(input("Digite o primeiro número: "))  #pede o primeiro numero e armazena na variavel numero1
        numero2 = float(input("Digite o segundo número: ")) #pede o segundo numero e armazena na variavel numero2
        operacao = input("Digite a operação (+, -, *, /) ou o nome (adicao, subtracao, multiplicacao, divisao): ") #pede o tipo de operação que será realizado

        resultado = calculadora(numero1, numero2, operacao) #chama a função calculadora

        print("Resultado da operação:", resultado) #imprime o resultado
        saida = input("Deseja continuar? (S/N): ") # se digitado "n" o while se repete, caso contrário encerra e pula para prixima linha.

print("Programa encerrado.")
