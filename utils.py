def validar_campo_vacio(*args):
    for arg in args:
        if not arg or arg.strip() == "":
            return False
    return True
