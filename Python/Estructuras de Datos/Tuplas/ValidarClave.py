_valid_aplha_mail = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890-_."

while True:
    _user = input("Ingrese el codigo: ")
    if(len(_user)>4):
        a=set(_valid_aplha_mail)
        b=set(_user)
        if len(b-a)>0:
            print("Usuario Invalido.")
            continue
        else:
            print("usuario Valido.")
            break
    else:
        print("Usuario Invalido.")