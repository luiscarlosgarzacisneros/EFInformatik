"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[413],{738:e=>{e.exports=JSON.parse('{"blogPosts":[{"id":"/2022/08/16/blog","metadata":{"permalink":"/EFInformatik/2022/08/16/blog","editUrl":"https://github.com/luiscarlosgarzacisneros/EFInformatik/tree/main/blog/2022-08-16-blog.md","source":"@site/blog/2022-08-16-blog.md","title":"Log Buch","description":"26. Aug.","date":"2022-08-16T00:00:00.000Z","formattedDate":"16. August 2022","tags":[],"readingTime":2.105,"hasTruncateMarker":false,"authors":[],"frontMatter":{}},"content":"26. Aug. \\npython repetition gemacht. Habe ein paar Sachen \xfcbersprungen, bin bis zum Pythagoras-Baum gekommen.\\n\\n\\n2. sept. 2022\\nalle listen-aufgaben gemacht. \\n\\n\\n8. sept.\\nListen gemacht\\n\\n\\n16. sept.\\nspielfeld gemacht\\n\\n21. okt.\\nhangman angefangen, topdown modell angeschaut\\n\\n28.okt \\nhangman, aufgaben funktionen * viereck, selbsttest\\n\\n25. Nov. 2022\\n\\nIch habe am Numtrip weitergearbeitet. Jetzt kann der spieler Felder l\xf6schen und der Input wird \xfcberpr\xfcft, so dass das Programm nicht crasht, falls er Falsch ist. Dieser Prozess wird auch unendlich lange wiederholt.\\n\\n```py\\ndef feldl\xf6schen():\\n    zeile = input(\'zeile: \')\\n    spalte = input(\'spalte: \')\\n#Welches Feld soll gel\xf6scht werden?\\n    eingabe_zeile = True\\n    eingabe_spalte = True\\n#Variabel ist True falls input korrekt ist\\n\\n    if not zeile.isnumeric():\\n        eingabe_zeile = False\\n    if not spalte.isnumeric():\\n        eingabe_spalte = False\\n#wenn eingabe keine ganze zahl ist - falsch\\n    if zeile.isnumeric():\\n        zeile = int(zeile)\\n\\n        if zeile < 0:\\n            eingabe_zeile = False\\n        if zeile > 5:\\n            eingabe_zeile = False\\n\\n    if spalte.isnumeric():\\n        spalte = int(spalte)\\n\\n        if spalte < 0:\\n            eingabe_spalte = False\\n        if spalte > 5:\\n            eingabe_spalte = False\\n#zahl muss zwischen 1 und 5 sein\\n\\n    if eingabe_zeile and eingabe_spalte == True:\\n        board[zeile - 1][spalte - 1] = \' \'\\n#wenn eingabe richtig ist - feld l\xf6schen\\n    else:\\n        print(\'Fehlerhafte Eingabe\')\\n# wenn eingabe falsch - mitteilen\\n\\n```\\n\\n2. Dez. 2022\\n\\nIch habe das Darstellen von einem Feld vereinfacht:\\n\\n```py\\nprint(\'I\', end=\'\')\\nfor g in range(6 - int(len(str(board[zeile][spalte])))):\\n    print(\' \', end=\'\')\\n# feld ist 6 zeichen lang. 6 - stellen zahl = anzahl leerzeichen.\\nprint(board[zeile][spalte], end=\'\')\\n```\\nund habe das Programm ge\xe4ndert, so dass der Spieler bei einer falschen eingabe eine genaue R\xfcckmeldung bekommt, indem ich eine Variabel \'fehler\' brauche. Diese wird je nachdem was der Fehler war ge\xe4ndert und am Schluss geprintet.\\n\\n```py\\ndef feldl\xf6schen():\\n    zeile = input(\'zeile: \')\\n    spalte = input(\'spalte: \')\\n\\n    eingabe_zeile = True\\n    eingabe_spalte = True\\n\\n    if not zeile.isnumeric():\\n        eingabe_zeile = False\\n        fehler = \'eingabe muss eine zahl sein\'\\n    if not spalte.isnumeric():\\n        eingabe_spalte = False\\n        fehler = \'eingabe muss eine (ganze) zahl sein\'\\n\\n    if zeile.isnumeric():\\n        zeile = int(zeile)\\n\\n        if zeile < 1:\\n            eingabe_zeile = False\\n            fehler = \'zahl muss gr\xf6sser als 1 sein\'\\n        if zeile > 5:\\n            eingabe_zeile = False\\n            fehler = \'zahl muss kleiner als 5 sein\'\\n\\n    if spalte.isnumeric():\\n        spalte = int(spalte)\\n\\n        if spalte < 1:\\n            eingabe_spalte = False\\n            fehler = \'zahl muss gr\xf6sser als 1 sein\'\\n        if spalte > 5:\\n            eingabe_spalte = False\\n            fehler = \'zahl muss kleiner als 5 sein\'\\n\\n    if eingabe_zeile and eingabe_spalte == True:\\n        board[zeile - 1][spalte - 1] = \' \'\\n    else:\\n        print(\'Fehlerhafte Eingabe\')\\n        print(fehler)\\n# fehler: sagt was der Spieler falsch gemacht hat\\n```"}]}')}}]);