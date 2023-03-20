
API
Die Lösung ist eine API. Eine API ist das Werkzeug, das die Daten einer Website für einen Computer verdaulich macht. Dadurch kann ein Computer Daten anzeigen und bearbeiten, genau wie eine Person es kann, indem er Seiten lädt und Formulare absendet. Es ist gut, die Arbeit mit Daten zu vereinfachen, weil es bedeutet, dass Menschen Software schreiben können, um langwierige und arbeitsintensive Aufgaben zu automatisieren. Wofür ein Mensch Stunden brauchen würde, kann ein Computer über eine API Sekunden brauchen.

HTTP
Im Web ist das Hauptprotokoll das Hyper-Text Transfer Protocol, besser bekannt unter seinem Akronym HTTP. Wenn Sie eine Adresse wie http://example.com in einen Webbrowser eingeben, weist das „http“ den Browser an, die HTTP-Regeln zu verwenden, wenn er mit dem Server kommuniziert.
Die Kommunikation in HTTP dreht sich um ein Konzept namens Anfrage-Antwort-Zyklus. Der Client sendet dem Server eine Anfrage, etwas zu tun. Der Server wiederum sendet dem Client eine Antwort, die besagt, ob der Server die Anfrage des Clients ausführen konnte oder nicht.
Um eine gültige Anfrage zu stellen, muss der Client vier Dinge angeben:
URL (Uniform Resource Locator) 1
Methode
Liste der Überschriften
Körper

URL
URL ist eine eindeutige Adresse für ein Ding (ein Substantiv). Welche Dinge Adressen bekommen, liegt ganz bei dem Unternehmen, das den Server betreibt. Sie können URLs für Webseiten, Bilder oder sogar Videos erstellen

METHODE
Die vier Methoden, die am häufigsten in APIs verwendet werden, sind:
GET – Fordert den Server auf, eine Ressource abzurufen
POST – Fordert den Server auf, eine neue Ressource zu erstellen
PUT – Fordert den Server auf, eine vorhandene Ressource zu bearbeiten/aktualisieren
DELETE – Fordert den Server auf, eine Ressource zu löschen


HEADER
Header stellen Metainformationen zu einer Anfrage bereit. Sie sind eine einfache Liste von Elementen wie der Zeit, zu der der Client die Anfrage gesendet hat, und der Größe des Anfragetexts.
Haben Sie mit Ihrem Smartphone schon einmal eine Website besucht, die speziell für Mobilgeräte formatiert wurde? Möglich macht das ein HTTP-Header namens „User-Agent“. Der Client verwendet diesen Header, um dem Server mitzuteilen, welche Art von Gerät Sie verwenden, und Websites, die intelligent genug sind, um dies zu erkennen, können Ihnen das beste Format für Ihr Gerät senden.

BODY
Der Anfragetext enthält die Daten, die der Client an den Server senden möchte.

HTTP-ANTWORT
Nachdem der Server eine Anfrage vom Client erhalten hat, versucht er, die Anfrage zu erfüllen und dem Client eine Antwort zurückzusenden. HTTP-Antworten haben eine sehr ähnliche Struktur wie Anfragen. Der Hauptunterschied besteht darin, dass die Antwort anstelle einer Methode und einer URL einen Statuscode enthält. Darüber hinaus folgen die Response-Header und -Body dem gleichen Format wie Requests.

STATUSCODE
Statuscodes sind dreistellige Zahlen, die jeweils eine eindeutige Bedeutung haben. Bei korrekter Verwendung in einer API kann diese kleine Zahl viele Informationen an den Client übermitteln. Zum Beispiel haben Sie vielleicht diese Seite während Ihrer Internet-Streifzüge gesehen: 404. 404 bedeutet „nicht gefunden“.

DATEN DARSTELLEN
Ein Computer muss die Daten in ein Format bringen, das der andere versteht. Im Allgemeinen bedeutet dies eine Art Textformat. Die gängigsten Formate in modernen APIs sind JSON (JavaScript Object Notation) und XML (Extensible Markup Language).

JSON
Viele neue APIs haben JSON als Format übernommen, da es auf der beliebten Programmiersprache Javascript aufbaut, die im Web allgegenwärtig ist und sowohl im Front- als auch im Back-End einer Webanwendung oder eines Webdiensts verwendet werden kann. JSON ist ein sehr einfaches Format, das aus zwei Teilen besteht: Schlüssel und Werte. Schlüssel repräsentieren ein Attribut über das beschriebene Objekt. Eine Pizzabestellung kann ein Objekt sein. Es hat Attribute (Schlüssel) wie Krustentyp, Toppings und Bestellstatus.
{
  "crust": "original",
  "toppings": ["cheese", "pepperoni", "garlic"],
  "status": "cooking",
  "customer": {
    "name": "Brian",
    "phone": "573-111-1111"
  }
}


XML
<order>
    <crust>original</crust>
    <toppings>
        <topping>cheese</topping>
        <topping>pepperoni</topping>
        <topping>garlic</topping>
    </toppings>
    <status>cooking</status>
</order>



endpunkte
ein Endpunkt ist die spezifische Adresse, die einen bestimmten Service oder eine bestimmte Funktion innerhalb einer api definiert.

polling
polling bezieht sich auf den Prozess, bei dem eine Anwendung regelmäßig eine api abfragt, um nach aktualisierten Informationen zu suchen. dieser Prozess kann auch als "abfragen" bezeichnet werden.
