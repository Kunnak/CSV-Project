# CSV-Project
Erstellen von CSV-Dateien für Nicknamen, Backups, Highscores [für mein PianoTiles]

- main.py - Hauptdatei
- welcome.py - Eingabe Nickname
- files.py - CSV-Dateien
- functions.py - Funktionsbibliothek
- game.py - Spielablauf

- nicknames.csv - CSV-Datei für die Speicherung aller Nicknames
- highscore.csv - CSV-Datei für die Speicherung aller erreichten Punkte

Das Programm fragt den User nach seinem Nicknamen ab und speichert diesen in eine CSV-Datei.
Anschließend wird ein Backup von dieser CSV-Datei erstellt, sollte dieser Username noch nicht
existieren. Sollte der Username bereits vorhanden sein, wird kein neuer Eintrag in der CSV-Datei
erstellt. Sollte die Datei der Nicknamen verändert, oder ein Backup angestoßen worden sein,
werden diese Aktivitäten in einer logfile-Datei gespeichert. Genauso wird ein Eintrag erstellt,
wenn ein vorhandener Spieler das Spiel startet.

Das Spiel selbst, ist ein Replikat von dem Handy Spiel "Piano Tiles".
Der Spieler bekommt ein Fenster geöffnet, auf dem Klaviertasten vom oberen Bildschirmrand zum
unteren fallen. Aufgabe des Spielers ist es mit Hilfe der linken Maustaste die fallenden Tasten,
bevor sie den boden erreichen zu zerstören.
Für jede zerstörte Taste bekommt der Spieler 1 Punkt. Ebenso wird für jede Taste die zerstört
wird, die geschwindigkeit der Tasten erhöht.

Der Spieler startet mit 3 Leben. Für jede Taste, die den Boden erreicht, wird ein Leben abge-
zogen. Sollte der Spieler kein Leben mehr zur Verfügung haben, wird das Spiel beendet und die
erreichten Punkte werden ausgegeben sowie die 10 besten Highscores die erreicht worden sind.

Mehr später..
