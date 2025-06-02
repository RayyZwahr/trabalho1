def loginUsuario(perfil):
    if perfil.lower() == "admin":
        print ("Bem-vindo, administrador!")
    else:
        print ("bem-vindo, usuario!.")
    

loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')