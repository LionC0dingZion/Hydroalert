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
