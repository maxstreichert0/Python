import csv

# Funktion zum Einfügen einer Zeile an der fünften Position einer Textdatei
def insert_line_at_five(file_path, new_line):
    """
    Fügt eine neue Zeile an der fünften Position in eine Textdatei ein. Falls die Datei weniger als fünf Zeilen hat,
    werden leere Zeilen hinzugefügt, bis die Datei lang genug ist.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Stelle sicher, dass die Liste lang genug ist. Falls nicht, füge leere Zeilen hinzu.
    while len(lines) < 4:
        lines.append('\n')

    # Füge die neue Zeile bei Index 4 ein, was der fünften Zeile entspricht.
    lines.insert(4, new_line + '\n')

    with open(file_path, 'w') as file:
        file.writelines(lines)

# Funktion zum Filtern von Zeilen basierend auf ihrer Länge
def filter_lines(file_path):
    """
    Filtert Zeilen aus einer Textdatei, die länger als 10 Zeichen sind, und überschreibt die Datei mit diesen Zeilen.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Filtere Zeilen, die länger als 10 Zeichen sind
    flines = filter(lambda x: len(x.strip()) > 10, lines)

    with open(file_path, 'w') as file:
        file.writelines(flines)

# Beispiel für das Schreiben von binären Daten in eine Datei
def write_binary_data():
    """
    Demonstriert, wie binäre Daten in eine Datei geschrieben werden.
    """
    file_path = 'beispiel.dat'
    bytes_to_write = bytes([1, 2, 3, 4, 5, 6, 7, 8, 9])  # Eine Liste von Bytes
    
    with open(file_path, 'wb') as file:
        file.write(bytes_to_write)

# Funktion zum Filtern einer CSV-Datei und Schreiben des Ergebnisses in eine neue Datei
def filter_csv(input_csv_path, output_csv_path, column_name, search_value):
    """
    Filtert eine CSV-Datei basierend auf einem spezifischen Wert in einer benannten Spalte und schreibt die
    gefilterten Zeilen in eine neue CSV-Datei.
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

# Hauptteil des Skripts, der die Funktionen demonstriert
if __name__ == "__main__":
    # Füge eine neue Zeile in die fünfte Zeile der Datei ein
    file_path = 'data.txt'
    new_line = 'Dies ist die neue fünfte Zeile.'
    insert_line_at_five(file_path, new_line)

    # Filtere Zeilen in der Datei basierend auf ihrer Länge
    filter_lines(file_path)

    # Schreibe binäre Daten in eine Datei
    write_binary_data()

    # Filtere eine CSV-Datei und schreibe gefilterte Zeilen in eine neue Datei
    input_csv_path = 'input.csv'
    output_csv_path = 'filtered_output.csv'
    column_name = 'Abteilung'
    search_value = 'HR'
    filter_csv(input_csv_path, output_csv_path, column_name, search_value)
