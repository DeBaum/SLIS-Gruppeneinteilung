# SLIS Gruppeneinteilung

## Projektgliederung
**data/Auswertung.csv**: Moodle-Export.
**data/out/\***: generierte Projekteinteilungen

### Student.py
Klasse, um Daten aus moodel-Export aufzunehmen.
**Student.got_prio** = Prio f�r das Projekt, dem er momentan zugewiesen ist (-1: Owner, 1..3: Prio-Wahl, 999: kein Treffer)
**Student.got_prio_str** = Text-Representation f�r Ausgabe in Datei

### run.py
Einstiegspunkt f�r Programm

### matcher/\_\_init\_\_.py
Basisklasse f�r alle Matcher-Klassen, weist initial elle Projekt-Owner ihren Projekten zu

### matcher/Optimizer.py
Wrapper f�r die anderen beiden Matcher.Klassen. Ruft zun�chst deren `create_match`-Methode auf, um danach die zu kleinen Gruppen aufzul�sen und umzuverteilen.