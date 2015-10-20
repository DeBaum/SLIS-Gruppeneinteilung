# SLIS Gruppeneinteilung

## Projektgliederung
**data/Auswertung.csv**: Moodle-Export.
**data/out/\***: generierte Projekteinteilungen

### Student.py
Klasse, um Daten aus moodel-Export aufzunehmen.
**Student.got_prio** = Prio für das Projekt, dem er momentan zugewiesen ist (-1: Owner, 1..3: Prio-Wahl, 999: kein Treffer)
**Student.got_prio_str** = Text-Representation für Ausgabe in Datei

### run.py
Einstiegspunkt für Programm

### matcher/\_\_init\_\_.py
Basisklasse für alle Matcher-Klassen, weist initial elle Projekt-Owner ihren Projekten zu

### matcher/Optimizer.py
Wrapper für die anderen beiden Matcher.Klassen. Ruft zunächst deren `create_match`-Methode auf, um danach die zu kleinen Gruppen aufzulösen und umzuverteilen.