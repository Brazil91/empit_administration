# Weekly Report KW 10

Datum: 11Mar22

## HWW

- ETRS und DHHN2016 Implementation in `postprocessing_v2.py`
  * DHHN2016 "web scraper" Optimierung (every tenth row except first and last pull of heigth and geosep)
  * itertuple instead of iterrows
- Abgabe des Zwischenreports

## Ontras lecture-app

- fix des Projektlängenfilter bug (Faktor 10)

## Ontras

- Arbeitsvorbereitung: "Optimale" Zusammenstellung von L und G Plänen 
  * alternierend G und L Pläne 
  * `FGL_101_GL_merged__DL_03Mar22.zip`
  * 
- Korrelation der Projekte mit der Dokumentation `G_L_plan_elab_correlation_DL.ods`
- Iteration #1 der der Manager ... abgeschlossen
  * `Ontras_Oct21_FGL_102_mngr_2_projects`
  * `Ontras_Oct21_FGL_102_mngr_3_projects`

## Field Truck Mapping via Richys Script

- Berechnung/Mapping hat theoretisch funktioniert, doch die lokale postgres DB ist nicht Korrekt eingerichtet, daher gescheitert
  * __Notwendig:__
    + Mergen der Repos von Bruno und Richy, damit die lokale Datenbank die richtige Struktur hat
    + Im Anschluss lokale DB neu einrichten
