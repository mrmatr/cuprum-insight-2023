# CuValley Hack 2023 - Zadanie 3 #
## Cuprum Insight ##

### Instrukcja wygenerowania prognozy z wykorzystaniem przeuczonego modelu ###

1. Przygotować wejściowe w pliku json. Plik powinien mieć strukturę zgodną z formatem zaprezentowanym w pliku **inference_data_template.json**. W repozytorium znajduje się również plik **inference_data.json** przygotowany zgodnie ze wzorem, który jest gotowy do wykorzystania.
2. W skrypcie **inference.py** ustawić odpowiednią ścieżkę do pliku json (zmienna data_path). Zmienna ta przyjmuje domyślną wartość `./inference_data.json`.
3. Uruchomić skrypt **inference.py**, który wysyła zapytanie do modułu inferencji oraz zwraca wynik.

### Opis plików znajdujących się w repozytorium ###

#### Skrypty .py ####

* create_json.py - Skrypt do utworzenia pliku **inference_data.json** na podstawie wybranych wierszy pliku **df_30.csv**
* elasticnet.py - Skrypt do trenowania i ewaluacji modelu Elasticnet 
* rf.py - Skrypt do trenowania i ewaluacji modelu Random Forest oraz badania istotności zmiennych (feature importance) 
* meteo_corr.py - Skrypt do badania korelacji pomiędzy stanem wody, a opadami 
* shift_raw_data.py -Skrypt do przetworzenia danych. Wejściem są pliki wejściowe (**hydro.xlsx**, **meteo.xlsx**), wyjściem plik **df_30.csv**
* imgiw_actual.py - Skrypt do pobierania aktualnych danych o stanie wody z portalu imgw
* imigw_archive.py - Skrypt do pobierania archiwalnych danych o stanie wody z portalu imgw

#### Notatniki Jupyter .ipynb ####

* darts_preds.ipynb - Notatnik Jupyter implementujący model predykcyjny w oparciu o szeregi czasowe (dane hydro **hydro.xlsx** oraz meteo **meteo.xlsx**. Architektura modelu odwzorowuje model DeepAR (https://arxiv.org/abs/1704.04110)

#### Pozostałe pliki ####

* df_30.7z - plik z danymi wejściowymi dla skryptów do trenowania modeli
* df_30_ext.7z - plik z danymi do trenowania rozszerzony o dane z wybranych pomiarów poziomu wody
* hack_imgw_2011_2021.csv - dane dodatkowe
* hydro.xlsx - plik z danymi wejściowymi
* inference_data.json - opisano powyżej
* inference_data_template.json - opisano powyżej
* meteo.xlsx - plik z danymi wejściowymi
* rf_fi.txt - istotność zmiennych (feature importance) modelu Random Forest

### Dashboard analityczny ###

 * https://apex.oracle.com/pls/apex/r/hackathon/hackathon-2023
