import pandas as pd
# Testowa ścieżka C:/Users/Janusz/Desktop/projekty/bazy dnaych/Fin_Dis.csv

while True:
    try:
        print("Info: This program is only support csv files. Use this simbol '/' during declare a path. ")
        data_input = input("Please enter the file path:")
        the_data = pd.read_csv(data_input)
        print("Proces is finished. Data have been loaded correctly.")
        break
    except Exception:
        print("Your path is not correct. Pleace try again.")


