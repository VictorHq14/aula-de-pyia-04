while True:
    resp = int(input("digite 0 para sair, 1 para somar, 2 para subtrair, 3 para dividir e 4 para multiplicar:  "))
    if resp == 4:
        numero1 = float(input("digite um numero que você quer multiplicar"))
        numero2 = float(input("digite o outro numero que você quer multiplicar"))
        def mult(a,b):
            return a*b
        result4 = mult(numero1,numero2)
        print(result4)
        
    elif resp == 3:
        numero1 = float(input("digite um numero que você quer dividir"))
        numero2 = float(input("digite o outro numero que você quer dividir"))
        def divi(a,b):
            return a/b
        result3 = divi(numero1,numero2)
        print(result3)
        
    elif resp == 2:
        numero1 = float(input("digite um numero que você quer subtrair"))
        numero2 = float(input("digite o outro numero que você quer subtrair"))
        def sub(a,b):
            return a-b
        result2 = sub(numero1,numero2)
        print(result2)
        
    elif resp == 1:
        numero1 = float(input("digite um numero que você quer somar"))
        numero2 = float(input("digite o outro numero que você quer somar"))
        def soma(a,b):
            return a+b
        result1 = soma(numero1,numero2)
        print(result1)
        
    elif resp == 0:
        print("encerrando programa")
        break
    else:
        print("Tente novamente")
