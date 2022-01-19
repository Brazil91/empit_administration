# KKW pre-validation 

## Kontaktierungs Template

> ##### Kontaktierung
> **long**
> lat: 
> lon: 
> Ellipsoide Höhe:  
> Orthometrische Höhe: 
>
> **short**
> lat:  
> lon: 
> Ellipsoide Höhe:  
> Orthometrische Höhe: 

## KKG_Gösgen/UJ_AS_2/2022-01-12_0

Nicht auswertbar, falsches GPS Setup. (Teilmenge von 2022-01-12_1).
 
## KKG_Gösgen/UJ_AS_2/2022-01-12_1 

### Evaluation

Das zweite produktiv Projekt _KKG_Gösgen/UJ_AS_2/2022-01-12_1_ ist auswertbar sowie vollständig.

Die tiefen Frequenzen sind z.T. gut auswertbar, doch nicht auswertbare Daten sind zu erkennen und zukünftig absehbar, siehe Abbildung. Die Güte ist vergleichbar von denen eines Stadtprojekts.

Die tiefen Frequenzen zeigen eine akzeptable Konstanz auf. Die Geometrie werden wir nicht, Albins Worte "Zentimeter genau", bestimmen können. Die Integritätssimulation wird vorraussichtlich in weiten Teilen entwertet werden müssen, da Stöungen global (Strecke) und nicht lokal (Messpunkte) sind. Das signal-noise ratio sieht sehr gut aus.

Das GPS Signal ist gut.

![[Pasted image 20220113145101.png]]

## KKG_Gösgen/UJ_AS_2/2022-01-13_0 

**Verbesserungsvorschlag an Flo**: GIS informationen der Kontaktierungspunkte (zukünftig cp) dokumentieren und übermitteln.

### Feldinformationen

> EMPIT field: project start: 2022-01-13T11:30:40.062426+00:00
> UJ_AS_1, DN300, GU
>
> ##### Kontaktierung
> **long**
> lat: 47.3666582
> lon: 7.96717832
> Ellipsoide Höhe: 462.324 m 
> Orthometrische Höhe: 416.657 m
>
> **short**
> lat: 47.36628196 
> lon: 7.96777941
> Ellipsoide Höhe: 439.384 m 
> Orthometrische Höhe: 393.718 m
>
> 1kt short, 100m, Schieber S202
> 2kt long, 200m, Pipeline UJ 55 via Schacht
> 
> R eingeschleift: 2,5 Ohm
> Gesamt R: 4 Ohm
> PK: 8 A
> 
> Asphaltiert, Start an Schacht bei long

**Physikalisch gemessene Höhe: 1.7 m**

Schlechteres Setting als am 12.01.22, da Kreuzende Löschwasserleieenm Anfangg. Nach halber strecke verliert sich die Leitung. Nach einem Abschnitt ist die Leitung wieder Messbar, jedoch sehr nah an einer Häuserwand, daher potenziell schlechtes GPS.

Drei Leitungen nebeneinander, kreuzende Löschwasserleitung zu Beginn.

## KKG_Gösgen/KKG_Gösgen/2022-01-15_0



### Feldinformationen

> EMPIT field: project start: 2022-01-15T11:04:23.186683+00:00
> 
> KKG-Gösgen
> 
> ZM05_AS1
> 
> ##### Kontaktierung
> **long**
> lat: 47.37279691
> lon: 7.97212811
> Ellipsoide Höhe: 503.630 m  
> Orthometrische Höhe: 457.967 m
>
> **short**
> lat: 47.36958647
> lon: 7.96906323
> Ellipsoide Höhe: 442.083 m  
> Orthometrische Höhe: 396.415 m
>
> 1kt short, 50m, Schieber ZW9703
> 2kt long, 610m, Schieber ZW 9702
> 
> R eingeschleift: 0 Ohm
> Gesamt R: 4,8 Ohm
> PK: 7A
> 
> asphaltierte Straße, freier Himmel (gutes GPS)




### Evaluation 17Jan22

Der Datensatz vom 15.01.22 sieht aus meiner Sicht nicht schlecht aus. Das SNR (Signal-Rausch-Verhältnis) sieht gut aus.Was mich etwas beunruhigt ist, dass Ihr 7 A rein gebt und die niedrigen Frequenzen mit 2.5 A startet der Verlauf des Stromes sinkt und ab ca. em 40 auf 1.9 A konstant bleibt, vgl. folgende Abbildung. 

![[KKW_GD_ZM05_AS1_fit_results.jpg]]

Der Verlauf des Stromes korreliert mit der tiefe, daher ist natürlich aus meiner Sicht die Frage wie damit umzugehen ist, habt ihr referenz tiefenmessungen mit nem Zollstock o.ä. machen können? Die Tiefe beginnt bei -2.2 steigt auf -1.3 und fällt/sinkt relativ sanft auf ca. -1.45, verhältnismäßig konstant.

In der folgenden Abbildung ist der 6 Hz Spline in XY der Frequenz des Index 1 zu erkennen.

![[KKW_GD_ZM05_AS1_xy_spline_6Hz.jpg]]

Die dritte Abbildung ist der 6 HZ Spline (approximierte Pipeline) Höhenplot. 

![[KKW_GD_ZM05_AS1_altitude_spline_6Hz.jpg]]


## KKG_Gösgen/KKG_Gösgen/ZM05_AS3/2022-01-17_0

### Feldinformation

Doc 1.6 bis 2 m

Wahrscheinlich Stromkabeleingemessen, tiefe

Nach, F2 wahrscheinlich 12 Hz, nur DoC 1 m



## Samstag

duktilguß Leitung 300

UJ ZM05

angeschlossen schieber und schacht

paar meter richtung long

tal richtung Berg

Bei long ist analog nachmessbar


Bitumen anstrich überall




laptop

keine nvidia graka

aktuelle oder aktuell -1 Intel Generation Prozessoren


Stromquellen Daten, Empit_field Daten Zusammenführen

perspektivisch automatisiert auf dem Server (daemon)



Spline Gradient

nehmen Pipeline als gegeben an → kontrolle des gegebenen spline/gps 
