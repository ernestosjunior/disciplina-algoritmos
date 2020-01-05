print('LOGIN APLICATIVO XYZ')
regrasdasenha='''
Regras para criação da senha:

* A senha tem que ter no mínimo 8 caracteres;
* Usuário e senha não podem ser iguais;
* A senha tem que conter pelo menos um caractere númerico.
'''
usuario=input("Digite o nome de usuário: ")
print(regrasdasenha)
senha=input('Digite sua senha: ')
tam = len(senha) 
while (tam<8) or (usuario==senha) or (senha.isalpha()):
    print('Senha inválida')
    senha=input('Digite sua senha: ')
    tam=len(senha)
else:
    print('Cadastro efetuado com sucesso!')
    print('Seja bem vindo(a)')
