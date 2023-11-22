import yaml
import json
import time

start_time = time.time()
for i in range(1000):
    with open("timetable.yaml", "w", encoding="UTF-8") as W:
        with open("schedule.json", encoding="UTF-8") as F:
            W.write(yaml.dump(json.load(F), allow_unicode=True))

end_time = time.time()

elapsed_time = end_time*100 - start_time*100
print("Время выполнения:", elapsed_time)
# 0.21112060546875
# 178.74374389648438
