## Hydroalert - Schulprojekt ITECH BS14: Kostenbewusste Überflutungserkennung mit Hitzewarnsystem für Entwicklungsländer"

Hydroalert ist ein Schulprojekt, das Umweltparameter in Echtzeit überwacht. Es verwendet einen Raspberry Pi, um Daten von Sensoren zu lesen und über eine Webanwendung darzustellen.

## Funktionen

- Echtzeitüberwachung von Temperatur, Luftfeuchtigkeit und Abstand
- Webanwendung zur Anzeige der Daten
- Alarmfunktion bei kritischen Bedingungen


## Fritzing Diagramm
![alert_Steckplatine](https://github.com/LionC0dingZion/Hydroalert/assets/142108023/76ee24a7-649d-46c5-b2c4-da05c60d8e99)


## Hauptkomponenten

- **Raspberry Pi:** Steuert den Datenfluss und betreibt den Webserver.
- **DHT11 Sensor:** Misst Temperatur und Luftfeuchtigkeit.
- **HC-SR04 Ultraschallsensor:** Ermöglicht die Abstandsmessung zum Wasser.
- **Buzzer:** Löst einen Alarm aus.
- **Character-LCD-Anzeige:** Zeigt die aktuelle Temperatur und Luftfeuchtigkeit an. Im Falle eines ausgelösten Alarms zeigt das Display zudem eine entsprechende Warnung an.

## Ablauf:

1. **Bibliotheken importieren:** Zuerst werden die benötigten Bibliotheken importiert, darunter Zeitfunktionen, GPIO-Bibliotheken für die Raspberry Pi Pins, Adafruit-Bibliotheken für das LCD und den DHT11-Sensor, sowie sqlite3 für die Datenbankoperationen.

2. **Hardware initialisieren:** Hier werden die Pins für das LCD, den DHT11, den HC-SR04 und den Buzzer konfiguriert.

3. **LCD-Konfiguration:** Es wird festgelegt, wie das LCD an die Pins angeschlossen ist und wie viele Spalten und Zeilen es hat.

4. **Datenbank initialisieren:** Es wird eine Verbindung zur SQLite-Datenbank 'sensor_data.db' hergestellt und ein Cursor erstellt.

5. **Tabelle erstellen:** Es wird eine Tabelle namens 'sensor_data' erstellt, falls sie noch nicht existiert, mit den Spalten 'timestamp', 'temperature', 'humidity' und 'distance'.

6. **Funktion zum Speichern von Daten:** Es wird eine Funktion `save_data_to_db` definiert, die Daten in die Datenbank einfügt.

7. **Funktion zum Messen der Entfernung:** Die Funktion `get_distance` verwendet den HC-SR04, um die Entfernung zu messen.

8. **Hauptschleife:** Hier beginnt die Hauptausführungsschleife, die für die Datenaufzeichnung zuständig ist.
    - a. Es werden Temperatur, Luftfeuchtigkeit und Entfernung gemessen.
    - b. Ein Zeitstempel wird erstellt.
    - c. Die LCD-Anzeige wird aktualisiert, um die gemessenen Werte anzuzeigen.
    - d. Wenn bestimmte Bedingungen (Luftfeuchtigkeit < 40, Temperatur > 30 oder Entfernung < 20) erfüllt sind, wird ein Alarm auf dem LCD angezeigt und ein Buzzer aktiviert. Andernfalls wird der Buzzer deaktiviert.
    - e. Die gemessenen Daten werden in die Datenbank gespeichert.
    - f. Es wird eine Sekunde gewartet, bevor der nächste Messzyklus beginnt.

9. **Abfangen von KeyboardInterrupt (Strg+C):** Wenn der Benutzer das Programm beendet, werden die GPIO-Pins aufgeräumt, die Datenbankverbindung geschlossen und eine Abschlussnachricht ausgegeben.


## Webanwendung mit Flask

Die Webanwendung wird mit Flask, einem Python-Webframework, betrieben. Sie visualisiert die Daten in Echtzeit und ermöglicht Benutzern, den Zustand zu überwachen.

## Anwendung starten und nutzen

1. Führen Sie `python alarm.py` aus, um den Alarm scharf zu stellen .
2. Führen Sie `python app.py` aus, um den Webserver zu starten.
3. Geben Sie im Webbrowser die individuelle IP-Adresse Ihres Raspberry Pi ein, um das Webinterface zu erreichen. Diese Adresse lautet normalerweise `192.168.1.100:5000`
   Beachten Sie, dass die angegebene IP-Adresse individuell ist. 

## Projektnutzen

Hydroalert demonstriert den praktischen Einsatz von Technologie in der Umweltüberwachung und fördert das Verständnis für Umweltbedingungen.

*Hinweis: Dieses Projekt wird im Rahmen eines schulischen Bildungsprogramms entwickelt und hat keinen kommerziellen Hintergrund.*
