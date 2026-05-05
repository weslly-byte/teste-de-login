
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

    usuario = {
  "admin": "1234"

}
  
tentativas = {}

def verificar_login(usuario, senha):
    
    # validação de tipo
    if not isinstance(usuario, str) or not isinstance(senha, str):
       return False
    

    # limite de tamanho
    if len(usuario) > 100 or len(senha) > 100:
        return False
    

    #controle de tentativas
    if usuario not in tentativas:
        tentativas[usuario] = 0

    if tentativas[usuario] >= 5:
       return "bloqueado"
    
    if usuario in usuario and usuario[usuario] == senha:
        tentativas[usuario] = 0
        return True
    
    else:
        tentativas[usuario] += 1
        return False
    
    def criar_conta(usuario, senha):
        if not isinstance(usuario, str) or not isinstance(senha, str):
            return "Campos_invalidos"
        
        if len(usuario) > 100 or len(senha) > 100:
            return "Campos vazios"
        
        if usuario in usuario:
            return "usuario_existe"
        
        usuario[usuario] = senha
        return "Sucesso"