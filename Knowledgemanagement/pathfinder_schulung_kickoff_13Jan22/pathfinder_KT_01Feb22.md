# DASH

Vereinigung von wrapper bzw. kombination von diversen frameworks wie leaflet, flask, react, html, css

- `html → html_component` korrespondieren zu html tags
- `dcc → dash core component` korrespondieren zu interaktive Komponenten 
- `dbc → dash_bootstap_component` korrespondieren zu css bootstrap Komponenten (viel js)
- https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/
- dbc.card descriptio, disclaimer, `pipeline_overview`
- dbc.tab ist das css objekt Registerkarte
  - Daraus folgt tab hat cards inhärent 

## flask
"Flask ist für den webtraffic zuständig. Er verpackt sie in html request."

## html
- head
  - css links/files
  - title
  - %meta% → autor der website, tags für Suchmaschinen, favicon (mini empit icon im tab)
- body
  - enthält den content
- footer
  - impressum
  - js.files (sinnvoller am Ende, damit die Seite sauber lädt) 
  - ...

## css bibliothek
  - bootstrap css → style baukasten, bekannt
    - empit pathfinder → LUX von bootstrap
  - css Klasse in pathfinder `className` (ist ein Attribut von dash Komponenten, die Gerendered werden) 
  - betrifft den server nicht, d.h. das Neustarten des browsers ist hinreichend, da er die css links aufruft und nicht der server (python/flask)

leaflet und react sind javascript librarys

## leaflet (Repräsentativ für js) 
- map framework/library
- javascript library
- in dash/pathfinder `dl`
  - benutzt react komponenten
    - bsp. der fullscreen mode in eine javascript komponente, die in leaflet react als button zur verfügung gestellt wird um die methhode ohne  javascript verfügbar zu machen
    -
