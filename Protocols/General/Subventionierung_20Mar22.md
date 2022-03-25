# Subventionierungsantrag

## Projekttitel

Entwicklung eines Parsers zur automatischen Datengütevorvalidierung bei der Messung mittels autonomer fliegenden Drohne


## Projektbeschreibung

Das Ziel des Projekts ist die Entwicklung eines Parsers, zur automatischen "live" Validierung der Datenqualität bei der Nutzung der autonom fliegenden Drohne. 

Eine Herausforderung für die Auswertung, der  mittels des CMI Messsystems aufgenommenen Daten, ist das Sicherstellen einer hinreichenden Datenqualität. Um die Effizienz der Prozesskette von Drohnen Projekten zu optimieren, soll ein automatischer Parser entwickelt werden, um Totzeiten zu verringern, bis eine schlechte Datengüte identifiziert wird, die eine erneute Einmessung des jeweiligen Rohrleitungssystems erfordert. Der Parser soll mit dem Flugalgortihmus gekoppelt sein, um auf dass Messverhalten Einfluß zu nehmen. 


### Strombasierte Daten

Eine Metrik zur Validierung der Güte der strombasierten Daten ist das Signal zu Rauschen Verhältniss. Wird ein Grenzwert überschritten, soll der Parser zeitnah Feedback geben, wodurch eine Anpassung der Konfiguration erfolgen kann. 

Eine weitere Funktionalität des Parser sollte sein, zu jedem zurückgerechneten Strom den ausgegebeben Strom zu "mappen". Anhand dieser Daten soll zukünftig ein Optimierer geschrieben werden, wordurch alle Strombasierte Funktionen optimiert werden. 

### Ortsbasierte Daten

Neben Funktionen, welche eine Funktion des Stroms sind, ist das GPS Signal eine essentielle Einflussgröße. Der Parser soll die Güte der GPS Information in relation zu den vorhandenen Messpunkten validieren. Wenn ein Datenpunkt nicht ins Spektrum der bereits vorhandenen Daten passt, soll die Drohne sofort veranlasst werden, den Datenpunkt erneut aufzunehmen. Die Dauer ein besseres Signal zu detektieren soll frei konfigurierbar sein. 

Des Weiteren werden erfahrungsgemäß ungewollt mehrfach Datenpunkte aufgenommen, bspw. aufgrund des autonomen Flugalgorithmus der Drohne.

Daraus folgt, dass des Parser bei mehrfachem vorhandensein von Datenpunkten zu einem Ort, den besten Datenpunkt anhand einer Bewertungsmatrix selektiert, welche im Rahmen des Projekts zu entwickeln ist.

Bei vorhandener Leitungsdokumentation, könnte eine Abgleich der zurükgelegten Strecke anhand der Dokumentation erfolgen. Bspw. könnten fehlerhafte Drifts bei Start und Ende Pipeline, bedingt durch das Einmessen des Rückleiters, zeitnah detektiert und korrigiert werden.

## Arbeitspakete

- Erstellen einer Bewertungsmatrix
- Empirische Ermittlung von Grenzwerten
- Entwicklung eines Stromsimulationswerte-/Stromquellendatenmapperi
- Entwicklung eines algorithmus, welcher
  * die Bewertungsmatrix nutzt und einen Messpunkt erneut aufnimmt, sollte der vorhandene Datenpunkt nicht hinreichend sein
  * den besten Musspunkt auswählt auf Grundlage der Bewertungsmatrix
- Ist-/Soll Vergleich, an definierten Orten, mit der Eingespeisten Leitungsdokumentation

## Benötigtes akademsiches Wissen

allgm. Ingenieurswissen, machine Learning, Neumann-Moore-Nachbarschaft, regressionsanalyse 

## Studienrichtung

Ingenieurswissenschaftlicher Studiengang

## Studienschwerpunkte

- Process Engineering 
- Big Data
- Digitalisierung im Rahmen von I4.0
