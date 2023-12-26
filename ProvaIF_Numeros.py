#len lista, onde os números serao depositados,contados e feito sua média
numeros = []
qnt = []

while True:
    #a variavel número que ira entrar na lista [numeros] e se encaixara em um if
    num = int(input('Digite números para receber a quantidade e a média entre eles, digite 0 para parar!\n'))
    #aqui ele tira a possibilidade de incluir o numero 0 na lista [numeros]
    if num > 0:
        numeros.append(num)
    #aqui o programa ira decidir se para ou continua 
    if num == 0:
        qnt = len(numeros)
        print(f'A quantidade de números informados, foi de: {qnt}\n A média entre eles é de: {sum(numeros) / (qnt)}\n')
        break
    
    else:
        continue