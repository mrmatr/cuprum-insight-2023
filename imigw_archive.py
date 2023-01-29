import os
from zipfile import ZipFile
import csv

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
#
zip_folder = r"{zip_folder}"
unzip_folder = r"{unzip_folder}"
for root, dirs, files in os.walk(zip_folder):
    for file in files:
        with ZipFile(os.path.join(zip_folder, file), 'r') as zObject:
            zObject.extractall(
                path=unzip_folder)
with open(r"{result_csv}", 'w', encoding='utf-8') as f:
    csv_writer = csv.writer(f, delimiter=';')
    csv_writer.writerow(
        ["kod_stacji", "nazwa_stacji", "nazwa_rzeki", "rok_hydrologiczny", "miesiac_roku_hydrologicznym",
         "dzien", "stan_wody", "przeplyw", "temperatura_wody", "miesiac_kalendarzowy"])
    for root, dirs, files in os.walk(unzip_folder):
        for file in files:
            with open(os.path.join(unzip_folder, file)) as f1:
                csv_reader = csv.reader(f1, delimiter=',')
                for row in csv_reader:
                    if row[1].upper() in station:
                        csv_writer.writerow(row)

