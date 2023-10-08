import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd
import adafruit_dht
import RPi.GPIO as GPIO
import sqlite3

# LCD Pin-Konfiguration
lcd_rs = digitalio.DigitalInOut(board.D4)
lcd_en = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D18)
lcd_d5 = digitalio.DigitalInOut(board.D22)
lcd_d6 = digitalio.DigitalInOut(board.D23)
lcd_d7 = digitalio.DigitalInOut(board.D24)

# LCD-Spalten und -Zeilen
lcd_columns = 16
lcd_rows = 2

# LCD initialisieren
lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

# DHT11 Sensor initialisieren
dhtDevice = adafruit_dht.DHT11(board.D13)

# HC-SR04 Sensor initialisieren
TRIG = 27
ECHO = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Buzzer initialisieren
BUZZER = 12
GPIO.setup(BUZZER, GPIO.OUT)

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('sensor_data.db')
c = conn.cursor()

# Tabelle erstellen, falls sie noch nicht existiert
c.execute('''
          CREATE TABLE IF NOT EXISTS sensor_data
          (timestamp INTEGER, temperature REAL, humidity REAL, distance REAL)
          ''')

def save_data_to_db(timestamp, temperature, humidity, distance):
    c.execute('''
              INSERT INTO sensor_data (timestamp, temperature, humidity, distance)
              VALUES (?, ?, ?, ?)
              ''', (timestamp, temperature, humidity, distance))
    conn.commit()

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start_time = time.time()
    end_time = time.time()

    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    distance = (end_time - start_time) * 34300 / 2
    return distance

try:
    while True:
        try:
            humidity = dhtDevice.humidity
            temperature = dhtDevice.temperature
            distance = get_distance()

            # Zeitstempel
            timestamp = int(time.time())

            lcd.clear()
            lcd.message = f"Temp: {temperature:.1f}C\nHumidity: {humidity:.1f}%"

            if humidity < 40 or temperature > 30 or distance < 20:
                lcd.clear()
                lcd.message = "ALARM"
                GPIO.output(BUZZER, GPIO.HIGH)
            else:
                GPIO.output(BUZZER, GPIO.LOW)

            # Daten in die Datenbank speichern
            save_data_to_db(timestamp, temperature, humidity, distance)

            time.sleep(1)

        except RuntimeError as e:
            print(f" Es gab einen Fehler bei einer der Messungen. Setze Programm fort.: {e}")
            # Das Programm wird trotz des Fehlers fortgesetzt.

except KeyboardInterrupt:
    GPIO.cleanup()
    conn.close()
    print("Programm beendet.")
