import time


def to_yaml(dict_element, file, spaces, prev):
    if isinstance(dict_element, str):
        file.write(' ' + dict_element + '\n')
    elif isinstance(dict_element, list):
        for i in dict_element:
            to_yaml(i, file, spaces, 'list')
    elif isinstance(dict_element, dict):
        file.write('\n')
        for i in dict_element.keys():
            if not prev == 'list':
                file.write(spaces * ' ' + i + ':')
            else:
                file.write((spaces - 2) * ' ' + '- ' + i + ':')
            to_yaml(dict_element[i], file, spaces + 2, 'dict')


start_time = time.time()
for i in range(1000):
    with open("timetable.yaml", "w", encoding="UTF-8") as W:
        with open("schedule.json", encoding="UTF-8") as F:
            N = eval(' '.join(F.readlines()))
            to_yaml(N, W, 0, 0)

end_time = time.time()
elapsed_time = end_time*100 - start_time*100
print("Время выполнения:", elapsed_time)
# 0.100341796875
# 38.942962646484375
