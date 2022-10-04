kod = "ABC123"
a=0

while a !=1:
    losenord=input("Vad ar koden? ")
    if losenord==kod: 
        print("Losenord OK") 
        a+=1
    elif losenord=="" : 
        print("AVBRYTER INLOGGNING")
        a+=1
    else:
        print("FEL LOSENORD! KLICKA ENTER FOR ATT AVRBYTA") 
        
