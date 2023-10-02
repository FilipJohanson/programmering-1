

def heltal():
    """funktionen säkerställer att antalet studenter är ett positivt heltal"""
    while True:     #whilesatsen loopar så länge inmatningen inte är ett heltal
        try:
            antal=int(input()) 
            if antal<=0:    #om antal är 0 eller mindre breakar inte loopen  
                print("Du måste skriva ett heltal, prova igen: ", end="")
            else:
                break   
        except ValueError:     #bryter loopen så länge det inte blir ValuError
            print("Du får endast skriva ett heltal, prova igen: ", end="")
    return antal    #sätter funktinens värde till antal 

def personnummer(): 
    """funktionen kontrollerar att personnr bara innehåller siffror"""
    while True:
        nr=input()
        if nr.isnumeric():  #isnumeric kontrollerar att det bara är siffror
            break   #breakar om det bara är siffror
        else:
            print("Personnummret kan bara innehålla siffror. Testa igen: ", end="")
    return nr
