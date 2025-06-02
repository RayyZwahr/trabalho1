def loginUsuario(perfil):  #criando a função com o parametro usuário
    if perfil.lower() == "admin": #se o usuário digitar admin (usando a função lower para converter as letras para minusculo) 
        print ("Bem-vindo, administrador!")
    else: #se digitar qualquer outra coisa
        print ("bem-vindo, usuario!.")
    

loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')
