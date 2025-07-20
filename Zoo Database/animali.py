#========================================================================================================

#                Francesco Curia (692254) e Matilde Viti (603604)
#                     Programmazione e Analisi di Dati 24/25

#                   ASSEGNAMENTO 3 -- ZOO 2 (PYTHON AVANZATO)

#========================================================================================================

class Animale:
    def __init__(self, nome, sangue_caldo, numero_zampe, verso, ambiente):
        if not isinstance(nome, str):
            raise TypeError("Errore! Il nome deve essere una stringa!")
        
        if nome.strip() == "": # affinché prenda in errore anche stringhe composte da soli spazi
            raise ValueError("Errore! Il nome deve essere una stringa non vuota!")
        
        self.nome = nome.strip().capitalize()  # il nome verrà salvato senza spazi e la prima lettera verrà resa maiuscola
        
        if isinstance(sangue_caldo, bool):
            self.sangue_caldo = sangue_caldo
        else:
            raise TypeError("Errore! sangue_caldo deve essere un valore booleano!")
        
        if not isinstance(numero_zampe, int):
            raise TypeError("Errore! numero_zampe è un intero!")
    
        if numero_zampe < 0:
            raise ValueError("Errore! numero_zampe deve essere positivo!")
        
        self.numero_zampe = numero_zampe
        
        if isinstance(verso, str):
            self.verso = verso.strip().capitalize()  # il verso verrà salvato senza spazi e la prima lettera verrà resa maiuscola
        else:
            raise TypeError("Errore! Il verso deve essere una stringa!")
        
        self._verifica_ambiente(ambiente) # rimanda alla funzione interna alla classe che verifica l'ambiente

    # abbiamo creato questa funzione perché la usiamo in diversi punti del programma, abbiamo messo un underscore perché la variabile è interna e di supporto
    def _verifica_ambiente(self, ambiente):
        ambienti_validi = ["Terra", "Acqua", "Aria"]
        if not isinstance(ambiente, list):
            raise TypeError("Errore! L'ambiente è una lista!")
        # Controlliamo che lista sia composta da almeno un elemento e max 3 elementi
        if len(ambiente) < 1 or len(ambiente) > 3:
            raise ValueError("Errore! La lista ambiente deve essere di min 1, max 3 elementi!")
        
        for elemento in ambiente:
            if not isinstance(elemento, str):
                raise TypeError("Gli ambienti sono stringhe!")
            
            if elemento not in ambienti_validi: # lista degli ambienti accettati
                raise ValueError("Gli ambienti possono essere Terra, Acqua o Aria, con la lettera maiuscola!")
            
        self.ambiente = ambiente


    # metodi getters
    def get_nome(self):
        return self.nome
    
    def get_sangue_caldo(self):
        return self.sangue_caldo
    
    def get_numero_zampe(self):
        return self.numero_zampe
    
    def get_verso(self):
        return self.verso
    
    def get_ambiente(self):
        return self.ambiente


    # metodi setters
    def set_nome(self, nome):
        if not isinstance(nome, str):
            raise TypeError("Errore! Il nome deve essere una stringa!")
        
        if nome.strip() == "":
            raise ValueError("Errore! Il nome deve essere una stringa non vuota!")
        
        self.nome = nome.strip().capitalize() # affinché il nome venga salvato nella classe con la lettera maiuscola e senza spazi


    def set_sangue_caldo(self, sangue_caldo):
        if isinstance(sangue_caldo, bool):
            self.sangue_caldo = sangue_caldo
        else:
            raise TypeError("Errore! sangue_caldo deve essere un valore booleano!")
        
        
    def set_numero_zampe(self, numero_zampe):
        if not isinstance(numero_zampe, int):
            raise TypeError("Errore! numero_zampe è un intero!")
    
        if numero_zampe < 0:
            raise ValueError("Errore! numero_zampe deve essere positivo!")
        
        self.numero_zampe = numero_zampe
        

    def set_verso(self, verso):
        if isinstance(verso, str):
            self.verso = verso.strip().capitalize()
        else:
            raise TypeError("Errore! Il verso deve essere una stringa non vuota!")
        

    def set_ambiente(self, ambiente):
        self._verifica_ambiente(ambiente) # come il costruttore, rimanda alla funzione interna che verifica l'ambiente

    # funzione __str__()
    def __str__(self):
        if self.verso: # per i Pesci, salva la stringa senza un verso in caso "self.verso" sia vuoto
            verso = f" facendo un {self.verso}" 
        else: 
            verso = "" 

        if self.numero_zampe == 0:
            zampe = "è senza zampe"
        else:
            zampe = f"ha {self.numero_zampe} zampe"

        if self.sangue_caldo: # True equivale a "sangue caldo" e False a "sangue freddo", essendo un booleano abbiamo risolto con una condizione  
            # il metodo .join() usato per unire due ambienti con "e", ad esempio con ["Acqua", "Terra"] -> Acqua e Terra 
            return f"{self.nome} {zampe}, sangue caldo e vive in {" e ".join(self.ambiente)}{verso}"
        else: 
            return f"{self.nome} {zampe}, sangue freddo e vive in {" e ".join(self.ambiente)}{verso}"   

    def __repr__(self): # per la rappresentazione non ambigua dell'oggetto
        return self.__str__()     

    # uguaglianza profonda    
    def __eq__(self, altro_animale):
        if isinstance(altro_animale, Animale):
            return (self.get_nome() == altro_animale.get_nome() and 
                self.get_sangue_caldo() == altro_animale.get_sangue_caldo() and 
                self.get_numero_zampe() == altro_animale.get_numero_zampe() and 
                self.get_verso() == altro_animale.get_verso() and
                self.get_ambiente() == altro_animale.get_ambiente())
                
        return False
    

