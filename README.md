# Erkenntnis

Das ist die Destillation. Kein Prozess, keine Beschreibungen — nur das, was
wir jetzt wissen und nicht wussten, bevor wir angefangen haben.

## 1. Das Amortisationsgesetz (fest, gemessen, vorhersagekräftig)

Ein einzelner Messdatensatz aus Classical Shadows beantwortet d Fragen
gleichzeitig; der Vorteil gegenüber dem gewöhnlichen Messen wächst exakt
wie die Wurzel aus d geteilt durch drei hoch dem Observablen-Gewicht:

    Vorteil = sqrt( d / 3^w )

Gemessen gegen Vorhersage: 1.69 zu 1.70, 2.21 zu 2.17, 2.70 zu 2.64.
Grenzfall bestätigt: Auf varianzfreien Observablen (GHZ) kollabiert der
Vorteil auf eins. Das Gesetz ist die Preisliste für jedes künftige
Auslese-Design: Es sagt vor jedem Experiment, ob sich der Umweg über einen
Quantenzustand lohnt oder ob Zählen billiger ist.

## 2. Der Phasenübergang (fest, gemessen, Literatur-nah)

Der überwachte Schaltkreis kippt bei einer Messrate

    p_c = 0.16 bis 0.22

vom verschränkten in den kollabierten Zustand. Der Kipppunkt ist
größenunabhängig im Fenster n gleich 8 bis 20, der Übergang wird schmaler
mit wachsendem n, und er ist asymmetrisch — die linke Flanke fällt etwa
doppelt so steil wie die rechte. Das ist kompatibel mit gerichteter
Perkolation. Offen bleibt die Exponenten-Entscheidung (Kandidaten 4/3 und
2 führen), sie braucht die n gleich 14 bis 20 Daten, die im results-Ordner
nachgereicht werden.

## 3. Die Negativ-Erkenntnis (fest, doppelt belegt)

Die Auslesekosten für den Edge-Case-Projektor explodieren NICHT mit der
Verschränkung. Sie sind flach in der Messrate und flach in der Qubitzahl
bis n gleich 12 — Faktor eins bis vier, keine Tendenz. Zehn unabhängige
Formeln des Hypothesen-Generators sagten alle exponentielles Wachstum
voraus und lagen um Faktor 20 bis 1000 daneben. Konsequenz: Der Sweet Spot,
den das Forschungsprogramm postuliert hat — der optimale Betriebspunkt am
Phasenübergang, erzeugt durch den Zielkonflikt Reichhaltigkeit gegen
Lesekosten — existiert im gesamten messbaren Fenster nicht. Der Zielkonflikt
ist für diese Observable aufgelöst: Lesen ist billig, egal wie verschränkt
der Zustand ist.

## 4. Die Methoden-Erkenntnis (der übertragbare Teil)

Der Hypothesen-Generator ist ein Kandidaten-Filter, kein Beweis-Rechner.
Seine Widerlegungen sind zuverlässig, seine positiven Beweise sind zu rund
der Hälfte dekorativ — erfundene Verifikationszahlen, Vorzeichenfehler,
Verstöße gegen elementare Schranken, sich gegenseitig ausschließende
Formeln alle auf valid. Die funktionierende Schleife ist deshalb: Generator
wirft Kandidaten mit geschlossenen Formeln aus, ein exaktes lokales Orakel
richtet sie innerhalb von Minuten. Vierzig der zweiundvierzig Ansprüche
des Wochenlaufs hat diese Schleife in Minuten statt Wochen entschieden.
Für jede künftige Pipeline gilt der gleiche Baukasten: enge Frage,
Orakel-Anker in die Schablone, Falsifizierbarkeit als Pflichtfeld,
Audit im Stundenrhythmus statt Wochenlauf.

## 5. Wo meine Hoffnung liegt

Drei Stellen, konkret und mit Bedingung. Erstens: Das Amortisationsgesetz
ist das Maß, an dem jeder künftige Quanten-Sampler gemessen werden muss —
wenn jemand behauptet, ein Quanten-Generator lese billiger aus, lautet die
Frage ab jetzt: gegen sqrt(d/3) gerechnet? Diese Zielmarke zu haben ist
mehr wert als jeder einzelne Sampler. Zweitens: Der Phasenübergang ist
echte, unbequeme Struktur — die Exponenten-Entscheidung bei größeren n ist
eine kleine, saubere, publishierbare Frage, und sie kostet nur Strom.
Drittens: Der Formel-Generator läuft heute, klassisch, gratis, mit
Faktor 2.6 Routing-Vorteil — falls die neue Pipeline Trainingsdaten für
symbolische Regression braucht, steht der Lieferant bereit.

Und die Hoffnung, die ich NICHT mehr setze: den Sweet Spot. Sie ist nicht
gescheitert, sie ist erledigt — widerlegt mit Zahlen, von zehn
unabhängigen Formeln bestätigt in ihrer Unmöglichkeit. Das ist der Wert
einer ehrlichen Null.
