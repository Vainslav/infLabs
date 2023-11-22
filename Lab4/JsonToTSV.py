megaString1 = ''
megaString2 = ''
def to_tsv(element, string1, string2):
    global megaString1
    global megaString2
    if isinstance(element, dict):
        for k in element.keys():
            if isinstance(element[k],str) or isinstance(element[k],float):
                to_tsv(element[k], string1 + k, string2)
                continue
            to_tsv(element[k], string1 + k + '/', string2)
    if isinstance(element, str) or isinstance(element, float):
        string2 = string2 + str(element)
        megaString1+=string1 + ','
        megaString2+=string2 + ','
        return [string1, string2]
    if isinstance(element, list):
        for i, k in enumerate(element):
            to_tsv(k, string1 + str(i) + '/', string2)


with open('schedule.tsv', 'w', encoding="UTF-8") as W:
    with open('schedule.json', encoding="UTF-8") as F:
        N = eval(' '.join(F.readlines()))
        to_tsv(N, '', '')
        W.write(megaString1+'\n')
        W.write(megaString2+'\n')