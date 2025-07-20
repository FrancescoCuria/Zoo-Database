# test interi stringhe
def testEqual(x, y):
    """ Controlla se x e y sono uguali e restituisce 1 se non lo sono e
    0 se lo sono"""
    if x == y:
        print("Pass")
        return 0
    else:
        print("Not Passing")
        return 1


# test eccezioni, passati se le eccezioni vengono lanciate correttamente
def testEccezione(eccezione, funzione, *args):
    """ Controlla che la funzione sollevi l'eccezione specificata
    """
    try:
        funzione(*args)
        print("Not Passing")
        return 1
    except eccezione:
        print("Pass")
        return 0
    except Exception as e:
        print("Not Passing")
        print(e)
        return 1