####### Classi della classe Animale ########

class Mammifero(Animale):
    def __init__(self, nome, sangue_caldo, numero_zampe, verso, ambiente, settimane_gestazione):
        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente) # accede agli attributi della classe madre
        
        # Aggiungiamo validazioni specifiche per la classe Mammifero
        if not isinstance(settimane_gestazione, int):
            raise TypeError("Errore! settimane_gestazione è un intero!")
    
        if settimane_gestazione < 0:
            raise ValueError("Errore! settimane_gestazione deve essere positivo!")
        
        self.settimane_gestazione = settimane_gestazione
        
        if sangue_caldo == True:
            self.sangue_caldo = sangue_caldo
        else:
            raise ValueError("Errore! I mammiferi hanno il sangue caldo!")
        
        if numero_zampe <= 4:
            self.numero_zampe = numero_zampe
        else:
            raise ValueError("Errore! I mammiferi hanno massimo 4 zampe!")
        
    # metodo getter
    def get_settimane_gestazione(self):
        return self.settimane_gestazione
    
    # metodo setter
    def set_settimane_gestazione(self, settimane_gestazione):
        if not isinstance(settimane_gestazione, int):
            raise TypeError("Errore! settimane_gestazione è un intero!")
    
        if settimane_gestazione < 0:
            raise ValueError("Errore! settimane_gestazione deve essere positivo!")
        
        self.settimane_gestazione = settimane_gestazione
        

    # prendiamo il metodo __str__() della super classe
    def __str__(self):
            stringa_di_animale = super().__str__()
            return f"(Mammifero) {stringa_di_animale}, con {self.settimane_gestazione} settimane di gestazione"
    
    def __repr__(self): # rappresentazione non ambigua dell'oggetto
        return self.__str__() 

    # uguaglianza profonda
    def __eq__(self, altro_mammifero):
        if isinstance(altro_mammifero, Mammifero):
            if (super().__eq__(altro_mammifero) and
                self.get_settimane_gestazione() == altro_mammifero.get_settimane_gestazione()):
                return True
        return False
                


class Uccello(Animale):
    def __init__(self, nome, sangue_caldo, numero_zampe, verso, ambiente, volatile):
            super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente) 

            # Aggiungiamo validazioni specifiche per la classe Uccello
            if isinstance(volatile, bool):
                self.volatile = volatile
            else:
                raise TypeError("Errore! volatile deve essere un valore booleano!")
            
            if sangue_caldo == True:
                self.sangue_caldo = sangue_caldo
            else:
                raise ValueError("Errore! Gli uccelli hanno il sangue caldo!")
            
            if self.numero_zampe <= 2:
                self.numero_zampe = numero_zampe
            else:
                raise ValueError("Errore! Gli uccelli hanno massimo 2 zampe")
            
    # metodo getter
    def get_volatile(self):
        return self.volatile
    
    # metodo setter
    def set_volatile(self, volatile):
        if isinstance(volatile, bool):
            self.volatile = volatile
        else:
            raise TypeError("Errore! volatile deve essere un valore booleano!")
                   
    # prendiamo il metodo __str__ della super classe
    def __str__(self):
            stringa_di_animale = super().__str__()
            if self.volatile:
                volare = "sa volare"
            else:
                volare = "non sa volare"
            return f"(Uccello) {stringa_di_animale}, {volare}"
    
    def __repr__(self):
        return self.__str__()

    # uguaglianza profonda
    def __eq__(self, altro_uccello):
        if isinstance(altro_uccello, Uccello):
            if (super().__eq__(altro_uccello) and
                self.get_volatile() == altro_uccello.get_volatile()):
                return True
        return False
                


