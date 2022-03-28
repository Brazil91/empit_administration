# Weekly Report KW 11

Datum: 25Mar22

## Evonik Feldeinsatz

Vom 20. März 2022 - 13:30 Uhr bis zum 23. März 2022 20:00 Uhr Einsatz in Evonik im Frankenthal als "Springer".

## Subventionierungsantragskonzept

Auf der Zugfahrt ins Frankenthal habe ich ein Subventionierungsantragkonzept erstellt.  

## KKG

> https://empit-pathfinder-kkg.herokuapp.com/
> ID: john126
> 
> PW: matrix126

1. Alle Projekte wurden geparsed und es wurden alle Splines angepasst.

2. Die Markdown Datein sind angepasst

3. Die Leitungsübersicht wurde mit *leichter Unsicherheit* ergänzt
   
   1. UJ bzw. ZW9/62 gemäß Dokumentation: Laut Dokumentation ist es eine 
      GU 300, daraus würde ich jetzt eine DN300 Grauguss Leitung ableiten. 
   
   2. ZM05 (außerhalb nördlich): Der Werkstoff ist laut Protokoll/Feldinformation (`KKW_GD_13Jan22.md`) eine DN300 duktilguss Leitung.
   
   3. Der Werkstoff der Leitung ZW8903 ist VA Stahl  
   
   4. Der Werkstoff der Leitungsgruppe `13Z001`, `13Z002`, `23Z001`  ist aufgrund des Namens der Feldcrew wahrscheinlich VE Stahl





Das Projekt ZM05_AS3 habe ich lokal gekürzt (ergo nicht aus der Datenbank, sondern lokal geparsed), aufgrund eines eingemessen Kabels ab ca. 30 % der Strecke.



Wie bei HWW sind bei den Pipelines `13Z001` und `ZW9/62` "unerwünschte"" `left_outs` vorhanden gewesen, die Händisch aus den Daten etnfernt werden müssen. Möglicherweise ist die Ursache in diesem Fall das schlechte GPS (siehe folgende Abbildung), was wahrscheinlich zu schlechten Mapping in empit_lab führt.


![](/home/empit/.var/app/com.github.marktext.marktext/config/marktext/images/2022-03-25-12-26-44-image.png)

Von der höhe der Pipeline `13Z001` wurde 0.23 m (Differenz der Mittelwerte) abgezogen. Aufgrund des sehr schlechten GPS waren die Daten nicht korrekt. Alle drei Pipelines Verlaufen gerade und parallel.



Derzeit funktioniert die Remote_db nicht bei jedem Projekt einwandfrei, Ursache unbekannt, Bruno ist im bilde.



Gösgen ist nun bei Marius im Review. Die Integritätauswertung kann bald initiiert werden.
