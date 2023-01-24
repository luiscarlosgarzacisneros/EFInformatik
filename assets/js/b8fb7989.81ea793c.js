"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[938],{3647:(e,n,a)=>{a.r(n),a.d(n,{assets:()=>o,contentTitle:()=>t,default:()=>h,frontMatter:()=>r,metadata:()=>s,toc:()=>d});var l=a(7462),i=(a(7294),a(3905));const r={},t="Log Buch",s={permalink:"/EFInformatik/2022/08/16/blog",editUrl:"https://github.com/luiscarlosgarzacisneros/EFInformatik/tree/main/blog/2022-08-16-blog.md",source:"@site/blog/2022-08-16-blog.md",title:"Log Buch",description:"26. Aug.",date:"2022-08-16T00:00:00.000Z",formattedDate:"16. August 2022",tags:[],readingTime:4.54,hasTruncateMarker:!1,authors:[],frontMatter:{}},o={authorsImageUrls:[]},d=[],p={toc:d};function h(e){let{components:n,...a}=e;return(0,i.kt)("wrapper",(0,l.Z)({},p,a,{components:n,mdxType:"MDXLayout"}),(0,i.kt)("ol",{start:26},(0,i.kt)("li",{parentName:"ol"},"Aug.\npython repetition gemacht. Habe ein paar Sachen \xfcbersprungen, bin bis zum Pythagoras-Baum gekommen.")),(0,i.kt)("ol",{start:2},(0,i.kt)("li",{parentName:"ol"},"sept. 2022\nalle listen-aufgaben gemacht. ")),(0,i.kt)("ol",{start:8},(0,i.kt)("li",{parentName:"ol"},"sept.\nListen gemacht")),(0,i.kt)("ol",{start:16},(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"sept.\nspielfeld gemacht")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"okt.\nhangman angefangen, topdown modell angeschaut"))),(0,i.kt)("p",null,"28.okt\nhangman, aufgaben funktionen * viereck, selbsttest"),(0,i.kt)("ol",{start:25},(0,i.kt)("li",{parentName:"ol"},"Nov. 2022")),(0,i.kt)("p",null,"Ich habe am Numtrip weitergearbeitet. Jetzt kann der spieler Felder l\xf6schen und der Input wird \xfcberpr\xfcft, so dass das Programm nicht crasht, falls er Falsch ist. Dieser Prozess wird auch unendlich lange wiederholt."),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-py"},"def feldl\xf6schen():\n    zeile = input('zeile: ')\n    spalte = input('spalte: ')\n#Welches Feld soll gel\xf6scht werden?\n    eingabe_zeile = True\n    eingabe_spalte = True\n#Variabel ist True falls input korrekt ist\n\n    if not zeile.isnumeric():\n        eingabe_zeile = False\n    if not spalte.isnumeric():\n        eingabe_spalte = False\n#wenn eingabe keine ganze zahl ist - falsch\n    if zeile.isnumeric():\n        zeile = int(zeile)\n\n        if zeile < 0:\n            eingabe_zeile = False\n        if zeile > 5:\n            eingabe_zeile = False\n\n    if spalte.isnumeric():\n        spalte = int(spalte)\n\n        if spalte < 0:\n            eingabe_spalte = False\n        if spalte > 5:\n            eingabe_spalte = False\n#zahl muss zwischen 1 und 5 sein\n\n    if eingabe_zeile and eingabe_spalte == True:\n        board[zeile - 1][spalte - 1] = ' '\n#wenn eingabe richtig ist - feld l\xf6schen\n    else:\n        print('Fehlerhafte Eingabe')\n# wenn eingabe falsch - mitteilen\n\n")),(0,i.kt)("ol",{start:2},(0,i.kt)("li",{parentName:"ol"},"Dez. 2022")),(0,i.kt)("p",null,"Ich habe das Darstellen von einem Feld vereinfacht:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-py"},"print('I', end='')\nfor g in range(6 - int(len(str(board[zeile][spalte])))):\n    print(' ', end='')\n# feld ist 6 zeichen lang. 6 - stellen zahl = anzahl leerzeichen.\nprint(board[zeile][spalte], end='')\n")),(0,i.kt)("p",null,"und habe das Programm ge\xe4ndert, so dass der Spieler bei einer falschen eingabe eine genaue R\xfcckmeldung bekommt, indem ich eine Variabel 'fehler' brauche. Diese wird je nachdem was der Fehler war ge\xe4ndert und am Schluss geprintet."),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-py"},"def feldl\xf6schen():\n    zeile = input('zeile: ')\n    spalte = input('spalte: ')\n\n    eingabe_zeile = True\n    eingabe_spalte = True\n\n    if not zeile.isnumeric():\n        eingabe_zeile = False\n        fehler = 'eingabe muss eine zahl sein'\n    if not spalte.isnumeric():\n        eingabe_spalte = False\n        fehler = 'eingabe muss eine (ganze) zahl sein'\n\n    if zeile.isnumeric():\n        zeile = int(zeile)\n\n        if zeile < 1:\n            eingabe_zeile = False\n            fehler = 'zahl muss gr\xf6sser als 1 sein'\n        if zeile > 5:\n            eingabe_zeile = False\n            fehler = 'zahl muss kleiner als 5 sein'\n\n    if spalte.isnumeric():\n        spalte = int(spalte)\n\n        if spalte < 1:\n            eingabe_spalte = False\n            fehler = 'zahl muss gr\xf6sser als 1 sein'\n        if spalte > 5:\n            eingabe_spalte = False\n            fehler = 'zahl muss kleiner als 5 sein'\n\n    if eingabe_zeile and eingabe_spalte == True:\n        board[zeile - 1][spalte - 1] = ' '\n    else:\n        print('Fehlerhafte Eingabe')\n        print(fehler)\n# fehler: sagt was der Spieler falsch gemacht hat\n")),(0,i.kt)("ol",{start:6},(0,i.kt)("li",{parentName:"ol"},"Dez 2022\nNachbarnzellen der gleichen Zahl werden jetzt auch gel\xf6scht. Das Programm geht \xfcberpr\xfcft alle Zellen.")),(0,i.kt)("h1",null,"23. Jan 2023 - Finaler Blogbeitrag"),(0,i.kt)("h2",null,"Ziel des Spiels"),"Das ist ein die Zahl 1024 zu erreichen (oder eine andere Zahl, wenn man will), indem man Nachbarfelder mit der gleichen Zahl zusammen kombiniert. Dabei verdoppelt sich der Wert.",(0,i.kt)("h2",null,"Umsetzung des Spiels"),(0,i.kt)("h3",null,"Voraussetzungen"),"Um das Spiel zu spielen bracht man mindestens Python 3",(0,i.kt)("h3",null,"Top-Down"),(0,i.kt)("h3",null,"Erkl\xe4rung eines algorithmischen Konzepts: Felder auff\xfcllen"),"Zuerst m\xfcssen Felder, die oberhalb eines ' '-Feldes sind nach unten verschoben werden, damit die leeren Felder alle immer an den obersten Stellen in den Spalten sind. Das simuliert das Fallen der Bl\xf6cke. Mit zwei For-Loops werden alle Felder \xfcberpr\xfcft, ob sie leere Felder unten ihnen haben und wenn ja nach unten verschoben.",(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-py"},"for i in range(5):\n                for i in range(5):\n                    if zeile + 1 < 5:\n                        if board[zeile + 1][spalte] == ' ':\n                            board[zeile + 1][spalte] = board[zeile][spalte]\n                            board[zeile][spalte] = ' '\n                        zeile = zeile + 1\n                zeile = 0\n                spalte = spalte + 1\n")),(0,i.kt)("p",null,"Nach der ersten Verschiebung nach unten k\xf6nnen wir schon anfangen neue Felder ins Spiel zu bringen. Es wird \xfcberpr\xfcft, ob die obersten Felder leer sind und wenn ja mit einer Zufallszahl (1,2 oder4) gef\xfcllt."),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-py"},"# wenn ein Feld oben leer ist, wird es mit einer zuf\xe4lligen Zahl (1,2 oder 4) gef\xfcllt.\n            numbers = [1, 2, 4]\n            if board[0][0] == ' ':\n                board[0][0] = str(random.choice(numbers))\n            if board[0][1] == ' ':\n                board[0][1] = str(random.choice(numbers))\n            if board[0][2] == ' ':\n                board[0][2] = str(random.choice(numbers))\n            if board[0][3] == ' ':\n                board[0][3] = str(random.choice(numbers))\n            if board[0][4] == ' ':\n                board[0][4] = str(random.choice(numbers))\n")),(0,i.kt)("p",null,"Diese Vorg\xe4nge werden 5-Mal durchgef\xfchrt, damit wir sicher sein k\xf6nnen, dass alle leeren Felder gef\xfcllt worden sind. Beide Algorithmen sehen zusammen so aus:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-py"},"# Felder oberhalb eines ' ' Feldes gehen 1 nah unten. Alle Felder werden \xfcberpr\xfcft\n        spalte = 0\n        zeile = 0\n        for i in range(5):\n            for i in range(5):\n                for i in range(5):\n                    if zeile + 1 < 5:\n                        if board[zeile + 1][spalte] == ' ':\n                            board[zeile + 1][spalte] = board[zeile][spalte]\n                            board[zeile][spalte] = ' '\n                        zeile = zeile + 1\n                zeile = 0\n                spalte = spalte + 1\n            spalte = 0\n\n            # wenn ein Feld oben leer ist, wird es mit einer zuf\xe4lligen Zahl (1,2 oder 4) gef\xfcllt.\n            numbers = [1, 2, 4]\n            if board[0][0] == ' ':\n                board[0][0] = str(random.choice(numbers))\n            if board[0][1] == ' ':\n                board[0][1] = str(random.choice(numbers))\n            if board[0][2] == ' ':\n                board[0][2] = str(random.choice(numbers))\n            if board[0][3] == ' ':\n                board[0][3] = str(random.choice(numbers))\n            if board[0][4] == ' ':\n                board[0][4] = str(random.choice(numbers))\n")),(0,i.kt)("h2",null,"Gr\xf6sste Herausforderungen"),"Die gr\xf6sste Herausforderung war das Floodfill zu implementieren, da ich noch nie mit rekursiven Funktionen gearbeitet habe.",(0,i.kt)("h2",null,"Tipps f\xfcr andere Sch\xfcler"),"Ich h\xe4tte ganz am Anfang eine Funktion gemacht, dass kontroliert, ob ein Feld existiert, so dass ich nicht jedes Mal das neu bei einer funktion schreiben muss. Das h\xe4tte mir sehr viel Zeit gespart.")}h.isMDXComponent=!0}}]);