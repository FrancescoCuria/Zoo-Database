# Script di test Assegnamento 3 622AA 2024/25
# Vengono funzionalità a campione sulle classi animale, risolvere eventuali errori anche nelle classi di pari livello nella gerarchia.
# Esempio: test di tipo sbagliato del numero delle zampe in Zebra, far sì che il test sia presente anche nelle altre classi (Leone, Giraffa, Ippopotamo, etc.)
from testMy import *
from zoo import *
from animali import *

x = Zoo()
def controllo():
    #contiamo i test falliti
    testFalliti=0
    print("==========> Inizio nuovo test <=============\n\n")
    #y = 

    # creazione animali corretti
    print("==========> Test 1")
    try:
        alex = Leone("Alex", True, 4, "Ruggito", ["Terra"], 7)
        melman = Giraffa("Melman", True, 4, "Mugugno", ["Terra"], 65)
        gloria = Ippopotamo("Gloria", True, 4, "Ruggito", ["Terra", "Acqua"], 34)
        skipper = Pinguino("Skipper", True, 2, "Garrito", ["Terra", "Acqua"], False)
        kowalski = Pinguino("Kowalski", True, 2, "Garrito", ["Terra", "Acqua"], False)
        rico = Pinguino("Rico", True, 2, "Garrito", ["Terra", "Acqua"], False)
        soldato = Pinguino("Soldato", True, 2, "Garrito", ["Terra", "Acqua"], False)
        flounder = PescePagliaccio("Flounder", False, 0, "", ["Acqua"], "Salata")
        nemo = PescePagliaccio("Nemo", False, 0, "", ["Acqua"], "Salata")
        anacleto = Gufo("Anacleto", True, 2, "Bubbolio", ["Aria"], True)
    except Exception as e:
        print("Errore creazione animali corretti", e)
        exit()
    print("Pass")
    # test creazione animali sbagliati
    print("==========> Test 2")
    testFalliti += testEccezione(TypeError, Leone, 123, True, 4, "Ruggito", ["Terra"], 7)
    testFalliti += testEccezione(ValueError, Leone, "", True, 4, "Ruggito", ["Terra"], 7)
    testFalliti += testEccezione(TypeError, Giraffa, "Io", "aa", 2, "", ["Terra"], 8)
    testFalliti += testEccezione(TypeError, Giraffa, "Io", True, "due", "aaa", ["Terra"], 8)
    testFalliti += testEccezione(ValueError, Giraffa, "Io", True, -1, "aaa", ["Terra"], 8)
    print("==========> Test 2.6")
    testFalliti += testEccezione(ValueError, Ippopotamo, "Io", True, 4, "aaa", ["Ciao"], 8)
    testFalliti += testEccezione(TypeError, Ippopotamo, "Io", True, 4, "aaa", "Terra", 8)
    testFalliti += testEccezione(TypeError, Ippopotamo, "Io", True, 4, "aaa", [55], 8)
    testFalliti += testEccezione(TypeError, Ippopotamo, "Io", True, 4, "aaa", "Terra", "aaa")
    testFalliti += testEccezione(ValueError, Ippopotamo, "Io", True, 4, "aaa", ["Terra"], -1)
    print("==========> Test 2.11")
    testFalliti += testEccezione(TypeError, Pinguino, "Io", 2, True, "aaa",["Aria"], 5)
    testFalliti += testEccezione(TypeError, Pesce, "Io", 0, True, "", ["Aria"], 5)
    testFalliti += testEccezione(TypeError, Pesce, "Io", 0, True, "", ["Aria"], "Ciao")
    
    
    
    # test setter e inserimenti sbagliati
    print("==========> Test 3")
    testFalliti += testEccezione(TypeError, melman.set_nome, 123)
    testFalliti += testEccezione(ValueError, melman.set_nome, "")
    testFalliti += testEccezione(TypeError, alex.set_verso, 123)
    testFalliti += testEccezione(TypeError, nemo.set_numero_zampe, "adf")
    testFalliti += testEccezione(ValueError, alex.set_numero_zampe, -2)
    print("==========> Test 3.6")
    testFalliti += testEccezione(TypeError, gloria.set_ambiente, 123)
    testFalliti += testEccezione(TypeError, alex.set_settimane_gestazione, "ciao")
    testFalliti += testEccezione(ValueError, alex.set_settimane_gestazione, -2)
    testFalliti += testEccezione(TypeError, skipper.set_volatile, "ciao")
    testFalliti += testEccezione(TypeError, skipper.set_volatile, 123)
    print("==========> Test 3.11")
    testFalliti += testEccezione(ValueError, nemo.set_acqua, "Ciao")
    testFalliti += testEccezione(TypeError, nemo.set_acqua, 123)


    # test inserimenti
    print("==========> Test 4")
    try:
        x.inserisci(alex, "A1")
        x.inserisci(melman, "A1")
        x.inserisci(gloria, "A1")
        x.inserisci(skipper, "A2")
        x.inserisci(kowalski, "A2")
        x.inserisci(rico, "A2")
        x.inserisci(soldato, "A2")
        x.inserisci(flounder, "A3")
        x.inserisci(nemo, "A3")
        x.inserisci(anacleto, "A2")
        print("Pass")
    except Exception as e:
        testFalliti += 1
        print("Not Pass")
        print(e)     
    print("==========> Test 4.16")
    #inserimenti sbagliati
    simba = Leone("Simba", True, 4, "Ruggito", ["Terra"], 7)
    # duplicato
    testFalliti += testEccezione(KeyError, x.inserisci, alex, "A1")
    # tipo
    testFalliti += testEccezione(TypeError, x.inserisci, simba, 12)
    # valore
    testFalliti += testEccezione(ValueError, x.inserisci, simba, "A")
    testFalliti += testEccezione(ValueError, x.inserisci, simba, "5A")

    # test su __str__ animali
    print("==========> Test 5")
    
    testFalliti += testEqual(str(alex), "Il Leone (Mammifero) Alex ha 4 zampe, sangue caldo e vive in Terra facendo un Ruggito, con 7 settimane di gestazione")
    testFalliti += testEqual(str(nemo), "Il PescePagliaccio (Pesce) Nemo è senza zampe, sangue freddo e vive in Acqua Salata")
    testFalliti += testEqual(str(kowalski), "Il Pinguino (Uccello) Kowalski ha 2 zampe, sangue caldo e vive in Terra e Acqua facendo un Garrito, non sa volare")
    
    
    # test su __eq__
    print("==========> Test 6")
    testFalliti += testEqual(alex, Leone("Alex", True, 4, "Ruggito", ["Terra"], 7))
    testFalliti += testEqual(alex==Leone("Alex", True, 4, "Ruggito", ["Terra"], 7), True)
    testFalliti += testEqual(alex==gloria, False)
    testFalliti += testEqual(alex==None, False)
    testFalliti += testEqual(alex==123, False)
    testFalliti += testEqual(nemo, PescePagliaccio("Nemo", False, 0, "", ["Acqua"], "Salata"))
    testFalliti += testEqual(PescePagliaccio("Nemo", False, 0, "", ["Acqua"], "Salata")==nemo, True)
    testFalliti += testEqual(nemo==flounder, False)

    # test su __eq__ zoo
    print("==========> Test 7")
    testFalliti += testEqual(x==None, False)
    testFalliti += testEqual(Zoo()==Zoo(), True)
    a = Zoo()
    a.inserisci(alex, "A1")
    b = Zoo()
    b.inserisci(alex, "A1")
    testFalliti += testEqual(a==b, True)


    # test su zoo.animale e zoo.elimina
    print("==========> Test 8")
    testFalliti += testEqual(x.animale( "Alex"), alex)
    testFalliti += testEccezione(KeyError, x.animale, "Tizio")
    
    x.elimina("Anacleto")
    testFalliti +=testEccezione(KeyError, x.animale, "Anacleto")
    testFalliti += testEccezione(KeyError, x.elimina, "Anacleto")
    x.inserisci(anacleto, "A4")
    

    # test sulle zone
    print("==========> Test 9")
    testFalliti += testEqual(x.zona("Alex"), "A1")
    testFalliti += testEccezione(KeyError, x.zona, "Tizio")
    testFalliti += testEccezione(TypeError, x.cambia_zona, "Alex", 123)
    testFalliti += testEccezione(ValueError, x.cambia_zona, "Alex", "A")
    print("==========> Test 9.5")
    x.cambia_zona("Anacleto", "B2")
    testFalliti += testEqual(x.zona("Anacleto"), "B2")
    testFalliti += testEqual(sorted(x.zone()), sorted(["A1", "A2", "A3", "B2"]))
    testFalliti += testEqual(Zoo().zone(), [])

    # test su animali_zona e zone_animali
    print("==========> Test 10")
    testFalliti += testEqual(sorted(x.animali_zona("A1")), sorted(["Alex", "Melman", "Gloria"]))
    testFalliti += testEqual(Zoo().animali_zona("A2"), [])
    testFalliti += testEqual(x.zone_animali(), {'A1': ['Alex', 'Melman', 'Gloria'], 'A2': ['Skipper', 'Kowalski', 'Rico', 'Soldato'], 'A3': ['Flounder', 'Nemo'], 'B2': ['Anacleto']})
    testFalliti += testEqual(Zoo().zone_animali(), {})

    # test su animali_classe e animali_specie
    print("==========> Test 11")
    testFalliti += testEqual(x.animali_classe("Mammifero"), ['Alex', 'Melman', 'Gloria'])
    testFalliti += testEqual(Zoo().animali_classe("Uccello"), [])
    testFalliti += testEqual(sorted(x.animali_specie("Pinguino")), sorted(['Skipper', 'Kowalski', 'Rico', 'Soldato']))
    testFalliti += testEqual(Zoo().animali_specie("Pinguino"), [])

    # test su animali_ambiente
    print("==========> Test 12")
    testFalliti += testEqual(sorted(x.animali_ambiente("Acqua")), sorted(['Gloria', 'Skipper', 'Kowalski', 'Rico', 'Soldato', 'Flounder', 'Nemo']))
    testFalliti += testEqual(Zoo().animali_ambiente("Acqua"), [])

    #test animali zampe almeno
    print("==========> Test 13")
    testFalliti += testEqual(x.animali_con_zampe_almeno(4), ['Alex', 'Melman', 'Gloria'])
    testFalliti += testEqual(sorted(x.animali_con_zampe_almeno()), sorted(['Alex','Melman', 'Gloria', 'Skipper', 'Kowalski', 'Rico', 'Soldato', 'Anacleto']))
    testFalliti += testEqual(Zoo().animali_con_zampe_almeno(2), [])

    # test conta
    print("==========> Test 14")
    testFalliti += testEqual(x.conta_sangue(True), 8)
    testFalliti += testEqual(Zoo().conta_sangue(True), 0)
    testFalliti += testEqual(x.conta_classe("Mammifero"), 3)
    testFalliti += testEqual(Zoo().conta_classe("Mammifero"), 0)
    testFalliti += testEqual(x.conta_specie("Pinguino"), 4)
    testFalliti += testEqual(Zoo().conta_specie("Pinguino"), 0)

    #test finale su file e __str__ zoo
    print("==========> Test 15")
    x.salva("zoo.txt")
    y = Zoo()
    y.carica("zoo.txt")
    testFalliti += testEqual(x, y)


    testFalliti += testEqual(str(x), 
"""Zona A1: Il Leone (Mammifero) Alex ha 4 zampe, sangue caldo e vive in Terra facendo un Ruggito, con 7 settimane di gestazione
Zona A1: La Giraffa (Mammifero) Melman ha 4 zampe, sangue caldo e vive in Terra facendo un Mugugno, con 65 settimane di gestazione
Zona A1: L'Ippopotamo (Mammifero) Gloria ha 4 zampe, sangue caldo e vive in Terra e Acqua facendo un Ruggito, con 34 settimane di gestazione
Zona A2: Il Pinguino (Uccello) Skipper ha 2 zampe, sangue caldo e vive in Terra e Acqua facendo un Garrito, non sa volare
Zona A2: Il Pinguino (Uccello) Kowalski ha 2 zampe, sangue caldo e vive in Terra e Acqua facendo un Garrito, non sa volare
Zona A2: Il Pinguino (Uccello) Rico ha 2 zampe, sangue caldo e vive in Terra e Acqua facendo un Garrito, non sa volare
Zona A2: Il Pinguino (Uccello) Soldato ha 2 zampe, sangue caldo e vive in Terra e Acqua facendo un Garrito, non sa volare
Zona A3: Il PescePagliaccio (Pesce) Flounder è senza zampe, sangue freddo e vive in Acqua Salata
Zona A3: Il PescePagliaccio (Pesce) Nemo è senza zampe, sangue freddo e vive in Acqua Salata
Zona B2: Il Gufo (Uccello) Anacleto ha 2 zampe, sangue caldo e vive in Aria facendo un Bubbolio, sa volare""")

    #stampa finale zoo
    print("==========> Stampa finale zoo")
    print(x)
    print()

    # abbiamo finito ?
    if testFalliti == 0:
        print("\t****Test completati -- effettuare la consegna come da README")
    else:
        print("Test falliti: ",testFalliti)

# eseguo i test automatici
controllo()

