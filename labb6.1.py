import felhantering_labb6

class Person:
    def __init__(self, förnamn, efternamn, personnummer):
        """skapar en person med attributen för-, efternamn och personnr"""
        self.förnamn=förnamn
        self.efternamn=efternamn
        self.personnummer=personnummer

    def __str__(self):  
        """skapar en mall för hur attributen ska vara vara"""
        return "Namn: " + self.förnamn + " " + self.efternamn + " Personnummer: " + self.personnummer
    
class Lista:

    def __init__(self):
        self.studenter=[]
        

    def fil(self, filnamn):
        """öppnar filen och skapar en lista med klassens "Person" mall för objekten"""
        while True: #loopar tills användaren skriver in en fil som finns
            try:
                studentfil=open(filnamn, "r")   #avläser filen
                break
            except FileNotFoundError:   
                filnamn=input("Det finns ingen fil med det namnet, försök igen: ")
        personnummer=studentfil.readline().strip()  #läser en rad 
        while personnummer!="": #eftersom personnummer står först, loopar den tills personnummer inte är någonting, alltså listan är slut
            efternamn=studentfil.readline().strip()
            förnamn=studentfil.readline().strip()
            self.studenter.append(Person(förnamn, efternamn, personnummer))
            personnummer=studentfil.readline().strip()
        studentfil.close    #stänger filen
        return self.studenter    #returnar listan

    def spara(self, filnamn):
            """sparar alla ändringar till en fil"""
            studentfil=open(filnamn, "w")
            for s in self.studenter:      #loopar så prsonnr kommer först sedan byter rad 
                studentfil.write(s.personnummer + "\n")
                studentfil.write(s.efternamn + "\n")
                studentfil.write(s.förnamn + "\n")
            studentfil.close
            print("Uppgifterna sparade!\n")     #när loopen är klar printas detta

    def ändra(self):
            """ändrar för och efternamn för angivet personnr"""
            tal=input("Skriv personens personnummer: ")
            for s in self.studenter:
                if s.personnummer==tal: #om det finns ett personnummer som är sammma som input
                    gammalt_för=s.förnamn   #sparar gamla förnamnet i en variabel för att sedan printa vad det var och ändrades till
                    gammalt_efter=s.efternamn   #sparar gamla efternamnet i en variabel 
                    nytt_förnamn=input("Vad vill du ändra förnamnet till? ")       
                    nytt_efternamn=input("Vad vill du ändra efternamnet till? ")
                    s.förnamn=nytt_förnamn    #sätter studentens namn till det nya
                    s.efternamn=nytt_efternamn
                    print("Tidigare " + str(gammalt_för) +" "+ str(gammalt_efter) + ", med personnummer: " + str(s.personnummer) + ", har nu fått namnet", nytt_förnamn, nytt_efternamn)  
                    break   #bryter loopen när det är klart
            else:   #om det inte finns ett matchande personnummer 
                    print("Det finns ingen med det personnumret")
                    


    def lägga_till(self, antal):
        """lägger till angivet antal i listan"""
        i=0
        while i<antal:
            print("Vad heter", i+1, ":a personen i förnamn? ", end="")
            förnamn=input()
            print("Vad heter", i+1, ":a personen i efternamn ", end="")
            efternamn=input()
            print("Vad har", i+1, ":a personen för personnummer ", end="")
            personnummer=felhantering_labb6.personnummer()  #tilllåter användaren att bara skriva siffror i personner
            self.studenter.append(Person(förnamn, efternamn, personnummer))  #lägger till längst bak i listan enligt Person:s mall
            print("Det tillagda objektet:")
            print(self.studenter[-1], "\n")  #printar tillagda personen genom att hitta index längst bak i listan. 
            i+=1

    def sök(self):
        """söker efter ett matchande personnr och printar dess attribut"""
        sök=input("Skriv personens personnummer: ")
        for s in self.studenter:
            if s.personnummer==sök:  
                print(s, "\n")
                break
        else:
            print("Det finns ingen med det personnummret\n")

    def radera(self, personnr):
        """raderar en person från listan efter personnummer"""
        for i,o in enumerate(self.studenter):  #taget från stack overflow, håller koll på i och o s index
                if o.personnummer==personnr:
                    print("Är du säker på att du vill ta bort denna:\n" + str(o))   #printar personen med index o
                    svar=input("Skriv [ja] om du vill fortsätta\n")
                    if svar=="ja":
                        del self.studenter[i]    #raderar personen med index i
                        print("Personen har raderats. Här är den uppdaterade listan:")
                        for l in self.studenter:
                            print(l)
                        print()
                        break    
                    else:   #skriver inte personen ja avbryts det
                        print("Åtgärden avbröts\n")
                        break
        else:
            print("Det finns ingen med det personnummert\n")

    def huvudprogram(self):
        """geranvändaren en meny där de kan välja vad de vill göra"""
        filnamn=input("Skriv namnet på filen du vill öppna: ")
        self.fil(filnamn)
        while True:     #hela programet är i en loop 
            print("Vill du:", "\n1. Sök student","\n2. Lägga till", "\n3. Ändra studentern", "\n4. Visa studentern", "\n5. Ta bort studenter", "\n6. Spara och avsluta", "\nSkriv position: ", end="")
            kommando=input()     #ger användaren en meny
            print()

            if kommando=="1": #sök
                self.sök()

            elif kommando=="2": #lägg till
                print("Hur många vill du lägga till?", end=" ")
                antal=felhantering_labb6.heltal()   #felhanterar så att du bara kan lägga till ett helt antal personer
                self.lägga_till(antal)

            elif kommando=="3": #ändra student
                for s in self.studenter: #printar listan för att göra det lättare att se
                    print(s)
                self.ändra()
                print()

            elif kommando=="4": #visa alla
                print("Här är alla i klassen:\n")
                for s in self.studenter:
                    print(s)
                print()
                q=0
                while q==0: #för tydlighetens skull måste användaren trycka enter för att gå vidare
                    input("Tryck enter för att fortsätta") #input sätts inte som något värde utan blir bara ett steg för att q ska öka med 1
                    q+=1    #q ökar med 1 vilket gör att whileförhållandet inte gäller
                print()

            elif kommando=="5": #radera person
                personnr=input("Vad har personen för personnummer som du vill ta bort? ")
                self.radera(personnr)

            elif kommando=="6": #spara
                filnamn=input("Skriv filnamnet på filen du vill spara på: ")
                self.spara(filnamn)
                break   #avslutar huvudprogramet genom att breaka loopen
            else:
                print("Skriv 1-6\n")    

Lista().huvudprogram()
