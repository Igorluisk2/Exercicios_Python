#3 faça um programa com uma função chamada "somaImposto". A função possui dois parâmetros formais: "taxaImposto", que é a quantia de imposto sobre vendas expressa
# em porcentagem e "custo", que é o custo de um item antes do imposto. A função "altera" o valor de custo para incluir o imposto sobre vendas

'''def somaImposto(custosemimposto,taxaImposto):
    valorfinal=custosemimposto+custosemimposto*taxaImposto/100
    return  valorfinal
a=float(input("Custo sem imposto: "))
b=float(input("Taxa do imposto: "))
x=somaImposto(a,b)
print(x)
'''

#4 Faça um programa que converta da notação de 24 horas para notação de 12 horas. Por exemplo, o programa deve converter 12:00. Por exemplo, o programa deve converter 14:25 em 2:25 p.m.
# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor "A" para A.M. e "P"
# para P.M. Assim, a função para efetuar as conversões terá um parametro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores
# de entrada todas as vezes que desejar.

'''def converter_horario(horas, minutos):
    if horas == 0:
        horas12 = 12
        periodo = "A"
    elif horas < 12:
        horas12 = horas
        periodo = "A"
    elif horas == 12:
        horas12 = 12
        periodo = "P"
    else:
        horas12 = horas - 12
        periodo = "P"
    return horas12, minutos, periodo

def exibir_horario(horas12, minutos, periodo):
    print(f"{horas12}:{minutos:02d} {periodo}.M.")

while True:
    horas = int(input("Digite a hora que deseja converter (0-23): "))
    minutos = int(input("Digite os minutos (0-59): "))

    if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
        print("Entrada inválida. Tente apenas numeros entre 0 e 23 para horas e 0 a 59 para minutos.")
        continue

    horas12, minutos, periodo = converter_horario(horas, minutos)
    exibir_horario(horas12, minutos, periodo)

    repetir = input("Deseja converter outro horário? (S/N): ")
    if repetir.upper() != "S":
        break'''

#5 Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o
# número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então
# exibir o valor a ser pago na tela. Após a execução programa deverá ser encerrado, exibindo o relatorio do dia,
# que conterá a quantidade e o valor totral de prestações pagas no dia. O cálcilo do valor a ser pago é feito da seguinte forma.
# Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(valor_prestacao, dias_atraso):
    if dias_atraso == 0:
        return valor_prestacao
    else:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * (0.001 * dias_atraso)
        return valor_prestacao + multa + juros

# Variáveis do relatório
total_prestacoes = 0
total_valor_pago = 0

while True:
    valor = input("Digite o valor da prestação (ou '0' para encerrar): ")
    valor = float(valor)

    if valor == 0:
        break

    dias_atraso = int(input("Digite o número de dias em atraso: "))

    valor_a_pagar = valorPagamento(valor, dias_atraso)
    print(f"Valor a ser pago: R${valor_a_pagar:.2f}")

    total_prestacoes += 1
    total_valor_pago += valor_a_pagar

# Exibir relatório
print("----- Relatório do Dia -----")
print(f"Quantidade de prestações pagas: {total_prestacoes}")
print(f"Valor total pago: R${total_valor_pago:.2f}")