class Pesce(Animale):
    def __init__(self, nome, sangue_caldo, numero_zampe, verso, ambiente, acqua):
            super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente) # accede agli attributi della classe madre

            # Aggiungiamo validazioni specifiche per la classe Pesce
            if ambiente == ["Acqua"]:
                self.ambiente = ambiente
            else:
                raise ValueError("Errore! I pesci vivono solo in Acqua!")
            
            if numero_zampe == 0:
                self.numero_zampe = numero_zampe
            else:
                raise ValueError("Errore! I pesci non hanno zampe!")
            
            if sangue_caldo == False:
                self.sangue_caldo = sangue_caldo
            else:
                raise ValueError("Errore! I pesci hanno il sangue freddo!")        

            if verso == "":
                self.verso = verso
            else:
                raise ValueError("Errore! I pesci non fanno versi!")
            
            if not isinstance(acqua, str):
                raise TypeError("Errore! Acqua è una stringa!")
            
            if acqua.strip().capitalize() not in ["Dolce", "Salata"]:  # stessa procedura di verso e nome in Animale
                raise ValueError("Errore! Acqua deve essere una stringa tra 'Dolce' o 'Salata'!")
            
            self.acqua = acqua.strip().capitalize() # salva acqua con la lettera maiuscola e senza spazi
            
    # metodo getter
    def get_acqua(self):
        return self.acqua
    
    # metodo setter
    def set_acqua(self, acqua):
        if not isinstance(acqua, str):
            raise TypeError("Errore! Acqua è una stringa!")
            
        if acqua.strip().capitalize() not in ["Dolce", "Salata"]: # come nel costruttore di Pesce
            raise ValueError("Errore! Acqua deve essere una stringa tra 'Dolce' o 'Salata'!")
            
        self.acqua = acqua.strip().capitalize()
    
    
    # prendiamo il metodo __str__() della super classe
    def __str__(self):
            stringa_di_animale = super().__str__()
            return f"(Pesce) {stringa_di_animale} {self.acqua}"
    
    def __repr__(self):
        return self.__str__()

    # uguaglianza profonda
    def __eq__(self, altro_pesce):
        if isinstance(altro_pesce, Pesce):
            if (super().__eq__(altro_pesce) and
                self.get_acqua() == altro_pesce.get_acqua()):
                return True
        return False
                

#######Classi delle specie animali#########
# Classi bonus aggiunte: Zebra (mammifero), Pappagallo (uccello) e PesceGatto (pesce)    

# Sottoclassi della classe Mammifero                                                       

class Leone(Mammifero):
    # il costruttore prende anche valori di default e per "ambiente" (oggetto mutabile perché lista) abbiamo messo None dichiarato poi subito dopo
    def __init__(self, nome, sangue_caldo = True, numero_zampe = 4, verso = "Ruggito", ambiente = None, settimane_gestazione = 15):

        if ambiente == None:
            ambiente = ["Terra"]          

        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente, settimane_gestazione) # accede agli attributi della classe madre

        # Aggiungiamo validazioni specifiche per la classe Leone

        # abbiamo messo questa condizione perché le settimane di gestazione di un leone sono massimo 16 settimane
        if settimane_gestazione <= 16:
            self.settimane_gestazione = settimane_gestazione
        else:
            raise ValueError("Errore! I leoni hanno massimo 16 settimane di gestazione!")
        
        if ambiente == ["Terra"]:
            self.ambiente = ambiente
        else:
            raise ValueError("Errore! I leoni vivono solo in Terra!")
        

    def __str__(self):
        stringa_di_mammifero = super().__str__() # riprende il metodo della classe madre
        return f"Il Leone {stringa_di_mammifero}"
    
    def __repr__(self):
        return self.__str__()
    
    # uguaglianza profonda
    def __eq__(self, altro_leone):
        if isinstance(altro_leone, Leone):
            return super().__eq__(altro_leone)
        return False
    
    def file_str(self): # stringa da usare per i file
        return f"Leone;{self.nome};{self.sangue_caldo};{self.numero_zampe};{' '.join(self.ambiente)};{self.verso};{self.settimane_gestazione}"


