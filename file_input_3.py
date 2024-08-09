with open('C:\\Users\\Elena\\Downloads\\dataset_3363_4.txt', 'r') as file, open('C:\\Users\\Elena\\Downloads\\out_3.txt', 'w') as output_file:
    datas =[]

    for line in file:
        datas.append(line.strip())

    new_datas = []

    for element in datas:
        element = element.split(";")
        new_datas.append(element)

    for data in new_datas: #получаем список из оценок
        data.pop((0))

    float_new_datas = []

    for data in new_datas: #превращаем str в float у оценок
        float_new_data = [float(num) for num in data]
        float_new_datas.append(float_new_data)


    for data in float_new_datas: #средняя оценка по каждому студенту
         output_file.write(f'{sum(data) / len(data)}\n')

    summ = 0
    average_results =[]


    for i in range(3): #средняя оценка по каждому предмету
        summ = 0
        count = 0
        for data in float_new_datas:
            summ += data[i]
            count += 1
            average = summ / count
        average_results.append(average)
    print(*average_results, file=output_file)















