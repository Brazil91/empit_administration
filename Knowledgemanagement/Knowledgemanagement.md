# Knowledgemanagement: Datenauswertung

  Die Auswertung der Magnetfelddaten ist komplex. Im Rahmen der Datenauswertung ist viel Wissen und Erfahrung notwendig, um valide Aussagen und Entscheidungen treffen zu können.  

| Englisch       | Deutsch       | Synonyme | Erklärung/Bemerkung             | Beispiel                        |
| -------------- | ------------- | -------- | ------------------------------- | ------------------------------- |
| current        | Strom         |          |                                 |                                 |
| depth          | Tiefe         |          |                                 |                                 |
| empit_lab_gps  |               |          | empitlab, elab                  |                                 |
| noise          | Rauschen      |          | Störungen durch Umwelteinflüsse | Hochspannugnsmasten, Stromkabel |
| lateral offset | Seitenversatz |          |                                 |                                 |

___

## Pipeline Engineering

Feldbögen bis ca. 20°

## empit_lab_gps

Das Auswertungstool zur Verwertung der vom Feldteam generierten Daten ist empit_lab_gps. Unser Chefentwickler ist der Physiker __Albin Hertrich__. 

Die Software ist in python gescchrieben und wird dem Team Auswertung containisiert zur Verfügung gestellt

### trouble shooting

error: `The application app.empit.empit_lab_gps/x86_64/master requires the runtime org.gnome.Platform/x86_64/41 which was not found`

solution: `flatpak install flathub org.gnomePlatform`



#### Kürzen der Daten in elab

Die Daten, zukünftige Dataframes können durch das postprocessing Script, gekürz werden. Dafür ist die Anomalie *misc*, siehe folgende Abbildung **# 1**, zu setzen mit dem entsprechendem Keyword.

Soll der Beginn der Daten verworfen werden, ist `del_start` als misc/name zu setzen, vgl. folgende Abbildung **# 2**. Für das Kürzen am Ende der Datenmenge ist analog vorzugehen, mit dem Keyword `del_end` .



![[Kürzen_der_Daten.png]]

___

## Datenauswertungsstages

### pre-alpha- Proof of concept erbracht

- Ausreichend für einen qualitativen Eindruck

#### Pre-Eval/Live Screening

Für das pre-eval/live Screening ist auf folgende Parameter genaustens zu achten:  

- GPS 

- ACVG

- Wenn der Strom am Ende der Messung "absackt", dann Rücksprache mit Feldteamlead, ggf. überlappende Messung. 

##### Screening im Team

Das vorgehen, sollte es im Team stattfinden, ist wie folgt anzugehen:  

1. Bei unbekannten/schwierigenden Situationen, aufgrund bspw. potentiell Korrupter Daten, sollten Team Kollegen im ersten Schritte die Daten **unabhängig** voneinander sichten und bewerten, um eine Verzerrung (bias) bei der Bewertung zu verhindern.
2. Nach der separaten Beurteilung, sollten die Teamkollegen Ihre Erkenntisse abgleichen.
3. Bei bestehender Unsicherheit ist folgende Eskalationshierarchie einzuhalten
    I.  Feldteam
    II.  Bruno ?
    III.  Alex oder Albin ?
    IV.  Albin oder Alex ?

#### Korrupte Daten?

Wenn die Daten von den Features, nicht korrekt aussehen (siehe Abbildung: Korrupte Daten? 1), dann  sich vorerst das Grid anzeigen lassen (siehe Abbildung: Korrupte Daten? 2).

![[Pasted image 20220127130803.png]]
Korrupte Daten? 1

![[Pasted image 20220127130956.png]]
Korrupte Daten? 2

### alpha- Feature vollständig

- Review im Team

### beta- Integration/Zusammenspiel aller Features

- Review im Team

### final- Review außerhalb des Teams

### Das Integritätspanel

#### Korrupte Daten?

Wenn die Daten von einem features, bspw. ACVG, nicht korrekt aussehen (siehe Abbildung: Korrupte Daten? 1), dann  sich vorerst die Datenpunkte anzeigen lassen (siehe Abbildung: Korrupte Daten? 2).