class Giraffa(Mammifero):
    # il costruttore prende anche valori di default e per "ambiente" (oggetto mutabile perché lista) abbiamo messo None dichiarato poi subito dopo
    def __init__(self, nome, sangue_caldo = True, numero_zampe = 4, verso = "Mugolio", ambiente = None, settimane_gestazione = 60):
        
        if ambiente == None:
            ambiente = ["Terra"]
        
        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente, settimane_gestazione) # accede agli attributi della classe madre

        # Aggiungiamo validazioni specifiche per la classe Giraffa

        # abbiamo messo questa condizione perché le settimane di gestazione di una giraffa sono massimo 65 settimane
        if settimane_gestazione <= 65:
            self.settimane_gestazione = settimane_gestazione
        else:
            raise ValueError("Errore! Le giraffe hanno massimo 65 settimane di gestazione!")
        
        if ambiente == ["Terra"]:
            self.ambiente = ambiente
        else:
            raise ValueError("Errore! Le giraffe vivono solo in Terra!")
        
        
    def __str__(self):
        stringa_di_mammifero = super().__str__()
        return f"La Giraffa {stringa_di_mammifero}"
    
    def __repr__(self):
        return self.__str__()
    
    # uguaglianza profonda
    def __eq__(self, altra_giraffa):
        if isinstance(altra_giraffa, Giraffa):
            return super().__eq__(altra_giraffa)
        return False
    
    def file_str(self): # stringa da usare per i file
        return f"Giraffa;{self.nome};{self.sangue_caldo};{self.numero_zampe};{' '.join(self.ambiente)};{self.verso};{self.settimane_gestazione}"


class Ippopotamo(Mammifero):
    # il costruttore prende anche valori di default e per "ambiente" (oggetto mutabile perché lista) abbiamo messo None dichiarato poi subito dopo
    def __init__(self, nome, sangue_caldo = True, numero_zampe = 4, verso = "Grugnito", ambiente = None, settimane_gestazione = 35):
        
        if ambiente == None:
            ambiente = ["Terra", "Acqua"]

        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente, settimane_gestazione) # accede agli attributi della classe madre
        
        # Aggiungiamo validazioni specifiche per la classe Ippopotamo

        # abbiamo messo questa condizione perché le settimane di gestazione di un ippopotamo sono massimo 40 settimane
        if settimane_gestazione <= 40:
            self.settimane_gestazione = settimane_gestazione
        else:
            raise ValueError("Errore! Gli ippopotami hanno massimo 40 settimane di gestazione!")
        
        # abbiamo messo la funzione sorted() in modo che l'interprete accetti sia ["Terra, "Acqua"] sia ["Acqua", "Terra"] e li metta in ordine alfabetico
        # con il "reverse" attivato affinché nell'output venga salvato come ["Terra", "Acqua"], cioè alfabeticamente al contrario
        if sorted(ambiente, reverse=True) == ["Terra", "Acqua"]:
            self.ambiente = sorted(ambiente, reverse=True)
        else:
            raise ValueError("Errore! Gli ippopotami vivono in Terra e Acqua!")
        
        
    def __str__(self):
        stringa_di_mammifero = super().__str__()
        return f"L'Ippopotamo {stringa_di_mammifero}"
    
    def __repr__(self):
        return self.__str__()
    
    # uguaglianza profonda
    def __eq__(self, altro_ippopotamo):
        if isinstance(altro_ippopotamo, Ippopotamo):
            return super().__eq__(altro_ippopotamo)
        return False
    
    def file_str(self): # stringa per i file
        return f"Ippopotamo;{self.nome};{self.sangue_caldo};{self.numero_zampe};{' '.join(self.ambiente)};{self.verso};{self.settimane_gestazione}"
    

