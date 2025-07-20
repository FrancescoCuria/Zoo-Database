#========================================================================================================

#                Francesco Curia (692254) e Matilde Viti (603604)
#                     Programmazione e Analisi di Dati 24/25

#                   ASSEGNAMENTO 3 -- ZOO 2 (PYTHON AVANZATO)

#========================================================================================================


from zoo import *
from animali import *
import tkinter as tk
from tkinter import messagebox, simpledialog # abbiamo importato simpledialog e messagebox per rendere più economico il codice


class myApp:
    # costruttore
    def __init__(self, root):
        self.root = root # finestra principale dell'applicazione
        self.zoo = Zoo() # creiamo un'istanza di Zoo per gestire gli animali
        self.root.title("Archivio Zoo")
        self.file = "zoo.txt"
        self.root.geometry("1000x720") # impostiamo le dimensioni iniziali della finestra
        self.root.minsize(600, 300) # minsize specifica la dimensione più piccola consentita
        self.root.maxsize(1000, 1000) # maxsize imposta il limite massimo


        # abbiamo creato una listbox per visualizzare la lista degli animali
        self.box_animali = tk.Listbox(self.root, width = 162)
        self.box_animali.grid(row = 0, column = 0, columnspan = 6, padx = 10, pady = 10, sticky = "nsew") # con sticky = "nsew" facciamo in modo che il widget occupi tutto il frame

        # frame che contiene i bottoni
        self.contenitore_bottoni = tk.Frame(self.root, relief = tk.RAISED, borderwidth = 1) # tk.RAISED dà un effetto 3D
        self.contenitore_bottoni.grid(row = 1, column = 0, columnspan = 6, padx = 10, pady = 10, sticky = "nsew") 

        # bottoni associati alle funzioni
        self.bottone_informazioni = tk.Button(self.contenitore_bottoni, text = "Informazioni utili 🐧❓", background = "#FFFACD", font = ("Comic Sans MS", 11, "bold"))
        self.bottone_informazioni.pack(fill = tk.X, pady = 5) 
        self.bottone_informazioni.bind("<Button-1>", self.informazioni)
    
        self.bottone_inserisci_animale = tk.Button(self.contenitore_bottoni, text = "Inserisci animale 🐬", background = "#FFB6C1", font = ("Comic Sans MS", 11, "bold"))
        self.bottone_inserisci_animale.pack(fill = tk.X, pady = 5)
        self.bottone_inserisci_animale.bind("<Button-1>", self.inserisci_animale)
        
        self.bottone_mostra_animale = tk.Button(self.contenitore_bottoni, text = "Mostra animale 🐰", background = "#E6E6FA", font = ("Comic Sans MS", 11, "bold"))
        self.bottone_mostra_animale.pack(fill = tk.X, pady = 5)
        self.bottone_mostra_animale.bind("<Button-1>", self.mostra_animale)

        self.bottone_modifica_zona = tk.Button(self.contenitore_bottoni, text = "Modifica la zona di un animale 🐦", background = "#ADD8E6", font = ("Comic Sans MS", 11, "bold"))
        self.bottone_modifica_zona.pack(fill = tk.X, pady = 5)
        self.bottone_modifica_zona.bind("<Button-1>", self.modifica_zona)

        self.bottone_elimina_animale = tk.Button(self.contenitore_bottoni, text = "Elimina animale 🐨", background = "#C1E1C1", font = ("Comic Sans MS", 11, "bold"))
        self.bottone_elimina_animale.pack(fill = tk.X, pady = 5)
        self.bottone_elimina_animale.bind("<Button-1>", self.elimina_animale)

        self.bottone_lista_specie = tk.Button(self.contenitore_bottoni, text = "Lista animali per specie 🦋", background = "#B2F5E9", font = ("Comic Sans MS", 11, "bold"))
        self.bottone_lista_specie.pack(fill = tk.X, pady = 5)
        self.bottone_lista_specie.bind("<Button-1>", self.lista_specie)

        self.bottone_lista_ambiente = tk.Button(self.contenitore_bottoni, text = "Lista animali per ambiente 🐶", background = "#FFDAB9", font = ("Comic Sans MS", 11, "bold"))
        self.bottone_lista_ambiente.pack(fill = tk.X, pady = 5)
        self.bottone_lista_ambiente.bind("<Button-1>", self.lista_ambiente)

        self.bottone_numero_classe = tk.Button(self.contenitore_bottoni, text = "Numero animali per classe 🐖", background = "#FAFAD2", font = ("Comic Sans MS", 11, "bold"))
        self.bottone_numero_classe.pack(fill = tk.X, pady = 5)
        self.bottone_numero_classe.bind("<Button-1>", self.numero_classe)

        self.bottone_salva_file = tk.Button(self.contenitore_bottoni, text = "Salva su file (.txt) 🐸", background = "#FFB6C1", font = ("Comic Sans MS", 11, "bold"))
        self.bottone_salva_file.pack(fill = tk.X, pady = 5)
        self.bottone_salva_file.bind("<Button-1>", self.salva_file)

        self.bottone_carica_file = tk.Button(self.contenitore_bottoni, text = "Carica da file (.txt) 🐟", background = "#D7BDE2", font = ("Comic Sans MS", 11, "bold"))
        self.bottone_carica_file.pack(fill = tk.X, pady = 5)
        self.bottone_carica_file.bind("<Button-1>", self.carica_file)

        self.bottone_esci = tk.Button(self.contenitore_bottoni, text = "Esci 🐘", bg = "#A7C7E7", font = ("Comic Sans MS", 11, "bold"))
        self.bottone_esci.pack(fill = tk.X, pady = 5)
        self.bottone_esci.bind("<Button-1>", self.esci)



   # metodo che serve a ricaricare il box animali ogni qual volta si effettua un'operazione sull'archivio
    def aggiorna_archivio(self):
        self.box_animali.delete(0, tk.END) # svuota l'archivio zoo
        zoo_splitted = self.zoo.__str__().split("\n")
        for animale in zoo_splitted:
            self.box_animali.insert(tk.END, animale)
    
    # abbiamo creato una funzione bonus per aprire una finestra con le istruzioni per l'utilizzo dell'app, cliccabile dal bottone "informazioni utili"
    def informazioni(self,evento):
        informazioni = """
        Benvenuto nell'Archivio Zoo! 🐾

        Ecco le istruzioni per l'utilizzo:
        
        1. Inserimento animale:
            - Animali accettati: Leone, Zebra, Giraffa, Ippopotamo, Gufo, Pinguino, Pappagallo, PescePagliaccio, PesceGatto.
            - Nome: Inserire un nome valido per l'animale (non vuoto).
            - Sangue caldo: Specificare "Sì" (es. per i Mammiferi) o "No" (es. per i Pesci).
            - Numero zampe: Inserire un numero intero.
            - Verso: Inserire il verso dell'animale. Per i Pesci, scrivere "Nessuno".
            - Ambiente: Indicare gli ambienti naturali ("Terra, Acqua, Aria"), in maiuscolo e separati da virgola e spazio.
            - Zona: Inserire una zona valida, composta da lettera maiuscola e numero (es. "A1", "B3").
            PARAMETRI EXTRA:
            - Settimane gestazione (solo per Mammiferi): Inserire un numero intero.
            - Volatile (solo per Uccelli): Specificare "Sì" o "No" (es. Pinguino = No, Gufo = Sì).
            - Acqua (solo per Pesci): Inserire una stringa fra "Dolce" per il PesceGatto e "Salata" per il PescePagliaccio.
            
        2. Modifica zona:
            - Inserire il nome dell'animale esistente e la nuova zona.

        3. Eliminazione animale:
            - Inserire il nome dell'animale che si desidera eliminare.

        4. Lista animali:
            - Puoi visualizzare i nomi degli animali per specie e ambiente o il numero di animali per classe.
        
        5. Salvataggio e caricamento:
            - Salva l'archivio in un file .txt o caricalo.

        6. Errori comuni:
            - Inserire solo dati validi e non lasciare campi vuoti.
            - Assicurati di utilizzare nomi e zone già presenti per modifiche o eliminazioni.

        🐾 Buon lavoro con il tuo archivio zoo!
        """
        messagebox.showinfo("Informazioni utili", informazioni)


    # I metodi della gui effettuano un richiamo ai metodi delle classi degli animali e dello Zoo contenute in animali.py e zoo.py
    
    def inserisci_animale(self, evento):
        while True:
            animale_utente = simpledialog.askstring("Scelta animale", "Che animale vuoi inserire?:\nAnimali accettati: Leone, Zebra, Giraffa, Ippopotamo, Gufo, Pinguino, Pappagallo, PescePagliaccio, PesceGatto")
            animale_normalizzato = animale_utente.strip().capitalize() # normalizziamo l'animale scelto

            if animale_normalizzato == "":
                messagebox.showwarning("Inserimento annullato", "Inserimento annullato o stringa vuota da parte dell'utente.")
                break # esco dal loop se l'utente annulla l'operazione o la stringa è vuota

            animali_validi = ["Leone", "Zebra", "Giraffa", "Ippopotamo", "Gufo", "Pinguino", "Pappagallo", "Pescepagliaccio", "Pescegatto"]

            if animale_normalizzato not in animali_validi:
                messagebox.showerror("Inserimento errato", "L'animale scelto deve essere uno tra gli animali proposti!")
                break

            try: # usiamo un try-except per tutti i parametri degli animali
                nome = simpledialog.askstring("Inserimento nome", "Inserisci il nome dell'animale:")
                if nome.strip() == "":
                    messagebox.showwarning("Inserimento annullato", "Inserimento annullato o stringa vuota da parte dell'utente.")
                    break
                
                # trattandosi di un booleano, abbiamo usato il metodo .askquestion()
                sangue_caldo = messagebox.askquestion("Conferma", "L'animale ha sangue 'caldo'?")
                sangue_caldo = True if sangue_caldo == "yes" else False

                numero_zampe = simpledialog.askinteger("Inserimento zampe animale", "Quante zampe ha l'animale?")
                if numero_zampe is None:
                    messagebox.showwarning("Inserimento annullato", "Inserimento annullato da parte dell'utente.")
                    break
                
                verso = simpledialog.askstring("Inserimento verso", "Inserisci il verso dell'animale:\nSe inserisci un Pesce, scrivi 'Nessuno'.")
                if verso.strip() == "":
                    messagebox.showwarning("Inserimento annullato", "Inserimento annullato o stringa vuota da parte dell'utente.")
                    break                

                ambiente = simpledialog.askstring("Inserimento ambiente", "Inserisci gli ambienti naturali dell'animale (con la prima lettera maiuscola e separati da virgola e spazio):\nAmbienti accettati: Terra, Acqua, Aria.")
                lista_ambiente = ambiente.split(", ")
                if ambiente.strip() == "":
                    messagebox.showwarning("Inserimento annullato", "Inserimento annullato o stringa vuota da parte dell'utente.")
                    break                  
                
                if animale_normalizzato in animali_validi[:4]: # abbiamo fatto lo slicing della lista animali_validi: i primi 4 animali infatti sono Mammiferi e hanno l'attributo settimane_gestazione
                    settimane_gestazione = simpledialog.askinteger("Inserimento numero settimane gestazione animale", "Quante settimane di gestazione ha l'animale?")
                    if settimane_gestazione is None:
                        messagebox.showwarning("Inserimento annullato", "Inserimento annullato da parte dell'utente.")
                        break

                    # creiamo il MAMMIFERO desiderato
                    if animale_normalizzato == "Leone":
                        animale = Leone(nome, sangue_caldo, numero_zampe, verso, lista_ambiente, settimane_gestazione)
                    elif animale_normalizzato == "Giraffa":
                        animale = Giraffa(nome, sangue_caldo, numero_zampe, verso, lista_ambiente, settimane_gestazione)
                    elif animale_normalizzato == "Ippopotamo":
                        animale = Ippopotamo(nome, sangue_caldo, numero_zampe, verso, lista_ambiente, settimane_gestazione)
                    else:
                        animale = Zebra(nome, sangue_caldo, numero_zampe, verso, lista_ambiente, settimane_gestazione)
                
                if animale_normalizzato in animali_validi[4:7]: # abbiamo fatto lo slicing per verificare gli Uccelli
                    # trattandosi di un booleano, abbiamo usato il metodo .askquestion()
                    volatile = messagebox.askquestion("Conferma", "L'animale è un volatile?")
                    volatile = True if volatile == "yes" else False

                    # creiamo l'UCCELLO desiderato
                    if animale_normalizzato == "Gufo":
                        animale = Gufo(nome, sangue_caldo, numero_zampe, verso, lista_ambiente, volatile)
                    elif animale_normalizzato == "Pinguino":
                        animale = Pinguino(nome, sangue_caldo, numero_zampe, verso, lista_ambiente, volatile)
                    else:
                        animale = Pappagallo(nome, sangue_caldo, numero_zampe, verso, lista_ambiente, volatile)

                
                if animale_normalizzato in animali_validi[7:]: # abbiamo fatto lo slicing per verificare i Pesci
                    verso = ""
                    acqua = simpledialog.askstring("Inserimento verso", "Inserisci il tipo di acqua:\nScrivi un'opzione tra 'Dolce' o 'Salata'.")
                    if acqua.strip() == "":
                        messagebox.showwarning("Inserimento annullato", "Inserimento annullato o stringa vuota da parte dell'utente.")
                        break                
                
                     # creiamo il PESCE desiderato
                    if animale_normalizzato == "Pescepagliaccio":
                        animale = PescePagliaccio(nome, sangue_caldo, numero_zampe, verso, lista_ambiente, acqua)
                    else:
                        animale = PesceGatto(nome, sangue_caldo, numero_zampe, verso, lista_ambiente, acqua)

                zona = simpledialog.askstring("Inserimento zona", "Inserisci la zona dell'animale, composta da una lettera maiuscola e un numero.\nEs. 'A1', 'F5', ecc.")
                if zona.strip() == "":
                    messagebox.showwarning("Inserimento annullato", "Inserimento annullato o stringa vuota da parte dell'utente.")
                    break                
                
                if self.zoo.inserisci(animale, zona) == True:
                    self.box_animali.insert(tk.END, f"Zona {zona}: {animale}") # tk.END assicura che ogni stringa venga salvata sotto le altre
                    messagebox.showinfo("Inserimento avvenuto con successo", f"L'animale {animale.get_nome()} è stato aggiunto nella zona {zona}.")
                    break  # esco dal loop se l'inserimento è avvenuto con successo
                else:
                    messagebox.showerror("Inserimento annullato", "Non è stato possibile inserire l'animale.\nRiprova.")
            except (ValueError,TypeError, KeyError) as e:
                    messagebox.showerror("Inserimento errato", f"Non è stato possibile inserire l'animale.\n{e}")
                    break # esce dal loop
               
    
    # mostra la stringa di un animale dato il nome
    def mostra_animale(self, evento):
        nome = simpledialog.askstring("Mostra animale", "Inserisci il nome dell'animale da mostrare:")
        try:
            messagebox.showinfo("Ecco l'animale!", self.zoo.animale(nome))
        except (ValueError, TypeError, KeyError) as e:
            messagebox.showerror("Inserimento errato", f"Non è stato possibile mostrare l'animale.\n{e}")
      
      
    # permette di modificare la zona associata ad un animale esistente
    def modifica_zona(self, evento):
        nome = simpledialog.askstring("Inserimento animale", "Inserisci il nome dell'animale a cui modificare la zona:")
        zona = simpledialog.askstring("Inserimento zona", "Inserisci la nuova zona dell'animale che vuoi modificare:")
        try:
            self.zoo.cambia_zona(nome, zona)
            self.aggiorna_archivio() # aggiorniamo l'archivio con la nuova zona
            messagebox.showinfo("Modifica zona", "La zona dell'animale selezionato è stata modificata!")
        except (ValueError, TypeError, KeyError) as e:
            messagebox.showerror("Inserimento errato", f"Non è stato possibile mostrare l'animale.\n{e}")


    # abbiamo aggiunto questa funzione per completezza
    def elimina_animale(self, evento):
        nome = simpledialog.askstring("Rimozione animale", "Inserisci il nome dell'animale che vuoi eliminare dall'archivio:")
        try:
            self.zoo.elimina(nome)
            self.aggiorna_archivio() # aggiorniamo l'archivio dopo aver eliminato l'animale 
            messagebox.showinfo("Rimozione animale", "L'animale è stato eliminato con successo!")
        except (ValueError, TypeError, KeyError) as e:
            messagebox.showerror("Inserimento errato", f"Non è stato possibile eliminare l'animale.\n{e}")


    def lista_specie(self, evento):
        specie = simpledialog.askstring("Inserimento specie", "Inserisci la specie degli animali desiderati:\nSpecie valide: Leone, Zebra, Giraffa, Ippopotamo, Gufo, Pinguino, Pappagallo, PescePagliaccio, PesceGatto.")
        try:
            if len(self.zoo.animali_specie(specie)) > 0: # se non ci sono animali appare un warning
                messagebox.showinfo("Ecco gli animali della specie selezionata!", ", ".join(self.zoo.animali_specie(specie)))
            else:
                messagebox.showwarning("Avviso!", "Non sono presenti animali della specie selezionata.")
        except (ValueError, TypeError, KeyError) as e:
            messagebox.showerror("Inserimento errato", f"Non è stato possibile mostrare gli animali della specie selezionata.\n{e}")


    def lista_ambiente(self, evento):
        ambiente = simpledialog.askstring("Inserimento ambiente", "Inserisci l'ambiente degli animali desiderati:\nAmbienti validi: Terra, Acqua e Aria.")
        try:
            if len(self.zoo.animali_ambiente(ambiente)) > 0: # se non ci sono animali appare un warning
                messagebox.showinfo("Ecco gli animali dell'ambiente selezionato!", ", ".join(self.zoo.animali_ambiente(ambiente)))
            else:
                messagebox.showwarning("Avviso!", "Non sono presenti animali dell'ambiente selezionato.")
        except (ValueError, TypeError, KeyError) as e:
            messagebox.showerror("Inserimento errato", f"Non è stato possibile mostrare gli animali dell'ambiente selezionato.\n{e}")

            
    def numero_classe(self, evento):
        classe = simpledialog.askstring("Inserimento classe", "Inserisci la classe degli animali desiderati:\nClassi valide: Mammifero, Uccello e Pesce.")
        try:
            messagebox.showinfo("Ecco il numero degli animali della classe selezionata!", f"Totale animali della classe selezionata: {self.zoo.conta_classe(classe)}")
        except (ValueError, TypeError, KeyError) as e:
            messagebox.showerror("Inserimento errato", f"Non è stato possibile mostrare la quantità degli animali della classe selezionata.\n{e}")

    
    def salva_file(self, evento): # per salvare i dati dell'archivio zoo su un file
        nome_file = simpledialog.askstring("Salva file", "Inserisci il nome del file:\nSi consiglia di utilizzare il formato .txt!")
        try:
            self.zoo.salva(nome_file)
            messagebox.showinfo("Salvataggio file", f"Il file è stato creato con successo!")
        except Exception as e:
            messagebox.showerror("Salvataggio non andato a buon fine", f"Non è stato possibile salvare il file. Riprovare, per favore!")


    def carica_file(self, evento): # per caricare un file sull'archivio
        nome_file = simpledialog.askstring("Carica file", "Inserisci il nome del file:\nDeve essere in formato .txt!")
        try:
            self.zoo.carica(nome_file)
            self.aggiorna_archivio() # aggiorna l'archivio con i dati del file caricato
            messagebox.showinfo("Caricamento file", f"Il file è stato caricato con successo!")
        except (ValueError, TypeError, FileNotFoundError) as e:
            messagebox.showerror("Caricamento non andato a buon fine", f"Non è stato possibile caricare il file. Riprovare, per favore!")


    def esci(self, evento): # chiudiamo l'applicazione
        self.root.destroy()
    
            
root = tk.Tk()
app = myApp(root)
root.mainloop()

