import csv

import requests

station = ["CHAŁUPKI",
           "OLZA",
           "KRZYŻANOWICE",
           "RACIBÓRZ-MIEDONIA",
           "RACIBÓRZ MIEDONIA",
           "KOŹLE",
           "KRAPKOWICE",
           "OPOLE-GROSZOWICE",
           "UJŚCIE NYSY KŁODZKIEJ",
           "BRZEG",
           "OŁAWA",
           "BRZEG DOLNY",
           "MALCZYCE",
           "ŚCINAWA", "OSETNO",
           "NYSA",
           "MIETKÓW",
           "TURAWA",
           "RYBNIK-STODOŁY",
           "RYBNIK STODOŁY",
           "PYSKOWICE-DZIERŻNO",
           "PYSKOWICE DZIERŻNO"
           ]
link = "https://danepubliczne.imgw.pl/api/data/hydro/"
result = requests.get(link).json()
with open(r"actual_data_csv", 'w', encoding='utf-8') as f:
    csv_writer = csv.writer(f, delimiter=';')
    csv_writer.writerow(
        ["kod_stacji", "nazwa_stacji", "nazwa_rzeki", "data", "stan_wody"])
    for r in result:
        if r["stacja"].upper() in station:
            csv_writer.writerow(
                [r["id_stacji"], r["stacja"], r['rzeka'], r['stan_wody_data_pomiaru'].split(' ')[0], r["stan_wody"], ])
