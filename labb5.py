import felhantering_labb5

class Person:
    def __init__(self, förnamn, efternamn, personnummer):
        """skapar en person med attributen för-, efternamn och personnr"""
        self.förnamn=förnamn
        self.efternamn=efternamn
        self.personnummer=personnummer

    def __str__(self):
        return "Namn: " + self.förnamn + " " + self.efternamn + " Personnummer: " + self.personnummer
    
class Student:
    def __init__(self):
        """skapar en tom lista där studenter läggs in"""
        self.student1=[]

    def __str__(self):  
        """skapar en mall för hur den ska printas"""
        studenten=""
        for student in self.student1:    #loopar funktionen för alla obejkt
            studenten+="Roll: Student "+str(student) +"\n"  #student ökar med detta för varje loop
        return studenten
        
    def lägg_till(self,i):
        """lägger till personer till listan"""
        print("Vad heter", str(i+1) + ":a studenten i förnamn? ", end="")    
        förnamn=input()     
        print("Vad heter",str(i+1) + ":a studenten i efternamn? ", end="")
        efternamn=input()
        print("Vad är", str(i+1) +  ":a studentens personnummer? ", end="")
        personnummer=felhantering_labb5.personnummer()  #felhanterar personnr
        ny_student=Person(förnamn, efternamn, personnummer) #använder person:s mall för hur en peson ska struktureras
        self.student1.append(ny_student)    #lägger till i listan
    
    def sök(self, sök):
        """söker efter personer och returnerar alla attribut"""
        for student in self.student1:
            if student.förnamn==sök:
                return student
    
    def radera(self, namn):
        """raderar ett objekt från listan genom att söka efter ett förnamn och sedan hitta dess index"""
        for i,o in enumerate(self.student1):  #taget från stack overflow 
            if o.förnamn==namn:
                del self.student1[i]
                for l in self.student1:
                    print(l, "\n")
            else:
                print("Det finns ingen med det namnet")
    
    def längd(self):
        """kontrollerar att listans längd är större än 0"""
        if len(self.student1)>0:
            for i in self.student1:
                return i, "\n"

class Lärare:
    """skapar en tom lista där lärare läggs in"""
    def __init__(self):
        self.lärare=[]

    def __str__(self):
        """skapar en mall för hur den ska printas"""
        läraren=""
        for lärare in self.lärare:   #loopar funktionen för alla obejkt
            läraren+="Roll: Lärare " +str(lärare) +"\n" #student ökar med detta för varje loop
        return läraren
        
    def lägg_till(self,i):
        """söker efter personer och returnerar alla attribut"""
        print("Vad heter", str(i+1) + ":a läraren i förnamn? ", end="")    
        förnamn=input()     
        print("Vad heter",str(i+1) + ":a läraren i efternamn? ", end="")
        efternamn=input()
        print("Vad är", str(i+1) +  ":a lärarens personnummer? ", end="")
        personnummer=felhantering_labb5.personnummer()  #felhanterar personnr
        ny_lärare=Person(förnamn, efternamn, personnummer)  #använder person:s mall för hur en peson ska struktureras
        self.lärare.append(ny_lärare)   #lägger till i listan

    def sök(self, sök):
        """söker efter personer och returnerar alla attribut"""
        for lärare in self.lärare:
            if lärare.förnamn==sök:
                return lärare
            
    def radera(self, namn):
        """raderar ett objekt från listan genom att söka efter ett förnamn och sedan hitta dess index"""
        for i,o in enumerate(self.lärare):  #taget från stack overflow 
            if o.förnamn==namn:
                del self.lärare[i]
                for l in self.lärare:
                    print(l, "\n")
            else:
                print("Det finns ingen med det namnet")

    def längd(self):
        """kontrollerar att listans längd är större än 0"""
        if len(self.lärare)>0:
            for l in self.lärare:
                return l, "\n"
    

def huvudfunktion():
    studenterna=Student()
    lärarna=Lärare()
    while True:
        print("Vill du:", "\n1. Sök ","\n2. Lägga till", "\n3. Ta bort", "\n4. Visa klasslistan", "\n5. Avsluta programmet", "\nSkriv position: ", end="")
        kommando=input()  #ger användaren en meny
        print()
        if kommando=="1":
            sök=input("Skriv förnamnet på den du söker: ")
            if lärarna.sök(sök)!=None:  #om funktionen inte returnar något
                print("Roll: Lärare",lärarna.sök(sök), "\n")
            if studenterna.sök(sök)!=None:  #om funktionen inte returnar något
                print("Roll: Student",studenterna.sök(sök), "\n")
            if lärarna.sök(sök)==None and studenterna.sök(sök)==None:   #om ingen av funktinerna returnar något
                print("Det finns ingen med det namnet\n")
        elif kommando=="2":
            roll=input("Är personen [1] lärare eller [2] student? ")
            if roll=="1": #elever
                print("Hur många elever vill du lägga till? ", end="")
                antal=felhantering_labb5.heltal()   #felhanterar antalet
                i=0
                while i<antal:  #loopar funktionen så att det läggs till rätt antal 
                    studenterna.lägg_till(i)
                    i+=1
                print("\nHär är de tillagda objekten: \n" + str(studenterna))
            if roll=="2":               
                print("Hur många lärare vill du lägga till? ", end="")
                antal_lä=felhantering_labb5.heltal()    #falhanterar antalet
                z=0
                while z<antal_lä:   #loopar funktionen så att det läggs till rätt antal 
                    lärarna.lägg_till(z)
                    z+=1
                print("\nHär är de tillagda objekten: \n" + str(lärarna))
            else:
                print("Du får endast skriva 1 eller 2 \n")
        elif kommando=="3":
            val=input("Vill du ta bort en [1]lärare eller [2]student? ")
            if val=="1":
                print(studenterna)
                namn=input("Skriv förnamnet på den du vill ta bort: ")
                studenterna.radera(namn)
            if val=="2":
                print(lärarna)
                namn=input("Skriv förnamnet på den du vill ta bort: ")
                lärarna.radera(namn)
            else:
                print("Du får bara skriva 1 eller 2\n")
        elif kommando=="4":
            if studenterna.längd()!=None:   #om funktionen returnar något
                print("Alla studenter:\n"+str(studenterna))
            if lärarna.längd()!=None:   #om funktionen returnar något
                print("Alla lärare:\n"+str(lärarna))
            if studenterna.längd()==None and lärarna.längd()==None: #om ingen av funktionerna returnar något
                print("Det finns ingen i listorna\n")
        elif kommando=="5": #avslutar loopen
            break
        else:
            print("Skriv 1-5\n")


huvudfunktion()