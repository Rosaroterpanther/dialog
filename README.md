# dialog
Dialog simple language to write game dialogs.

## Version
v0.1 (Gedankenexperiment)

## Idee
Einfache Sprache um Dialoge fuer Video Spiele zu schreiben.

Script für Sprachen verwaltung.

Schnittstellen für verschiedenen Sprachen.

## Anforderungen
1) Intuitiv zu speichern
2) einfach zu schreiben & einfach auszulesen
3) Variablen, Funktionen und Entscheidungen
4) n Teilnehmer am Dialog
5) Pausen

## Syntax
### Kommentare
```
meta version=1.0 author=Vor+Nachname

// Ich bin ein Kommentar
```

### Dialog Texte
```
"Ich bin Text der in einem Dialog angezeigt wird ..."
```

### Labels
Individuelle Sprungadressen/Abschnitte

```
label labelName:
  "Ich gehöre zu diesem label"
```

Besonderes Label kennzeichnet Ende des Dialogs
```
end
```

### Sprünge
```
goto Zeile
goto label
goto end
```

### Funktionen
```
function()
```

### Variablen
```
$ name = getName() // Write
{ name } // Read
```

### Entscheidungen
- Entscheidungen mit Textauswahl

```
choice "Text":
    goto labelTrue

choice "Anderer Text":
    goto labelFalse
```

- Entscheidungen mit Vergleichen

```
if one == two:
  "one gleich two"
elif one < two:
  "one kleiner two"
else:
  "two kleiner one"
```

### Personen / Gesprächsteilnehmer
Sprecher initalisieren

```
Person 1Name
Person 2Name+Nachname
...
Person nName
```

aktuellen Sprecher wechseln
```
speaker 1Name
```

### Pausen
```
pause seconds
```


## Beispiel
```
meta version=1.0 author=Jonas+Nachname

// Init Person
Person Emil+Manfred
Person Felix

speaker Emil+Manfred

"Hi my name is Emil!"
"How are you?"

choice "Good":
    goto Good

choice "Bad":
    goto Bad

label Good:
    speaker Felix
    "Oh that sounds good!"
    speaker Emil

label Bad:
    "Sorry uncool."

"How old are you?"

// Gets the age from the user
$ age = getAge()

if age >= 100:
    "You are the oldest person that i know.."
else:
    "Still a youg one!"

"So you are { age } Years old."
"Thats fascinating"

playFascinatingSong() // Plays a fascinating song in the Background

pause 0.5

"Well have a nice day"

end
```
