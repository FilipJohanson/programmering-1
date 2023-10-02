class Student:
    """skapar en klass med attributen för- och efternamn och personnr"""
    def __init__(self, förnamn,efternamn, personnummer):
        self.förnamn=förnamn
        self.efternamn=efternamn
        self.personnummer=personnummer
    def __str__(self):
        """funktionen ger tillbaka attributen i en tydlig struktur"""
        return "Namn: " + self.förnamn + " " + self.efternamn + " Personnummer: " + self.personnummer   

def huvudprogram():
    """skapar en lista som den kan lägga och redigera i"""
    klasslista=[]   #skarpar en tom lista utanför loopen så att datan inte raderas varje varv
    while True:     #hela programet är i en loop 
        print("Vill du:", "\n1. Ändra klasslistan","\n2. Lägga till", "\n3. Ta bort studenter?", "\n4. Visa klasslistan", "\n5. Avsluta programmet", "\nSkriv position: ", end="")
        kommando=int(input())   #ger användaren en meny
        print()

        if kommando==1:     #om användaren väljer alt 1
            pos=1   #första namnet har plats 1
            for s in klasslista:    #printar ut den existerande klasslistan med dess position framför
                print(pos, ": ", end="")
                print(s)
                pos+=1      #gör att positionen ökar med 1
            tal=input("Skriv personnummer på personen du vill ändra: ")
            for student in klasslista:  #för varje objekt i listan 
                if student.personnummer==tal:   #om tal är samma som någon students personnr 
                    nytt_förnamn=input("Vad vill du ändra förnamnet till? ")
                    nytt_efternamn=input("Vad vill du ändra efternamnet till? ")
                    student.förnamn=nytt_förnamn    #sätter studentens namn till det nya
                    student.efternamn=nytt_efternamn
                    print("Här är den uppdaterade listan:")
                    for student in klasslista:  #printar den uppdaterade listan
                        print(student)
                elif student.personnummer!=tal:     #om ta inte är sammma som någons students personnr börjas huvudloopen om 
                    print("Det finns ingen med det personnummret")
            print()

        elif kommando==2:    #om användaren väljer alt 2
            antal=int(input("Hur många vill du lägga till? ")) 
            i=0
            while i<2 and i<antal:      #loopen körs lika många ggr som antal om inte antal är större än 2. för att grammatiken ska stämma: 1:a 2:a
                    print("Vad heter", str(i+1) + ":a studenten i förnamn? ", end="")    
                    förnamn=input()     
                    print("Vad heter", str(i+1) + ":a studenten i efternamn? ", end="")
                    efternamn=input()
                    print("Vad är", str(i+1) + ":a studentens personnummer? ", end="")
                    personnummer=input()
                    klasslista.append(Student(förnamn, efternamn, personnummer))    #lägger in värderna i klasslistan
                    i+=1
            while i>=2 and i<antal: #när antal är större än 2 hoppar funk till denna loop för att grammatiken ska stämma: 3:e 4:e osv.
                    print("Vad heter", str(i+1) + ":e studenten i förnamn? ", end="")    
                    förnamn=input()     
                    print("Vad heter", str(i+1) + ":e studenten i efternamn? ", end="")
                    efternamn=input()
                    print("Vad är", str(i+1) + ":e studentens personnummer? ", end="")
                    personnummer=input()                   
                    klasslista.append(Student(förnamn, efternamn, personnummer))    #lägger in värderna i klasslistan
                    i+=1    #i ökar med 1 efter varje loop
            print("Här är alla i klassen:")
            for student in klasslista:  #printar klasslistan
                print(student)
            print()
            
        elif kommando==3:    #om användaren väljer alt 3
            if  len(klasslista)==0:     #om det inte finns någon i klasslistan kan det inte raderas någon
                print("Det finns ingen i klassen")
            else:
                print("Här är alla i klassen:")
                pos=1   #första namnet har plats 1
                for s in klasslista:    #printar ut den existerande klasslistan med dess position framför
                    print(pos, ": ", end="")
                    print(s)
                    pos+=1      #gör att positionen ökar med 1
                q=int(input("Vilken position i listan har den du vill ta bort? "))  #q blir positionen du vill ta borts index-position
                del klasslista[q-1]     #eftersom index börjar med 0 raderas q-1
                print("Här är den uppdaterade listan:") #printar den uppdaterade klasslistan
                for s in klasslista:    #printar klasslistan
                    print(s)
                print()

        elif kommando==4:    #om användaren väljer alt 4
            if  len(klasslista)==0: #om klasslistans längd är 0 (inga objekt)
                print("Det finns ingen i klassen")
            else:   #om ddet finns objekt i listan
                print("Här är alla i klassen:")
                for s in klasslista:    #printar klasslistan
                    print(s)
                print()
                q=0
                while q==0: #för tydlighetens skull måste användaren trycka enter för att gå vidare
                    input("Tryck enter för att fortsätta") #input sätts inte som något värde utan blir bara ett steg för att q ska öka med 1
                    q+=1    #q ökar med 1 vilket gör att whileförhållandet inte gäller
            print()
        elif kommando==5:    #om användaren väljer alt 5 breakas loopen och programmet avslutas
            break

        else:
            print("Du kan endast skriva 1-5")   #om användaren inte skriver ett tal i menyn körs loopen igen 
            print()
        

huvudprogram()
        
