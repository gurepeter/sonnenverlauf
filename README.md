# Sonnenverlauf
## Voraussetzung
Voraussetzung ist die Bibliotheke pysolar.solar
## Einstellungen
GPS-Koordinaten Gureweg 1
* latitude = 46.655997
* longitude = 13.756257
* filter_is_off = False
* filter_altitude = 5 # bei einem Sonnenstand groesser von x Grad
* filter_uhrzeit = 14 # alle Werte ab xx Uhr (z.B. Nachmittag)
* stunden_intervall = 1 # alle x Stunden Werte auslesen - 1 .. jede Stunde - 0.5 jede 1/2 Stunde

das ganze Jahr:
* startdatum = datetime.datetime(2023, 1, 1, 7, 0, 0, tzinfo=pytz.timezone('CET')) # Etc/GMT+1
* enddatum   = datetime.datetime(2023, 12, 31, 20, 0, 0, tzinfo=pytz.timezone('CET'))

 
