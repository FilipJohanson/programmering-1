"""Programmering 1: Labb 3 22/9-2023"""

import felhantering_labb3   
"""importerar felhanteringsmodulen"""

def arisumma(startvärde, diff, antal_tal):
    """beräknar summan av en aritmetisk talföljd"""
    sista_talet=startvärde+diff*antal_tal-diff #beräknar sista talet i följdne
    summa=antal_tal*(startvärde+sista_talet)*0.5 
    return summa    #sätter funktionens värde till summa

def geosumma(startvärde, kvot, antal_tal):
    """beräknar summan av en geometrisk talföljd"""
    summa=startvärde*(kvot**antal_tal-1)/(kvot-1)   
    return summa     #sätter funktionens värde till summa

def huvudprogram():
    """användaren skriver in variabelvärden och funktionen felhanterar dem, sedan beräknar den största talföljden"""
    print("Skriv startvärde för den aritmetiska talföljden: ", end="")
    startvärde_ari=felhantering_labb3.decimal()   #startvärde_ari kallar på decimal() i felhanteringsmodulen. I den får användaren skriva ett värde som felhanteras och sätts som startvärde_ari
    print("Skriv differensen: ", end="")
    diff=felhantering_labb3.decimal()     #diff kallar på decimal() i felhanteringsmodulen. I den får användaren skriva ett värde som felhanteras och sätts som diff
    print("Skriv antal tal i följden: ", end="")
    antal_ari=felhantering_labb3.antal_tal()    #antal_ari kallar på antal_tal() i felhanteringsmodulen. I den får användaren skriva ett värde som felhanteras och sätts som antal_ari
    print("Summan av den aritmetiska talföljden är: " + str(arisumma(startvärde_ari, diff, antal_ari)))     #aritmetiska summan printas

    print("Skirv starvärde för den geometriska talföljden: ", end="")
    starvärde_geo=felhantering_labb3.decimal()  #startvärde_geo kallar på decimal() i felhanteringsmodulen. I den får användaren skriva ett värde som felhanteras och sätts som startvärde_ari
    print("Skriv kvoten: ", end="")
    kvot=felhantering_labb3.kvoten()    #kvot kallar på kvoten() i felhanteringsmodulen. I den får användaren skriva ett värde som felhanteras och sätts som kvot
    print("Skriv antal tal i talföljden: ", end="")
    antal_geo=felhantering_labb3.antal_tal()    #antal_geo kallar på antal_tal() i felhanteringsmodulen. I den får användaren skriva ett värde som felhanteras och sätts som antal_geo
    print("Summan av den geometriska talföljden är: " + str(geosumma(starvärde_geo,kvot,antal_geo)))    #geometriska summan printas

    aritmetiska_summa = arisumma(startvärde_ari,diff,antal_ari)     #ger funktionernas värden ett variabelnamn
    geometrisk_summa = geosumma(starvärde_geo,kvot,antal_geo)


    if geometrisk_summa>aritmetiska_summa:      #jämför summorna med varandra och printar en slutsats
        print("Den geometriska summan är störst!")
    if aritmetiska_summa>geometrisk_summa:
        print("Den aritmetiska summan är störst!")
    if aritmetiska_summa==geometrisk_summa:
        print("Summorna är lika stora!")

huvudprogram()