
import pandas as pd
dfh = pd.read_csv('hack_imgw_2011_2021.csv', sep=';')





def get_date_from_hydro(row):
    yh=row['rok_hydrologiczny']
    mh = row['miesiac_roku_hydrologicznym']
    if mh < 3:
        yy = yh -1
        mm = mh + 10
    else:
        yy = yh
        mm = mh - 2
    dd = row['dzien']
    return datetime.date(yy, mm, dd)





dfh['data'] = dfh.apply(lambda x: get_date_from_hydro (x), axis = 1)

