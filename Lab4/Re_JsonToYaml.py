import re
import time


start_time = time.time()
for i in range(1000):
    with open("timetable.yaml", "w", encoding="UTF-8") as W:
        with open("schedule.json", encoding="UTF-8") as F:
            N = F.readlines()
            pattern1 = r'(\s*)"(.*)"(:\s)"(.*)"'
            pattern2 = r'(\s*)"(.*)"(:\s)(\d*)'
            for i in N:
                string = ''
                if re.match(pattern1, i):
                    if re.findall(pattern1, i):
                        for j in re.findall(pattern1, i)[0]:
                            string += j
                        W.write(string[2:]+'\n')
                elif re.match(pattern2, i):
                    if re.findall(pattern2, i):
                        for j in re.findall(pattern2, i)[0]:
                            string += j
                        W.write(string[2:] + '\n')
end_time = time.time()
elapsed_time = end_time*100 - start_time*100
print("Время выполнения:", elapsed_time)
# 0.098480224609375
# 40.512237548828125