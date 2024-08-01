import re

with open('C:\\Users\\Elena\\Downloads\\dataset_3363_2.txt', 'r') as file:

    for line in file:

        # Регулярное выражение для поиска пар буква-число
        pattern = re.compile(r'([a-zA-Z])(\d+)')

        # Находим все пары буква-число
        matches = pattern.findall(line)

        # Печатаем результаты
        for match in matches:
            print(f"{match[0] * int(match[1])}", end="")

                          # автоматическое закрытие файла

print('Файл закрыт')

