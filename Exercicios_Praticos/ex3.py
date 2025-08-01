usuario_correto = "admin"
senha_correta = "1234"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Acesso permitido!")
else:
    print("Nome de usuário ou senha incorretos.")