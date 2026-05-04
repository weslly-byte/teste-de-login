
# dados "fixos" (simulado um banco de dados simples)
usuario_correto = "admin"
senh_correta = "1234"

# Entrada do Usuário
usuario = input("Digite o usuario: ")
senha = input("Digite a senha: ")

#verificação
if usuario == usuario_correto and senha == senh_correta:
    print("Login realizado com sucesso!")
else:
    print("Usuario ou senha incorretas.")