from typing import List


def read_file_double_new_line(file_name: str) -> List[List[str]]:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read().split("\n\n")
    data_list = [i.split("\n") for i in data]

    return data_list


def read_file_with_new_line(file_name: str) -> List[str]:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read().split("\n")

    return data
