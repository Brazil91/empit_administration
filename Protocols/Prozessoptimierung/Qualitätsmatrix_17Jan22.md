# Wo ist der Strom? Strompfad rekonstuktion?

Schleife hohe induktivität, induktive Widerstand (geht mit der Frequenz)
Höherer Strom nicht möglich, mit derzeitigen Setup. Risko steigt mit höherer Spannung

Je höher die Frequenz, desto höhere kapazitive Verluste.

Kapazitive Kopplung, nicht nur ferromagnetische Stoffe haben einen Einfluss, bspw. hat feuchter Boden einen höheren Einfluss, als ein trockenere → Leitfähigkeit von Stoffen ist der Faktor

_Perspektivisch für das Team Datenauswertung: Metainformationen vor der Messung erheben, like:_
  
  - Wetter
  - Kreuzende Leitungen
  - Bahnschienen
  - Hochspannungsleitungen im Umfeld

Bitumen hat eine geringere isolatorische Wirkung als PE, daher wird der für uns effektive Strom in der Leitung systematisch geringer sein.

**Zweipunkt** Kontaktierung: "bananenförmige" Funktion
**Einpunkt** Kontaktiert: monoton fallend

Handlungsoption: in einem zu definierenden Radius um die Kontaktierungsstelle die Magnetfelder mappen via current mapper. Nicht zu nah an den Kontaktierungspunkten, wegen Z-Feld-Verzerrung

  	- Erwartung ist im Detail ggf. mit Bruno, Jan, Albin zu diskutieren

	- "kleine Spirale" von 10 Metern um die Kontaktierung laufen. 

An Flo: Welche Leitung, danach für mich, Leitungen im Umfeld?
___


## Qualitätsmatrix; Albins Input

Achsen: Datenqualität, Auswertungsqualität
Ziel: Es ist schnell zu verstehen was haben wir für eine Datenqualität und wie weit wollen wir Aufwandstechnsich in der Auswertung hin → Kosten/Nutzen relation

## Meeting 24Jan22

### Spline
- GPS
- local fit
	* advanced dynamic spline


### Geometry → Weight Function
- stable GPS evaluationparameter needed
- spline error → resdiual
- distance error function → 5, 6 pt
	- wie weit ist der Sensorpunkt von der approximierten Pipeline entfernt
		* je weiter entfernt, desto schlechter die Approximation der Simulationsergebnisse   

**Raw data**
1a. raw data gps quality → weight function
1b. SNR weight function

**Non Raw Data**
2. spline error function
	- local fit error /covariance matrix plotting→ uncertain → validierung an HWW (Daniel)
3. outlier detection → isolated forest algorithm (clustering; Ausreißer)

Wish for pre-alpha: 1a + 1b → correlation with fit results →→ indicator for evaluation →→→ additional outlier team data eval team



resudials:  normalization → residual_pipe_fitter + spline_residuals 

minimal SNR = 10 (if insides/knowledge over domain < 10 possible); Noise = ambient + sensor noise

backward propagation from spline to fit results (dev of Albin); new category of data

Montecarlo experiment (DoE) → brute force → unknown parameter

#### First part, development of: 
I 1a. raw data quality (1a) weight function → normalization
II 1b. SNR weight function
III Spline error (2) weight function → normalization
	- covariance matrix of fit results → cmin?
	- 	* xarray (data format, multidimensional) → @property
IV outlier detection → isolated forest algorithm (clustering; Ausreißer)

Timeframe: 2 Weeks?
	 – _ACVG functions defect_ 1 day planning + 2 days of development


### Integrity 

to be continued...

## gasnat



