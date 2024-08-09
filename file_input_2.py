with open('C:\\Users\\Elena\\Downloads\\dataset_3363_3.txt', 'r') as file:
    word_count = {}

    for line in file:
        # Убираем пробельные символы в начале и конце строки
        line = line.strip()
        # Разделяем строку на слова
        word_list = line.split()

        # Преобразуем слова к нижнему регистру и фильтруем, оставляя только те, которые состоят из букв
        word_list_lower = [word.lower() for word in word_list if word.isalpha()]

        # Подсчитываем количество каждого слова
        for word in word_list_lower:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    # Нахождение максимального значения
    max_word_count = max(word_count.values())

    # Нахождение всех ключей с максимальным значением
    max_word_counts = [key for key, value in word_count.items() if value == max_word_count]

    max_word_counts.sort()

    print(f"{max_word_counts[0]} {max_word_count}")








