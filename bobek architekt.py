#vlozenie modulov
import tkinter

#nastavenie platna
canvas = tkinter.Canvas(width=1000, height=500, background="white")
canvas.pack()

#otvorenie suboru na citanie
subor = open("zastavba_na_ulici.txt","r")

#vytvorenie prazdnych zoznamov
sirky = []
vysky = []

def budovy(): #funkcia na vykreslenie budov
    #nastavenie pociatocnej suradnice
    x = 0
    
    for riadok in subor: #cyklus na prechadzanie riadku v subore
        riadocek = riadok.split()

        #zapisanie sirky a vysky
        sirka = int(riadocek[0])
        vyska = int(riadocek[1])

        #vlozenie zistenych hodnot do zoznamov
        sirky.append(sirka)
        vysky.append(vyska)

        #podmienka na vykreslenie budovy alebo pozemku
        if not vyska == 0:
            canvas.create_rectangle(x,450,x+sirka,450-vyska,fill="grey")
        else:
            canvas.create_rectangle(x,451,x+sirka,449,fill="green",outline="")

        #zmena suradnice
        x += sirka

def vyskovy_rozdiel(): #funkcia na vykreslenie vyskoveho rozdielu
    #zistenie prevysenia z Entry boxu
    prevysenie = int(entry1.get())

    #nastavenie pomocnych premennych
    poradie = 0
    sirka = 0

    for i in vysky: #cyklus na prechadzanie hodnot v zozname
        #podmienka na neriesenie prvej hodnoty
        if not poradie == 0:
            #zaznacenie predoslej hodnoty
            pred = vysky[poradie-1]

            #podmienka na vypocet rozdielu
            if int(i) < pred:
                rozdiel = pred - int(i)
                ostava = pred - rozdiel
            else:
                rozdiel = int(i) - pred
                ostava = int(i) - rozdiel

            #podmienka na vykreslenie prevysenia
            if rozdiel >= prevysenie and vysky[poradie-1] != 0:
                canvas.create_rectangle(sirka-1,450-ostava,sirka+1,450-ostava-rozdiel,fill="red",outline="")

        #zmena pomocnych premennych
        sirka += sirky[poradie]
        poradie += 1

#vytvorenie Entry boxu
entry1 = tkinter.Entry()
entry1.pack()

#vytvorenie tlacidla
tlacitko = tkinter.Button(text='vykresli',command=vyskovy_rozdiel)
tlacitko.pack()

#zavolanie funkcie
budovy()
