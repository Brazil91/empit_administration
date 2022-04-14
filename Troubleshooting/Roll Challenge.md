# Roll Challenge

## current_mapper_1 (current_mapper_2021_5_mag13)

Eine Herausforderung bei dieser Problematik ist, dass es unbekannt ist welcher Track der Richtige ist. Bspw. könnte ein "stark" oszillierender Track dennoch die Pipeline approximieren, als einer der geringe oszillationen aufweist, siehe Folgene Abbildung. Wie der Verlauf geartet ist, ist eine Funktion der dynamic des Inspizierendend, also wie der Bewegungsablauf der Person ist.

![[Pasted image 20220412110829.png]]

Das korrektur Script (calculate_roll-corrected_spline.py) verringert per definition den Abstand von Referenz- und Testtrack, daher ist notwendig "sicher" zu sein, ob der lateral Offset eine Funktion des Winkelfehlers (roll error) ist oder nicht.

Unter der Annahme, dass das GPS gut ist also fix (schlechtes GPS gleich float; es gibt noch mehr) aufweist, gilt folgendes: Wenn eine generelle Konstanz des lateral offsets zu erkennen ist, auch bei Änderungen der pipe depth, ist ein roll error unwahrscheinlich und ist von der Korrektur abzuraten. 

Bei guten GPS ist ein lateral offset von bis zu 5 cm zu erwarten.