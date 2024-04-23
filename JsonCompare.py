import json
import pendulum


print(f"The current time is {pendulum.now()}")

input1='path_to_file1'
input2='path_to_file2'
output='new_path'

def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def extract_unit_names(data):
    unit_names = []
    for unit in data:
        unit_names.append(unit.values()[0])
    return unit_names
def compare_unit_lists(list1, list2):
    unique_in_list1 = set(list1) - set(list2)
    unique_in_list2 = set(list2) - set(list1)
    return unique_in_list1, unique_in_list2

# Zastąp 'path_to_file1.json' i 'path_to_file2.json' ścieżkami do Twoich plików JSON
data1 = load_json_file(input1)
data2 = load_json_file(input2)

# Wyodrębnij nazwy jednostek z obu plików
unit_names_file1 = extract_unit_names(data1)
unit_names_file2 = extract_unit_names(data=data2)

# Porównaj listy jednostek i znajdź unikalne jednostki dla każdego pliku
unique_in_file1, unique_in_file2 = compare_unit_lists(unit_names_file1, unit_names_file2)

# Zapisz unikalne jednostki do pliku tekstowego
with open(output, 'w', encoding='utf-8') as output_file:
    output_file.write("Unikalne w pierwszym pliku:\n")
    for unit in unique_in_file1:
        output_file.write(unit + "\n")
    
    output_file.write("\nUnikalne w drugim pliku:\n")
    for unit in unique_in_file2:
        output_file.write(unit + "\n")

print("Zapisano unikalne jednostki do pliku 'unikalne_jednostki.txt'.")