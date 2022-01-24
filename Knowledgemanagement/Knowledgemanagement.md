# Knowledgemanagement: Datenauswertung

  Die Auswertung der Magnetfelddaten ist komplex. Im Rahmen der Datenauswertung ist viel Wissen und Erfahrung notwendig, um valide Aussagen und Entscheidungen treffen zu können.  



| Englisch | Deutsch | Synonyme | Erklärung/Bemerkung             | Beispiel                        |
| -------- | -------- | -------- | ------------------------------- | ------------------------------- |
|current|Strom|
|depth|Tiefe|
|empit_lab_gps|||empitlab, elab|
|noise|Rauschen||Störungen durch Umwelteinflüsse|Hochspannugnsmasten, Stromkabel|
|lateral offset|Seitenversatz|
___

## Pipeline Engineering

Feldbögen bis ca. 20°


## empit_lab_gps

Das Auswertungstool zur Verwertung der vom Feldteam generierten Daten ist empit_lab_gps. Unser Chefentwickler ist der Physiker __Albin Hertrich__. 

Die Software ist in python gescchrieben und wird dem Team Auswertung containisiert zur Verfügung gestellt

## Datenauswertungsstages


pre-alpha- Proof of concept erbracht

- Ausreichend für einen qualitativen Eindruck

### alpha- Feature vollständig

- Review im Team

### beta- Integration/Zusammenspiel aller Features

- Review im Team

### final- Review außerhalb des Teams





### Das Integritätspanel

In 

### Verhalten der fit Ergebnisse in Bezug auf current, depth, lateral, offset

### Thema Verfügbarerer Strom

Verschlechterung des SNR mit steigender Frequenz, da Impendaz( wechselstrom widerstand) steigt. Hinzu kommt der Skineffekt, da der effektive Querschnitt des Stroms sich verringert, folglich fließt weniger Ampere.

ALles was mettall ist kann potentiell Spiegel sein. Je höher die Frequenz, desto undurchlässiger sind Metalle (Skineffekt weitergeführt).

Strom und Tiefe können sich kompensieren → 10 m 30 A 1 m 3 A Fitstom strom → Zähler/tiefe nenner

Zu Begin sei angemerkt, dass der Strom (current) nicht physikalisch gemessen wird, sondern mittels Gleichungssysteme zurück gerechnet wird. 

Die gesamten 

Ein Indikator für eine schlechte Datenlage ist, wenn eine hohe Korrelation  (sei es proportional oder anti-proportional) der physikalischen/geometrischen Größen vorliegt.

### Signal-Noise-Ratio

Das Signal-Noise ratio ist das Verhältnis von induziertem Signal zu Umweltbedingten Störeinflüssen Signal/Noise. Rauschen wird durch durchstömte elektrische Leiter in der Umgebung induziert, wie bspw. 50 Hz Hochspannungsleiter. 

Im contour plot ist Rauschen daran zu erkennen, dass keine großflächigen ergo kleinflächige Änderungen zu erkennen sind (Abbildung folgt).

In der folgenden Abbildung ist kein Rauschen zu erkennen.

![[aca-a4_no_noise.jpg]]
___


### Induktive Kopplung


___


### Kapazitive Kopplung


___


### ACVG


___


## Spline

blocklength specific parameter:
- turning_point_distance
- overlap



### Troubleshooting workarounds

Wenn sich ein Splinesegment nicht öffnen lässt und der folgende o.ä. Fehler auftritt:

![[splinesegment_opening_error_traceback.jpg]]

ist der komplementär Plot zu öffnen, eine minimale Änderung zu machen, worauf hin sich die Splinekoeffizienten ändern und sich das gewünschte, zu verändernde Segment, wieder öffnen und manipulieren lässt.


## Splineoptimierungsworkaround

### HWW

Bögen ab 1°

maximale Quali.

Deadline 2 Wochen

### Astora

Termin um 14 Uhr

Bögen ab 5°




## Qualitätsmatrix

Achsen: Datenqualität, Auswertungsqualität
Schnell zu verstehen was haben wir für eine Datenqualitätie und weit wollen wir Aufwandstechnsich in der Auswertung hin → Kosten/Nutzen
