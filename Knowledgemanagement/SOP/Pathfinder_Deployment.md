# Pathfinder Deployment

## Data integration

Die Daten aus dem post_processing sind in die pathfinder app wie folgt zu integrieren:
 `/home/empit/Documents/empit_git_env/empit-pathfinder-dev/projects/<customer>/data/inspections`

## inspection.configuration

Um die Daten dem Backend zur Verfügung zu stellen, benötigt das backend die Referenz, welche sich in der `inspection.configuration` befindet.

Dafür ist dass Script `inspection_config_parser_v1.py` (zshconfig alias = iconfig) auszuführen. Dem "zsh wizard" ist den inspection Datei Pfad zu übergeben (bspw. `/home/empit/Documents/empit_git_env/empit-pathfinder-dev/projects/dev_feature_testing/data/inspections/RMR-033_inspection.csv`).

> Anmerkung:
> Für das contact points feature (Marius ist im Bilde) und dass kommende image_table_feature sind der config (siehe folgendes Beispiel) weitere keys hinzuzufügen.

> inspection:
>   RMR-033: {
>     label: 'RMR-033',
>     export_file: './inspections/RMR-033_inspection.csv',
>     street_file: './streets/RMR-033_street.csv',
>     campaign: 'Select all',
>     }

## columns.configuration

Die Columns der *_inspection.csv sowie die columns aus der `columns.configuration` müssen für alle Files identisch sein (sofern `require_active_columns: true`; es wird `true` empfohlen)

## feature.configuration

> inspection_features:
>   available:
>     [...]
>   active:
>     [
>       "doc",
>     ]
  enabled: ["pipeline_poles"]

Die für den Kunden erwünschte Features sind in der `feature.configuration` unter `active` einzutragen. Die Features, die beim launching der App enabled sein sollen sind in die Liste unter dem Key `enabled: []` hinzuzufügen.


## feature_section.configuration

Features die von den default features, die in der `default_feature.configuration` aufgelistet sind, abweichen, müssen in die `default_feature.configuration` übertragen und dort modifiziert werden. Das kann notwendig sein, wenn sich bspw. das _Wording_ vom default unterscheiden soll.


## map.configuration

In dieser config sind allgm. wordings (sowie pipeline polyline parameter; sind Standards die **nicht** zu ändern sind/sein sollten), idR. sind hier keine Änderungen vorzunehmen.


## plots.configuration

In dieser config sind alle plot spezifischen configs anzupassen. 


## text_and_table.configuration

In dieser Config sind ebenfalls wording configs.


