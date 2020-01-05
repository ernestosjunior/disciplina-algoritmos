print('CALCULADORA')
n1=float(input('Digite o primeiro número: '))
n2=float(input('Digite o segundo número: '))
print
''' 
Operadores:

[+] Adição
[-] Subtração
[*] Multiplicação
[/] Divisão
'''
op=input('Digite o operador: ')
if op=='+':
    print(n1+n2)
elif op=='-':
    print(n1-n2)
elif op=='*':
    print(n1*n2)
else:
    op=='/'
    print(n1/n2)

