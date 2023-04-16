# Sonnenverlauf

## Voraussetzung
Python 3.x
Voraussetzung ist die Bibliotheke pysolar.solar
## Links
* [https://www.sunearthtools.com](https://www.sunearthtools.com/dp/tools/pos_sun.php)
* [Link zum Pythonscript sonnverlauf.py](src/sonnenstand.csv)
* [Link zum Ergebnis sonnenstand.csv](src/sonnenstand.csv)

## Einstellungen
GPS-Koordinaten Gureweg 1
* latitude = 46.655997
* longitude = 13.756257
Filtereinstellungen
* filter_is_off = False
* filter_altitude = 5 # bei einem Sonnenstand groesser von x Grad
* filter_uhrzeit = 14 # alle Werte ab xx Uhr (z.B. Nachmittag)
Intervall
* stunden_intervall = 1 # alle x Stunden Werte auslesen - 1 .. jede Stunde - 0.5 jede 1/2 Stunde

Zeitraum: das ganze Jahr
* startdatum = datetime.datetime(2023, 1, 1, 7, 0, 0, tzinfo=pytz.timezone('CET')) # Etc/GMT+1
* enddatum   = datetime.datetime(2023, 12, 31, 20, 0, 0, tzinfo=pytz.timezone('CET'))

## Ergebnis
Eine Datei sonnenstand.csv wird mit 4 Spalten erzeugt
* 1.Spalte: **index**    - laufende Nummer
* 2.Spalte: **datum**    - Datum mit Uhrzeit
* 3.Spalte: **altitude** - Sonnenstand in Grad zur Erde
* 4.Spalte: **azimuth**  - Horizontalwinkel in Grad 0° ist Norden - 90° Osten - 180° Süden - 225° Westen
* 5.Spalte: **schatten** - bei einem Objekt mit einer Hoehe von 1m


 
