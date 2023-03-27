"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[413],{738:e=>{e.exports=JSON.parse("{\"blogPosts\":[{\"id\":\"/2022/08/16/blog\",\"metadata\":{\"permalink\":\"/EFInformatik/2022/08/16/blog\",\"editUrl\":\"https://github.com/luiscarlosgarzacisneros/EFInformatik/tree/main/blog/2022-08-16-blog.md\",\"source\":\"@site/blog/2022-08-16-blog.md\",\"title\":\"Log Buch\",\"description\":\"26. Aug.\",\"date\":\"2022-08-16T00:00:00.000Z\",\"formattedDate\":\"16. August 2022\",\"tags\":[],\"readingTime\":6.275,\"hasTruncateMarker\":false,\"authors\":[],\"frontMatter\":{}},\"content\":\"26. Aug. \\npython repetition gemacht. Habe ein paar Sachen \xfcbersprungen, bin bis zum Pythagoras-Baum gekommen.\\n\\n\\n2. sept. 2022\\nalle listen-aufgaben gemacht. \\n\\n\\n8. sept.\\nListen gemacht\\n\\n\\n16. sept.\\nspielfeld gemacht\\n\\n21. okt.\\nhangman angefangen, topdown modell angeschaut\\n\\n28.okt \\nhangman, aufgaben funktionen * viereck, selbsttest\\n\\n25. Nov. 2022\\n\\nIch habe am Numtrip weitergearbeitet. Jetzt kann der spieler Felder l\xf6schen und der Input wird \xfcberpr\xfcft, so dass das Programm nicht crasht, falls er Falsch ist. Dieser Prozess wird auch unendlich lange wiederholt.\\n\\n```py\\ndef feldl\xf6schen():\\n    zeile = input('zeile: ')\\n    spalte = input('spalte: ')\\n#Welches Feld soll gel\xf6scht werden?\\n    eingabe_zeile = True\\n    eingabe_spalte = True\\n#Variabel ist True falls input korrekt ist\\n\\n    if not zeile.isnumeric():\\n        eingabe_zeile = False\\n    if not spalte.isnumeric():\\n        eingabe_spalte = False\\n#wenn eingabe keine ganze zahl ist - falsch\\n    if zeile.isnumeric():\\n        zeile = int(zeile)\\n\\n        if zeile < 0:\\n            eingabe_zeile = False\\n        if zeile > 5:\\n            eingabe_zeile = False\\n\\n    if spalte.isnumeric():\\n        spalte = int(spalte)\\n\\n        if spalte < 0:\\n            eingabe_spalte = False\\n        if spalte > 5:\\n            eingabe_spalte = False\\n#zahl muss zwischen 1 und 5 sein\\n\\n    if eingabe_zeile and eingabe_spalte == True:\\n        board[zeile - 1][spalte - 1] = ' '\\n#wenn eingabe richtig ist - feld l\xf6schen\\n    else:\\n        print('Fehlerhafte Eingabe')\\n# wenn eingabe falsch - mitteilen\\n\\n```\\n\\n2. Dez. 2022\\n\\nIch habe das Darstellen von einem Feld vereinfacht:\\n\\n```py\\nprint('I', end='')\\nfor g in range(6 - int(len(str(board[zeile][spalte])))):\\n    print(' ', end='')\\n# feld ist 6 zeichen lang. 6 - stellen zahl = anzahl leerzeichen.\\nprint(board[zeile][spalte], end='')\\n```\\nund habe das Programm ge\xe4ndert, so dass der Spieler bei einer falschen eingabe eine genaue R\xfcckmeldung bekommt, indem ich eine Variabel 'fehler' brauche. Diese wird je nachdem was der Fehler war ge\xe4ndert und am Schluss geprintet.\\n\\n```py\\ndef feldl\xf6schen():\\n    zeile = input('zeile: ')\\n    spalte = input('spalte: ')\\n\\n    eingabe_zeile = True\\n    eingabe_spalte = True\\n\\n    if not zeile.isnumeric():\\n        eingabe_zeile = False\\n        fehler = 'eingabe muss eine zahl sein'\\n    if not spalte.isnumeric():\\n        eingabe_spalte = False\\n        fehler = 'eingabe muss eine (ganze) zahl sein'\\n\\n    if zeile.isnumeric():\\n        zeile = int(zeile)\\n\\n        if zeile < 1:\\n            eingabe_zeile = False\\n            fehler = 'zahl muss gr\xf6sser als 1 sein'\\n        if zeile > 5:\\n            eingabe_zeile = False\\n            fehler = 'zahl muss kleiner als 5 sein'\\n\\n    if spalte.isnumeric():\\n        spalte = int(spalte)\\n\\n        if spalte < 1:\\n            eingabe_spalte = False\\n            fehler = 'zahl muss gr\xf6sser als 1 sein'\\n        if spalte > 5:\\n            eingabe_spalte = False\\n            fehler = 'zahl muss kleiner als 5 sein'\\n\\n    if eingabe_zeile and eingabe_spalte == True:\\n        board[zeile - 1][spalte - 1] = ' '\\n    else:\\n        print('Fehlerhafte Eingabe')\\n        print(fehler)\\n# fehler: sagt was der Spieler falsch gemacht hat\\n```\\n\\n\\n6. Dez 2022\\nNachbarnzellen der gleichen Zahl werden jetzt auch gel\xf6scht. Das Programm geht \xfcberpr\xfcft alle Zellen.\\n\\n\\n\\n<h1>23. Jan 2023 - Finaler Blogbeitrag</h1>\\n\\n\\n<h2>Ziel des Spiels</h2>\\nDas ist ein die Zahl 1024 zu erreichen (oder eine andere Zahl, wenn man will), indem man Nachbarfelder mit der gleichen Zahl zusammen kombiniert. Dabei verdoppelt sich der Wert.\\n\\n<h2>Umsetzung des Spiels</h2>\\n\\n<h3>Voraussetzungen</h3>\\nUm das Spiel zu spielen bracht man mindestens Python 3\\n\\n<h3>Top-Down</h3>\\n\\n![](Numtrip.jpg)\\n\\n<h3>Erkl\xe4rung eines algorithmischen Konzepts: Felder auff\xfcllen</h3>\\nZuerst m\xfcssen Felder, die oberhalb eines ' '-Feldes sind nach unten verschoben werden, damit die leeren Felder alle immer an den obersten Stellen in den Spalten sind. Das simuliert das Fallen der Bl\xf6cke. Mit zwei For-Loops werden alle Felder \xfcberpr\xfcft, ob sie leere Felder unten ihnen haben und wenn ja nach unten verschoben.\\n\\n```py\\nfor i in range(5):\\n                for i in range(5):\\n                    if zeile + 1 < 5:\\n                        if board[zeile + 1][spalte] == ' ':\\n                            board[zeile + 1][spalte] = board[zeile][spalte]\\n                            board[zeile][spalte] = ' '\\n                        zeile = zeile + 1\\n                zeile = 0\\n                spalte = spalte + 1\\n```\\n\\nNach der ersten Verschiebung nach unten k\xf6nnen wir schon anfangen neue Felder ins Spiel zu bringen. Es wird \xfcberpr\xfcft, ob die obersten Felder leer sind und wenn ja mit einer Zufallszahl (1,2 oder4) gef\xfcllt.\\n\\n```py\\n# wenn ein Feld oben leer ist, wird es mit einer zuf\xe4lligen Zahl (1,2 oder 4) gef\xfcllt.\\n            numbers = [1, 2, 4]\\n            if board[0][0] == ' ':\\n                board[0][0] = str(random.choice(numbers))\\n            if board[0][1] == ' ':\\n                board[0][1] = str(random.choice(numbers))\\n            if board[0][2] == ' ':\\n                board[0][2] = str(random.choice(numbers))\\n            if board[0][3] == ' ':\\n                board[0][3] = str(random.choice(numbers))\\n            if board[0][4] == ' ':\\n                board[0][4] = str(random.choice(numbers))\\n```\\n\\nDiese Vorg\xe4nge werden 5-Mal durchgef\xfchrt, damit wir sicher sein k\xf6nnen, dass alle leeren Felder gef\xfcllt worden sind. Beide Algorithmen sehen zusammen so aus:\\n\\n```py\\n# Felder oberhalb eines ' ' Feldes gehen 1 nah unten. Alle Felder werden \xfcberpr\xfcft\\n        spalte = 0\\n        zeile = 0\\n        for i in range(5):\\n            for i in range(5):\\n                for i in range(5):\\n                    if zeile + 1 < 5:\\n                        if board[zeile + 1][spalte] == ' ':\\n                            board[zeile + 1][spalte] = board[zeile][spalte]\\n                            board[zeile][spalte] = ' '\\n                        zeile = zeile + 1\\n                zeile = 0\\n                spalte = spalte + 1\\n            spalte = 0\\n\\n            # wenn ein Feld oben leer ist, wird es mit einer zuf\xe4lligen Zahl (1,2 oder 4) gef\xfcllt.\\n            numbers = [1, 2, 4]\\n            if board[0][0] == ' ':\\n                board[0][0] = str(random.choice(numbers))\\n            if board[0][1] == ' ':\\n                board[0][1] = str(random.choice(numbers))\\n            if board[0][2] == ' ':\\n                board[0][2] = str(random.choice(numbers))\\n            if board[0][3] == ' ':\\n                board[0][3] = str(random.choice(numbers))\\n            if board[0][4] == ' ':\\n                board[0][4] = str(random.choice(numbers))\\n```\\n\\n<h2>Gr\xf6sste Herausforderungen</h2>\\nDie gr\xf6sste Herausforderung war das Floodfill zu implementieren, da ich noch nie mit rekursiven Funktionen gearbeitet habe.\\n\\n<h2>Tipps f\xfcr andere Sch\xfcler</h2>\\nIch h\xe4tte ganz am Anfang eine Funktion gemacht, dass kontroliert, ob ein Feld existiert, so dass ich nicht jedes Mal das neu bei einer funktion schreiben muss. Das h\xe4tte mir sehr viel Zeit gespart.\\n\\n\\n\\n17. m\xe4rz 2023\\n\\nFolgende Sachen haben wir in der letzen Woche gemacht:\\n\\nNode RED\\nNode-RED ist ein Tool zur visuellen Programmierung von Flows. Es bietet eine grafische Oberfl\xe4che\\nzum Verbinden von Nodes das sind die kleinen k\xe4stchen die auf Abbildung 1 zu sehen sind, um\\nDaten zu verarbeiten und automatsierte Abl\xe4ufe zu erstellen. Es bietet die M\xf6glichkeit, messger\xe4te\\nu.a miteinander zu verknu\u0308pfen und zu automatsieren und wie in userem fall sp\xe4ter dann daten zu\\nsammeln. Node-RED kann Kombinaton mit verschiedenen Platformen wie Arduinos und Raspberry\\nPi wie zum beispiel unser kleines CO2 messger\xe4t verwendet werden.\\n\\nPostman\\nPostman ist eine Softwareanwendung zur Erstellung, Verwaltung und Testung von APIs. Es bietet eine\\nbenutzerfreundliche Oberfl\xe4che zum Senden von HTTP-Anfragen an eine API und zum Anzeigen der\\nAntwort. Es erm\xf6glicht Entwicklern, schnell API-Endpoints zu testen und zu debuggen, indem sie\\nAnfragen und Antworten in einer visuellen Umgebung anzeigen.\\n\\nAuf dem Programm Postman kann man dann unsere API verwenden, indem man einen GET-Request\\nerstellt und den zu konvertierenden Text u\u0308bergibt. Die API wandelt dann den Text in Emojis um und\\ngibt das Ergebnis zuru\u0308ck. Das ist eine einfache M\xf6glichkeit, um zu testen, ob die API wie erwartet\\nfunktoniert. Man kann den Request-URL in Postman eingeben und den gewu\u0308nschten Text\\nu\u0308bergeben. Wenn alles funktoniert, sollte man die Emojis als Antwort erhalten.\\n\\n23. M\xe4rz\\nAuthenzifizierung eines Benutzers:\\nWir haben in Node-RED einen Flow gemacht, der zwei HTML-Seiten enth\xe4lt: eine _welcome.html_ und eine _login.html_. Aufbau: Die Login-Funktion sucht in der Datenbank nach Benutzernamen und Passwort und \xfcberpr\xfcft, ob sie \xfcbereinstimmen. Dies wird in den Cookies gespeichert.\\n\\nDatenbank:\\n```py\\nflow.set(\\n\xa0\xa0\xa0 \\\"johnny\\\",\\n\xa0\xa0\xa0 {\\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0 pw: \\\"qwert\\\"\\n\xa0\xa0\xa0 }\\n)\\nflow.set(\\n\xa0\xa0\xa0 \\\"maria\\\",\\n\xa0\xa0\xa0 {\\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0 pw: \\\"asdf\\\"\\n\xa0\xa0\xa0 }\xa0)\\nreturn msg;\\n```\\n\\nCookies:\\n```py\\nif (user){\\n\xa0\xa0\xa0 if (password== user.pw){\\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0 msg.cookies = {\\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 auth: true,\\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 name: name\\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0 }\\n\xa0\xa0\xa0 }\\n}\xa0\\n```\\nDie Login Funktion leitet uns and die entscprechende seite weiter: _welcome.html_.\\n\\nDas Problem ist, dass man ein Passwort niemals abspeichern darf. Man muss sie immer gehasht abspeichern, da sonst bei einem Datenleak alle Benutzernamen und Passw\xf6rter ver\xf6ffentlicht\xa0werden\xa0k\xf6nnten.\\n\\nhttps://node-red-ol18.onrender.com/#flow/ed73c51f6c96ba27\"}]}")}}]);