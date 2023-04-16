'''
Created on 11.04.2023

@author: Santner Peter

Gureweg 1: 46.655997, 13.756257
Alle Details unter: https://github.com/gurepeter/sonnenverlauf#readme

'''

from pysolar.solar import get_altitude, get_azimuth
import datetime
import pytz
import pandas as pd

def datespan(startDate, endDate, delta=datetime.timedelta(days=1)):
    currentDate = startDate
    while currentDate < endDate:
        yield currentDate
        currentDate += delta


def sonnenstand(date):
    import math 
    sun_result = {}
    hoehe = 1 # 1m Hoch = Gegenkathede
    altitude = get_altitude(latitude, longitude, date)
    azimuth = get_azimuth(latitude, longitude, date)
    date_new = date.strftime('%Y.%m.%d %H:%M %z %Z')
    print("{}\t{}\t{}\t{}".format(date, date_new, altitude, azimuth))
    sun_result['datum']     = date
    sun_result['altitude']  = altitude
    sun_result['azimuth']   = azimuth
    sun_result['schatten']  = hoehe / math.tan(altitude * math.pi / 180) 
    # sun_result['stunde']    = date.hour
    # sun_result['offset']    = date.tzinfo.dst(date)
    # sun_result['stunde_string'] = date.strftime('%H %Z')
    return sun_result


def sonnenstand_ueber_zeitbereich():
    pd_sun_list = pd.DataFrame(columns=['datum', 'altitude', 'azimuth'])

    print (pd_sun_list)
    for day in datespan(startdatum, enddatum, delta=datetime.timedelta(hours=stunden_intervall)):
        sun_result = sonnenstand(day)
#        df = pd.DataFrame()
#        df.append(sun_result,ignore_index=True)
#        sun_result['Hour']= df['datum'].hour
        if (sun_result['altitude'] > filter_altitude and day.hour > filter_uhrzeit) or filter_is_off:
            pd_sun_list = pd_sun_list.append(sun_result, ignore_index=True)
    print (pd_sun_list)
    pd_sun_list.info()
    pd_sun_list.to_csv("sonnenstand.csv", decimal=",")
    
    
    
if __name__ == '__main__':
    
    # GPS-Koordinaten Gureweg 1
    latitude = 46.655997 # 42.206
    longitude = 13.756257 # -71.382
    filter_is_off = False
    filter_altitude = 5 # bei einem Sonnenstand groesser von x Grad
    filter_uhrzeit = 14 # alle Werte ab xx Uhr (z.B. Nachmittag)
    stunden_intervall = 1 # alle x Stunden Werte auslesen - 1 .. jede Stunde - 0.5 jede 1/2 Stunde
    # das ganze Jahr:
    startdatum = datetime.datetime(2023, 1, 1, 7, 0, 0, tzinfo=pytz.timezone('CET'))
    enddatum   = datetime.datetime(2023, 12, 31, 20, 0, 0, tzinfo=pytz.timezone('CET'))
    # am 6. April:
    #startdatum = datetime.datetime(2023, 4, 6, 14, 0, 0, tzinfo=pytz.timezone('CET'))
    #enddatum   = datetime.datetime(2023, 4, 6, 20, 0, 0, tzinfo=pytz.timezone('CET'))

    print("Altitude und Azimuth vom Gureweg 1 ({} {}) von {} bis {}".format(latitude, longitude, startdatum, enddatum ))
    sonnenstand_ueber_zeitbereich()
    
    