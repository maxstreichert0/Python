



def insert_line_at_five(file_path, new_line):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Stelle sicher, dass die Liste lang genug ist. Falls nicht, füge leere Zeilen hinzu.
    while len(lines) < 4:
        lines.append('\n')

    # Füge die neue Zeile bei Index 4 ein, was der fünften Zeile entspricht.
    lines.insert(4, new_line + '\n')
    with open(file_path, 'w') as file:
        file.writelines(lines)









def filter_lines(file_path):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    flines = filter(lambda x: len(x) > 10 , lines)
    flines = list(flines)

    print(flines)
    with open(file_path, 'w') as file:
        file.writelines(flines)







# Schreibe binäre Daten in eine Datei
st = "test"
st.encode()
file = open('beispiel.dat', 'wb')

bytes_to_write = bytes([1,2,3,4,5,6,7,8,9])  # Eine Liste von Bytes

file.write(bytes_to_write)

filter_lines("data.txt")












# Pfad zur Datei
file_path = 'data.txt'
# Neue Zeile, die eingefügt werden soll
new_line = 'Dies ist die neue fünfte Zeile.'

# Führe die Funktion aus
insert_line_at_five(file_path, new_line)
# Definiere eine Liste von Zahlen
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Definiere eine Funktion, die überprüft, ob eine Zahl gerade ist
def ist_gerade(zahl):
    return zahl % 2 == 0

# Verwende die filter()-Funktion, um gerade Zahlen zu filtern
gefilterte_zahlen = filter(ist_gerade, zahlen)

# Konvertiere den Filter-Iterator in eine Liste, um das Ergebnis anzuzeigen
gefilterte_zahlen_liste = list(gefilterte_zahlen)

print(gefilterte_zahlen_liste)

arr = [2,3,4,5,6,7,8,9,1,2,34,23,2,323,23,23,1,3,000,323]
farr = filter(lambda x: x > 10 , arr)
farr = list(farr)
print(farr)















import csv

def filter_csv(input_csv_path, output_csv_path, column_name, search_value):
    """
    Filtert eine CSV-Datei und schreibt Zeilen, die den Suchwert im angegebenen
    Spaltennamen enthalten, in eine neue CSV-Datei.

    Args:
        input_csv_path (str): Pfad zur Eingabe-CSV-Datei.
        output_csv_path (str): Pfad zur Ausgabe-CSV-Datei.
        column_name (str): Name der Spalte, nach der gefiltert werden soll.
        search_value (str): Wert, nach dem in der angegebenen Spalte gesucht wird.
    """
    with open(input_csv_path, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        # Prüfe, ob der Spaltenname in der CSV-Datei vorhanden ist
        if column_name not in fieldnames:
            print(f"Spalte '{column_name}' nicht gefunden in der Eingabe-CSV.")
            return

        with open(output_csv_path, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            
            # Filtere Zeilen und schreibe die passenden Zeilen in die Ausgabedatei
            for row in reader:
                if str(row[column_name]) == search_value:
                    writer.writerow(row)

# Beispielaufruf der Funktion
input_csv_path = 'input.csv'
output_csv_path = 'filtered_output.csv'
column_name = 'Abteilung'
search_value = 'HR'

filter_csv(input_csv_path, output_csv_path, column_name, search_value)
