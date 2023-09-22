"""Programmering 1: Labb 3 (felhanteringsmodul) 22/9-2023"""

def decimal():
    """funktionen säkerställer att användaren skriver ett tal"""
    while True:     #whilesatsen loopar så länge inmatningen inte är ett tal
        try:
            deci=float(input())
            break   #bryter loopen om deci är ett tal
        except ValueError:  #loopen bryts inte om inmatning inte är ett tal
            print("Du får endast skriva ett tal, prova igen: ", end="")
    return deci   #sätter funktionens värde till deci

def antal_tal():
    """funktionen säkerställer att antalet tal i summorna är ett positivt heltal"""
    while True:     #whilesatsen loopar så länge inmatningen inte är ett heltal
        try:
            antal=int(input()) 
            if antal<=0:    #om antal är 0 eller mindre breakar inte loopen  
                print("Antalet tal kan måste vara större än noll, prova igen: ", end="")
            else:
                break   
        except ValueError:     #bryter loopen så länge det inte blir ValuError
            print("Du får endast skriva ett heltal, prova igen: ", end="")
    return antal    #sätter funktinens värde till antal 

def kvoten():
    """funktionen bygger vidare decimal() och säger att kvoten inte kan vara 1, 0 eller mindre"""
    while True:
        kvot=decimal()  #använder decimal():s felhantering
        if kvot==1 or kvot<=0:  #om kvoten är detta breakar inte loopen
            print("kvoten får inte vara 1, 0 eller negativt, prova igen, ", end="")
        else:
            break
    return kvot     #sätter funktionens värde till kvot