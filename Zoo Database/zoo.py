#========================================================================================================

#                Francesco Curia (692254) e Matilde Viti (603604)
#                     Programmazione e Analisi di Dati 24/25

#                   ASSEGNAMENTO 3 -- ZOO 2 (PYTHON AVANZATO)

#========================================================================================================

from animali import *

class Zoo:
    def __init__(self):
        self.zoo = {} # Dizionario per gestire gli animali, dove la chiave è il nome dell'animale e il valore è una tupla (oggetto animale, zona)

    # abbiamo creato questa funzione ausiliare che verifica la zona, usata in più funzioni 
    def _verifica_zona(self, zona):
    # la zona deve essere una stringa di due caratteri: il primo una lettera maiuscola, il secondo un numero 
    # la funzione isdigit() controlla se una stringa contiene numeri da 0 a 9, isupper() se la lettera è maiuscola
        if not isinstance(zona, str):
            raise TypeError("Errore! La zona è una stringa!")
            
        if len(zona) != 2 or not zona[0].isupper() or not zona[1].isdigit():
            raise ValueError("Errore! La zona è una stringa di due caratteri: una lettera maiuscola e un numero!")
        return True
    
    # abbiamo creato questa funzione che verifica il nome, usata in più funzioni
    def _verifica_nome(self, nome):
        if not isinstance(nome, str):
            raise TypeError("Errore! Il nome è una stringa!")   

        if nome.strip() == "": # per non accettare anche stringhe composte solo da spazi
            raise ValueError("Errore! La stringa non deve essere vuota!") 
        
        if nome.strip().capitalize() not in self.zoo: # poiché tutti i nomi sono salvati nel dizionario con la lettera maiuscola e senza spazi
            raise KeyError("Errore! Il nome non è presente nel dizionario!")
        return True


    def __str__(self):
        stringa = []
        for nome, (animale, zona) in self.zoo.items():
            stringa.append(f"Zona {zona}: {animale}")
        return "\n".join(stringa) # affinché le stringhe della lista vengano salvate come una intera con ritorni a capo
    
    # uguaglianza profonda tra due zoo
    def __eq__(self, altro_zoo):
        if not isinstance(altro_zoo, Zoo):
            return False
    
        if len(self.zoo) != len(altro_zoo.zoo):
            return False
        
        for nome, parametro in self.zoo.items():
            if nome not in altro_zoo.zoo:
                return False

            # confrontiamo le tuple
            # prendiamo gli elementi della tupla e li assegniamo a delle variabili che poi confrontiamo
            altro_animale, altra_zona = altro_zoo.zoo[nome]
            if parametro[0] != altro_animale or parametro[1] != altra_zona:
                return False
        return True            
    

    def inserisci(self, animale, zona):
        # la funzione accetta come oggetti solo "Animale" e le sue sottoclassi 
        if not isinstance(animale, Animale):
            raise TypeError("Errore! L'animale è un oggetto!")

        # verifica la zona con la funzione precedentemente spiegata
        self._verifica_zona(zona)

        if animale.get_nome() in self.zoo:
            raise KeyError("Errore! L'animale è già presente!")
        
        self.zoo[animale.get_nome()] = (animale, zona)
        return True


    def animale(self, nome):
        self._verifica_nome(nome) # verifica il nome con la funzione precedentemente spiegata
        nome_normalizzato = nome.strip().capitalize() # affinché la funzione sia case insensitive e tolga spazi
        return self.zoo[nome_normalizzato][0]


    def zona(self, nome):
        self._verifica_nome(nome)
        nome_normalizzato = nome.strip().capitalize() # affinché la funzione sia case insensitive e tolga spazi
        return self.zoo[nome_normalizzato][1] 


    def elimina(self, nome):
       self._verifica_nome(nome) # verifica il nome con la funzione precedentemente spiegata
       nome_normalizzato = nome.strip().capitalize() # affinché la funzione sia case insensitive e tolga spazi
       del self.zoo[nome_normalizzato] 
       return True


    def cambia_zona(self, nome, zona):
        # Cambia la zona di un animale specificato dal nome
        self._verifica_nome(nome)
        self._verifica_zona(zona)
        nome_normalizzato = nome.strip().capitalize()
        # poiché la tupla è immutabile, abbiamo effettuato una concatenazione con l'aggiunta della nuova zona
        self.zoo[nome_normalizzato] = self.zoo[nome_normalizzato][:1] + (zona,)
        return True       


    def zone(self):
        lista_zone = [] # Lista vuota per raccogliere tutte le zone dello zoo
        for valore in self.zoo.values():
            lista_zone.append(valore[1])
        # abbiamo convertito la lista in un set per eliminare i duplicati delle zone; abbiamo poi riconvertito il set in una lista affinché potessimo usare la funzione sorted() per ordinare i valori
        return sorted(list(set(lista_zone)))
    

    def animali_zona(self, zona):
        self._verifica_zona(zona) # verifica il nome con la funzione precedentemente spiegata
        lista_animali_zona = []
        for valore in self.zoo.values():
            if valore[1] == zona:
                lista_animali_zona.append(valore[0].get_nome())
        return lista_animali_zona # ritorna la lista degli animali della zona desiderata


    def zone_animali(self):
        # creiamo un dizionario per raggruppare gli animali per zona 
        dizionario_zone = {}
        for nome, parametro in self.zoo.items():
            # creiamo la lista per la zona se non è già presente
            if parametro[1] not in dizionario_zone: # parametro[1] corrisponde alla zona, se non presente viene inizializzata con una lista vuota
                dizionario_zone[parametro[1]] = []

            dizionario_zone[parametro[1]].append(parametro[0].get_nome())
        return dizionario_zone
    

    def animali_classe(self, classe):
        if not isinstance(classe, str):
            raise TypeError("Errore! La classe è una stringa!")
        
        classe_normalizzata = classe.strip().capitalize() # affinché la funzione sia case insensitive e tolga spazi

        lista_classi_valide = ["Mammifero", "Uccello", "Pesce"]
        if classe_normalizzata not in lista_classi_valide:
            raise ValueError("Errore! La classe è una tra 'Mammifero', 'Uccello' o 'Pesce'!")
        # crea una lista vuota per memorizzare i nomi degli animali che appartengono alla classe specificata
        lista_classe = []
        # abbiamo creato un dizionario con la stringa della classe come chiave e l'oggetto corrispondente come valore, in modo da utilizzare il parametro come accesso
        classi = {
                  "Mammifero": Mammifero,
                  "Uccello": Uccello,
                  "Pesce": Pesce
                  }
        # come detto prima, tramite la chiave "classe" verifichiamo se l'animale corrisponde all'oggetto desiderato
        for nome, parametro in self.zoo.items():
            if isinstance(parametro[0], classi[classe_normalizzata]):
                lista_classe.append(nome)
                    
        return lista_classe


    def animali_specie(self, specie):
        if not isinstance(specie, str):
            raise TypeError("Errore! La specie è una stringa!")
        
        specie_normalizzata = specie.strip().capitalize() # affinché la funzione sia case insensitive e tolga spazi
        # abbiamo creato una lista per contenere i nomi degli animali appartenenti alla specie specificata
        lista_specie = []
        # abbiamo creato un dizionario con la stringa della classe come chiave e l'oggetto corrispondente come valore, in modo da utilizzare il parametro come accesso
        specie_valide = {
                  "Leone": Leone,
                  "Giraffa": Giraffa,
                  "Ippopotamo": Ippopotamo,
                  "Zebra": Zebra,
                  "Gufo": Gufo,
                  "Pappagallo": Pappagallo,
                  "Pinguino": Pinguino,
                  "Pescepagliaccio": PescePagliaccio,
                  "Pescegatto": PesceGatto
                  }
        
        # come detto prima, tramite la chiave "specie" verifichiamo se l'animale corrisponde all'oggetto desiderato
        for nome, parametro in self.zoo.items():
            if isinstance(parametro[0], specie_valide[specie_normalizzata]):
                lista_specie.append(nome)
                    
        return lista_specie
    

    def animali_ambiente(self, ambiente):
        if not isinstance(ambiente, str):
            raise TypeError("Errore! L'ambiente è una stringa!")
        
        ambiente_normalizzato = ambiente.strip().capitalize() # affinché la funzione sia case insensitive e tolga spazi
        ambienti_validi = ["Terra", "Acqua", "Aria"]
        if ambiente_normalizzato not in ambienti_validi:
            raise ValueError("Errore! L'ambiente può essere solo Terra, Acqua o Aria!")
        
        lista_ambiente = [] # lista vuota che aggiungerà gli animali dell'ambiente desiderato
        for nome, parametro in self.zoo.items():
            animale = parametro[0]
            for elemento in animale.get_ambiente():
                if elemento == ambiente_normalizzato:
                    lista_ambiente.append(nome)

        return lista_ambiente


    def animali_con_zampe_almeno(self, numero_zampe = 2): # default 2
        if not isinstance(numero_zampe, int):
            raise TypeError("Errore! numero_zampe è un numero intero!")
        
        if numero_zampe < 0:
            raise ValueError("Errore! numero_zampe è un intero positivo!")
        
        lista_animali_zampe = []
        for nome, parametro in self.zoo.items():
            animale = parametro[0] 
            if animale.get_numero_zampe() >= numero_zampe: # controlliamo se il numero di zampe è almeno quello specificato o maggiore
                lista_animali_zampe.append(nome)
                
        return lista_animali_zampe
    

    def conta_sangue(self, sangue_caldo):
        if not isinstance(sangue_caldo, bool):
            raise TypeError("Errore! sangue_caldo è un valore booleano!")
        
        conto = 0 # variabile di accumulazione che incrementa di 1 per ogni animale trovato
        if sangue_caldo: # ovvero se il sangue è caldo
            for parametro in self.zoo.values():
                animale = parametro[0]
                if animale.get_sangue_caldo() == True: # True equivale al sangue caldo, quindi la variabile 'conto' incrementa seguendo questa condizione
                    conto += 1
            return conto
        elif not sangue_caldo: # ovvero se il sangue è freddo
            for parametro in self.zoo.values():
                animale = parametro[0]
                if animale.get_sangue_caldo() == False: # False equivale al sangue freddo, quindi la variabile 'conto' incrementa seguendo questa condizione
                    conto += 1 
            return conto
        

    def conta_classe(self, classe):
        # abbiamo usato la funzione animali_classe() e l'abbiamo inserita in una variabile alla quale abbiamo applicato la funzione len()
        lista_animali_classe = self.animali_classe(classe)
        if len(lista_animali_classe) > 0:
            return len(lista_animali_classe) 
        else:
            return 0


    def conta_specie(self, specie):
        # abbiamo usato la funzione animali_specie() e l'abbiamo inserita in una variabile alla quale abbiamo applicato la funzione len()
        lista_animali_specie = self.animali_specie(specie)
        if len(lista_animali_specie) > 0:
            return len(lista_animali_specie) 
        else:
            return 0


    def salva(self, nome_file):
        with open(nome_file, "w") as infile: # useremo "w" per scrivere sul file
            for nome, parametro in self.zoo.items():
                animale = parametro[0]
                zona = parametro[1]
                infile.write(animale.file_str() + ";" + zona + "\n") # salverà il file_str() dell'oggetto animale con l'aggiunta della zona
        

    def carica(self, nome_file):
        if not isinstance(nome_file, str):
            raise TypeError("Errore! nome_file è una stringa!")
  
        if not nome_file.endswith('.txt'):
            raise ValueError("Errore! Il file non è nel formato corretto. Deve essere un file .txt!")
  
        with open(nome_file) as infile: # non abbiamo specificato "r" perché già legge di default
            data = infile.readlines()
            for riga in data:
                riga = riga.strip()
                lista_animale = riga.split(";")

                if len(lista_animale) < 7:
                    raise ValueError(f"Formato riga non valido: {riga}")
    
                # Identifichiamo la classe dell'animale
                specie = lista_animale[0]
                nome = lista_animale[1]
                sangue_caldo = True if lista_animale[2] == "True" else False # Confronta il valore al terzo elemento della lista con la stringa "True": se il valore è "true", restituisce True, altrimenti False.
                numero_zampe = int(lista_animale[3]) # poiché un numero
                ambiente = lista_animale[4].split(" ") # poiché è una lista
                verso = lista_animale[5]
                zona = lista_animale[-1] # l'ultimo indice corrisponde alla zona
                
                # Creiamo l'istanza appropriata
                # Vediamo i Mammiferi
                if specie == "Leone":
                    gestazione = int(lista_animale[6])
                    animale = Leone(nome, sangue_caldo, numero_zampe, verso, ambiente, gestazione)

                elif specie == "Giraffa":
                    gestazione = int(lista_animale[6])
                    animale = Giraffa(nome, sangue_caldo, numero_zampe, verso, ambiente, gestazione)

                elif specie == "Ippopotamo":
                    gestazione = int(lista_animale[6])
                    animale = Ippopotamo(nome, sangue_caldo, numero_zampe, verso, ambiente, gestazione)

                elif specie == "Zebra":
                    gestazione = int(lista_animale[6])
                    animale = Zebra(nome, sangue_caldo, numero_zampe, verso, ambiente, gestazione)
                    
                # Passiamo agli Uccelli
                elif specie == "Pinguino":
                    volatile = True if lista_animale[6] == "True" else False
                    animale = Pinguino(nome, sangue_caldo, numero_zampe, verso, ambiente, volatile) 

                elif specie == "Gufo":
                    volatile = True if lista_animale[6] == "True" else False
                    animale = Gufo(nome, sangue_caldo, numero_zampe, verso, ambiente, volatile)  

                elif specie == "Pappagallo":
                    volatile = True if lista_animale[6] == "True" else False
                    animale = Pappagallo(nome, sangue_caldo, numero_zampe, verso, ambiente, volatile)            

                # Infine, i Pesci
                elif specie == "PescePagliaccio":
                    acqua = str(lista_animale[6])
                    animale = PescePagliaccio(nome, sangue_caldo, numero_zampe, "", ambiente, acqua)            
                    
                elif specie == "PesceGatto":
                    acqua = str(lista_animale[6])
                    animale = PesceGatto(nome, sangue_caldo, numero_zampe, "", ambiente, acqua)            
                
                else:
                    raise ValueError(f"Tipo di animale non riconosciuto: {specie}")
                
                # Aggiunge l'animale allo zoo
                self.inserisci(animale, zona)