class Zebra(Mammifero):
    # il costruttore prende anche valori di default e per "ambiente" (oggetto mutabile perché lista) abbiamo messo None dichiarato poi subito dopo
    def __init__(self, nome, sangue_caldo = True, numero_zampe = 4, verso = "Nitrito", ambiente = None, settimane_gestazione = 48):

        if ambiente == None:
            ambiente = ["Terra"]
            
        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente, settimane_gestazione) # accede agli attributi della classe madre
        
        # Aggiungiamo validazioni specifiche per la classe Zebra

        # abbiamo messo questa condizione perché le settimane di gestazione di una zebra sono massimo 56 settimane
        if settimane_gestazione <= 56:
            self.settimane_gestazione = settimane_gestazione
        else:
            raise ValueError("Errore! Le zebre hanno massimo 56 settimane di gestazione!")
        
        if ambiente == ["Terra"]:
            self.ambiente = ambiente
        else:
            raise ValueError("Errore! Le zebre vivono solo in Terra!")
        

    def __str__(self):
        stringa_di_mammifero = super().__str__()
        return f"La Zebra {stringa_di_mammifero}"
    
    def __repr__(self):
        return self.__str__()
    
    # uguaglianza profonda
    def __eq__(self, altra_zebra):
        if isinstance(altra_zebra, Zebra):
            return super().__eq__(altra_zebra)
        return False
    
    def file_str(self): # stringa per i file
        return f"Zebra;{self.nome};{self.sangue_caldo};{self.numero_zampe};{' '.join(self.ambiente)};{self.verso};{self.settimane_gestazione}"


# Sottoclassi della classe Uccello

class Pinguino(Uccello):
    # il costruttore prende anche valori di default e per "ambiente" (oggetto mutabile perché lista) abbiamo messo None dichiarato poi subito dopo
    def __init__(self, nome, sangue_caldo = True, numero_zampe = 2, verso = "Garrito", ambiente = None, volatile = False):

        if ambiente == None:
            ambiente = ["Terra", "Acqua"]
        
        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente, volatile) # accede agli attributi della classe madre
        
        # Aggiungiamo validazioni specifiche per la classe Pinguino
        
        if volatile == False:
            self.volatile = volatile
        else:
            raise ValueError("Errore! Il pinguino non vola!")

        # abbiamo messo la funzione sorted() in modo che l'interprete accetti sia ["Terra, "Acqua"] sia ["Acqua", "Terra"] e li metta in ordine alfabetico
        # con il "reverse" attivato affinché nell'output venga salvato come ["Terra", "Acqua"], cioè alfabeticamente al contrario
        if sorted(ambiente, reverse=True) == ["Terra", "Acqua"]:
            self.ambiente = sorted(ambiente, reverse=True)
        else:
            raise ValueError("Errore! I pinguini vivono in Terra e Acqua!")
        

    def __str__(self):
        stringa_di_uccello = super().__str__() # accede al metodo della classe madre
        return f"Il Pinguino {stringa_di_uccello}"
    
    def __repr__(self):
        return self.__str__()

    # uguaglianza profonda
    def __eq__(self, altro_pinguino):
        if isinstance(altro_pinguino, Pinguino):
            return super().__eq__(altro_pinguino)
        return False
    
    def file_str(self): # stringa per i file
        return f"Pinguino;{self.nome};{self.sangue_caldo};{self.numero_zampe};{' '.join(self.ambiente)};{self.verso};{self.volatile}"


class Gufo(Uccello):
    # il costruttore prende anche valori di default e per "ambiente" (oggetto mutabile perché lista) abbiamo messo None dichiarato poi subito dopo
    def __init__(self, nome, sangue_caldo = True, numero_zampe = 2, verso = "Bubbolio", ambiente = None, volatile = True):
        
        if ambiente == None:
            ambiente = ["Aria"]

        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente, volatile) # accede agli attributi della classe madre
       
        # Aggiungiamo validazioni specifiche per la classe Gufo
        if volatile == True:
            self.volatile = volatile
        else:
            raise ValueError("Errore! Il gufo sa volare!")
        
        if ambiente == ["Aria"]:
            self.ambiente = ambiente
        else:
            raise ValueError("Errore! I gufi sono uccelli e quindi vivono in Aria!")
        

    def __str__(self):
        stringa_di_uccello = super().__str__()  # accede al metodo della classe madre
        return f"Il Gufo {stringa_di_uccello}"
    
    def __repr__(self):
        return self.__str__()
    
    # uguaglianza profonda
    def __eq__(self, altro_gufo):
        if isinstance(altro_gufo, Gufo):
            return super().__eq__(altro_gufo)
        return False
    
    def file_str(self): # stringa per i file
        return f"Gufo;{self.nome};{self.sangue_caldo};{self.numero_zampe};{' '.join(self.ambiente)};{self.verso};{self.volatile}"