![[Pasted image 20220127130803.png]]
Korrupte Daten? 1

![[Pasted image 20220127130956.png]]
Korrupte Daten? 2

### Verhalten der fit Ergebnisse in Bezug auf current, depth, lateral, offset

### Thema Verfügbarerer Strom

Verschlechterung des SNR mit steigender Frequenz, da Impendaz( wechselstrom widerstand) steigt. Hinzu kommt der Skineffekt, da der effektive Querschnitt des Stroms sich verringert, folglich fließt weniger Ampere.

ALles was mettall ist kann potentiell Spiegel sein. Je höher die Frequenz, desto undurchlässiger sind Metalle (Skineffekt weitergeführt).

Strom und Tiefe können sich kompensieren → 10 m 30 A 1 m 3 A Fitstom strom → Zähler/tiefe nenner

Zu Begin sei angemerkt, dass der Strom (current) nicht physikalisch gemessen wird, sondern mittels Gleichungssysteme zurück gerechnet wird. 

Die gesamten 

Ein Indikator für eine schlechte Datenlage ist, wenn eine hohe Korrelation  (sei es proportional oder anti-proportional) der physikalischen/geometrischen Größen vorliegt.

### Frequenzstörungen

16,67 Hz ist die freq der Bahn

50 Hz Stromnetz

### Signal-Noise-Ratio

Das Signal-Noise ratio ist das Verhältnis von induziertem Signal zu Umweltbedingten Störeinflüssen Signal/Noise. Rauschen wird durch durchstömte elektrische Leiter in der Umgebung induziert, wie bspw. die 50 Hz Frequenz durch Hochspannungsleitungen. 

Im contour plot der Wechselstrommagnetfelder der Modelle _aca-a4_ (horizontale elipsoides Wechselstrommagnetfeld) sowie _aca-a8_ (vertikal Ellipsoides Wechselstrommagnetfeld) ist Rauschen daran zu erkennen, dass keine großflächigen ergo kleinflächige Änderungen zu erkennen sind. In den folgende Abbildungen sind Integritätspanels der Abstufung _"The Good", "The Bad", "The Ugly"_ zu erkennen.

![[aca-a4_no_noise.jpg]]
Gutes SNR

![[SNR_medi.jpg]]
Mittelmäßiges SNR

![[SNR_bad.jpg]]
Schlechtes SNR

___

### Induktive Kopplung

___

### Kapazitive Kopplung

___

### ACVG

ACVG Check f → A

EIn oder zwei Kreisläufe?

Wenn ACVG, dann dip in dem linearen Verlauf 

ACVG wird über die Rover Räder bestimmt. Die ACVG Messung ist eine Technik, bei der in dem ein Potenzial in einem geerdeter geschlossener Kreislauf gemessen wird. 

Alle vier Rover Räder haben eine elektrisch Leitende Komponente. Die Bezeichnung ist `0` indiziert und   wird gegen den Uhrzeigersinn hochgezählt. Das Rad `0` ist hinten links.

Der AD Wandler hat drei Kanäle. Gemessen wird  über die folgenden Räder. 

AD Wandler 3 Kanäle 

- 0 → 1 →→ Alex

- 0 → 2

- 0 → 3 →→ Alex

___

## GIS

WGS84

Geoidseperation

## Spline

blocklength specific parameter:

- turning_point_distance
- overlap

### Troubleshooting workarounds

Wenn sich ein Splinesegment nicht öffnen lässt und der folgende o.ä. Fehler auftritt:

![[splinesegment_opening_error_traceback.jpg]]

ist der komplementär Plot zu öffnen, eine minimale Änderung zu machen, worauf hin sich die Splinekoeffizienten ändern und sich das gewünschte, zu verändernde Segment, wieder öffnen und manipulieren lässt.

Spline Key nicht in *.epr

![[Pasted image 20220204115232.png]]

## Splineoptimierungsworkaround

### HWW

Bögen ab 1°

maximale Quali.

Deadline 2 Wochen

### Astora

Termin um 14 Uhr

Bögen ab 5°
