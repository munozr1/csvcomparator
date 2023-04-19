import csv
from datetime import datetime

def load_files(file_path_1, file_path_2):
    try:
        with open(file_path_1, 'r') as file1:
            data1 = list(csv.reader(file1))
        with open(file_path_2, 'r') as file2:
            data2 = list(csv.reader(file2))
    except FileNotFoundError as e:
        if file_path_1 not in str(e):
            print(f"Invalid file path: {file_path_1}")
        if file_path_2 not in str(e):
            print(f"Invalid file path: {file_path_2}")
        return None
    else:
        return data1, data2


def compare_rows(row1, row2):
    if len(row1) != len(row2):
        return False
    for col1, col2 in zip(row1, row2):
        if col1.strip().lower() != col2.strip().lower():
            try:
                date1 = datetime.strptime(col1, '%m-%d-%Y')
                date2 = datetime.strptime(col2, '%m/%d/%Y')
                if date1 != date2:
                    return False
            except ValueError:
                return False
    return True

def find_unmatched_rows(data1, data2):
    unmatched_rows = []
    for row1 in data1:
        is_matched = False
        for row2 in data2:
            if compare_rows(row1, row2):
                is_matched = True
                break
        if not is_matched:
            unmatched_rows.append(row1)
    return unmatched_rows


# def compare(file1, file2):
#   data1, data2 = load_files(file1, file2)
#   if data1 is None or data2 is None:
#     return
#   unmatched_rows = find_unmatched_rows(data1, data2)
#   print(f"Unmatched rows: {unmatched_rows}")
  
def compare(file1, file2):
    data1, data2 = load_files(file1, file2)
    if data1 is None or data2 is None:
        return [], []

    unmatched_rows_file1 = find_unmatched_rows(data1, data2)
    unmatched_rows_file2 = find_unmatched_rows(data2, data1)

    return unmatched_rows_file1, unmatched_rows_file2