class Pappagallo(Uccello):
    # il costruttore prende anche valori di default e per "ambiente" (oggetto mutabile perché lista) abbiamo messo None dichiarato poi subito dopo
    def __init__(self, nome, sangue_caldo = True, numero_zampe = 2, verso = "Garrito", ambiente = None, volatile = True):
        
        if ambiente == None:
            ambiente = ["Aria"]

        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente, volatile) # accede agli attributi della classe madre
        
        # Aggiungiamo validazioni specifiche per la classe Pappagallo
        if volatile == True:
            self.volatile = volatile
        else:
            raise ValueError("Errore! Il pappagallo sa volare!")
        
        if ambiente == ["Aria"]:
            self.ambiente = ambiente
        else:
            raise ValueError("Errore! I pappagalli sono uccelli e quindi vivono in Aria!")
        

    def __str__(self):
        stringa_di_uccello = super().__str__()  # accede al metodo della classe madre
        return f"Il Pappagallo {stringa_di_uccello}"
    
    def __repr__(self):
        return self.__str__()
    
    # uguaglianza profonda
    def __eq__(self, altro_pappagallo):
        if isinstance(altro_pappagallo, Pappagallo):
            return super().__eq__(altro_pappagallo)
        return False
    
    def file_str(self): # stringa per i file
        return f"Pappagallo;{self.nome};{self.sangue_caldo};{self.numero_zampe};{' '.join(self.ambiente)};{self.verso};{self.volatile}"


# Sottoclassi della classe Pesce

class PescePagliaccio(Pesce):
    # il costruttore prende anche valori di default e per "ambiente" (oggetto mutabile perché lista) abbiamo messo None dichiarato poi subito dopo
    def __init__(self, nome, sangue_caldo = False, numero_zampe = 0, verso = "", ambiente = None, acqua = "Salata"):
        if ambiente == None:
            ambiente = ["Acqua"]

        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente, acqua)  # accede agli attributi della classe madre 
        
        # Aggiungiamo validazioni specifiche per la classe PescePagliaccio
        if acqua.strip().capitalize() == "Salata":
            self.acqua = acqua.strip().capitalize() # come per la classe madre, salva acqua con la lettera maiuscola e senza spazi
        else:
            raise ValueError("Errore! Il PescePagliaccio vive in Acqua Salata!")
        
        
    def __str__(self):      # accede al metodo della classe madre
        stringa_di_pesce = super().__str__()
        return f"Il PescePagliaccio {stringa_di_pesce}"
    
    def __repr__(self):
        return self.__str__()
    
    # uguaglianza profonda
    def __eq__(self, altro_pesce_pagliaccio):
        if isinstance(altro_pesce_pagliaccio, PescePagliaccio):
            return super().__eq__(altro_pesce_pagliaccio)
        return False
    
    def file_str(self): # stringa per i file
        return f"PescePagliaccio;{self.nome};{self.sangue_caldo};{self.numero_zampe};{' '.join(self.ambiente)};{None};{self.acqua}"


class PesceGatto(Pesce):
    # il costruttore prende anche valori di default e per "ambiente" (oggetto mutabile perché lista) abbiamo messo None dichiarato poi subito dopo
    def __init__(self, nome, sangue_caldo = False, numero_zampe = 0, verso = "", ambiente = None, acqua = "Dolce"):
        if ambiente == None:
            ambiente = ["Acqua"]

        super().__init__(nome, sangue_caldo, numero_zampe, verso, ambiente, acqua)    # accede agli attributi della classe madre
        
        # Aggiungiamo validazioni specifiche per la classe PesceGatto
        if acqua.strip().capitalize() == "Dolce":
            self.acqua = acqua.strip().capitalize() # come per la classe madre, salva acqua con la lettera maiuscola e senza spazi
        else:
            raise ValueError("Errore! Il PesceGatto vive in Acqua Dolce!")
        
        
    def __str__(self):
        stringa_di_pesce = super().__str__()        # accede al metodo della classe madre
        return f"Il PesceGatto {stringa_di_pesce}"
    
    def __repr__(self):
        return self.__str__()
    
    # uguaglianza profonda
    def __eq__(self, altro_pesce_gatto):
        if isinstance(altro_pesce_gatto, PesceGatto):
            return super().__eq__(altro_pesce_gatto)
        return False
    
    def file_str(self):     # stringa da usare per i file
        return f"PesceGatto;{self.nome};{self.sangue_caldo};{self.numero_zampe};{' '.join(self.ambiente)};{None};{self.acqua}"

