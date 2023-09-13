"""Programmering 1: Labb 2 12/9-2023"""

"""beräknar aritmetiska summan"""
def beräkning_arisumma(): 
    while True:     #whilestatsen loopar så länge startvärde inte är ett tal
        try:
            startvärde=float(input("Skirv in startvärdet (a1): "))  
            break       
        except ValueError:      #bryter loopen så länge det inte blir ValuError 
                print("Det är inte ett tal")    
    while True:     #whilestatsen loopar så länge startvärde inte är ett tal
        try:
            diff=float(input("Skirv in differensen (d): "))
            break
        except ValueError:       #bryter loopen så länge det inte blir ValuError
            print("Det är inte ett tal")
    while True: #whilesatsen loopar så länge antal_tal inte är ett heltal
        try:
            antal_tal=int(input("Skirv in antal element i följden (n): "))
            break
        except ValueError:     #bryter loopen så länge det inte blir ValuError
            print("inte ett heltal")                              
    antal_tal=startvärde+diff*antal_tal-diff #beräknar sista talet i följdne
    summa=antal_tal*(startvärde+antal_tal)*0.5 #beräknar summan av alla tal i följden
    print("Den aritmetiska summan är: " + str(summa))
    return summa    #sätter funktionens värde till summa

"""beräknar geometriska summan"""
def beräkning_geosumma():
    while True:     #whilestatsen loopar så länge startvärde inte är ett tal
        try:
            startvärde=float(input("Skirv in startvärdet (g1): "))
            break
        except ValueError:      #bryter loopen så länge det inte blir ValuError
            print("Det är inte ett tal")   
    while True:     #whilestatsen loopar så länge startvärde inte är ett tal
        try:    
            kvot=float(input("Skirv in kvoten (q): "))
            if kvot==1:    #när q är 1 blir nämnaren i divisionen 0. om q==1 printar den "q får inte..."" och brekar inte loopen
                print("q får inte vara 1")
            else:   #om q inte år 0 breakar den loopen 
                break       
        except ValueError:      #bryter loopen så länge det inte blir ValuError
            print("Det är inte ett tal")
    while True: #skapar en slinga som stoppas när n är ett godtyckligt tal
        try:
            antal_tal=int(input("Skirv in antal element i följden (n): "))
            break
        except ValueError:      #bryter loopen så länge det inte blir ValuError
            print("inte ett heltal")      
    summa=startvärde*(kvot**antal_tal-1)/(kvot-1)   #beräknar summan av alla tal
    print("Den geometriska summan är: " + str(summa))
    return summa     #sätter funktionens värde till summa

"""bestämmer värdet på första summan efter användaren väljer om det är en aritmetisk eller geometrisk talföljd"""
def första_summan():    
    värde_av_input=input("Är den första summan [a]rtimetisk eller [g]eometrisk?")    #användaren väljer a för ari- och g för geotalföljd 
    if värde_av_input=="a":  #om värdet är a beräknar den funktionen beräkning_arisumma
        summa_funk=beräkning_arisumma()  #summa_funk är värdet av funktionen som returnas till den ursprungliga funktionen: första_summan
        return summa_funk
    if värde_av_input=="g":   #om värdet är g beräknar den funktionen beräkning_geosumma
        summa_funk=beräkning_geosumma() #summa_funk är värdet av funktionen som returnas till den ursprungliga funktionen: första_summan
        return summa_funk            
    else:
        print("Du får bara skriva a eller g")
        print(första_summan())

"""bestämmer värdet på andra summan efter användaren väljer om det är en aritmetisk eller geometrisk talföljd"""
def andra_summan():
    värde_av_input=input("Är den andra summan [a]rtimetisk eller [g]eometrisk?")
    if värde_av_input=="a":     #om värdet är a beräknar den funktionen beräkning_arisumma
        summa_funk=beräkning_arisumma()   #summa_funk är värdet av funktionen som returnas till den ursprungliga funktionen: första_summan
        return summa_funk
    if värde_av_input=="g":     #om värdet är g beräknar den funktionen beräkning_geosumma
        summa_funk=beräkning_geosumma()  #summa_funk är värdet av funktionen som returnas till den ursprungliga funktionen: första_summan
        return summa_funk
    else:   #om användaren skrivit något annat än a eller g kommer ett felmeddelande och den får skriva om
        print("Du får bara skriva a eller g")
        print(andra_summan())
   
"""sätter funktionerna till variabler"""
SUMMA1=första_summan() 
SUMMA2=andra_summan()

"""jämför summorna med varandra och returnerar största summan"""
if SUMMA1>SUMMA2:
    print("Den första summan är störst!")
elif SUMMA2>SUMMA1:
    print("Den andra summan är störst!")
else:
    print("Dem är lika stora :)")
