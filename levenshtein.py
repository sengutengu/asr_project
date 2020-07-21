import csv, editdistance, string
from statistics import mean

def stripper(s):
    return s.translate(str.maketrans('', '', string.punctuation))

def average_calculator(l1, l2):
    list = []
    for i in range(len(groundtruths)):
        list.append(l1[i]/len(l2[i]))
    return mean(list)

with open('results.csv', 'r') as file:
    reader = csv.reader(file)
    groundtruths = []
    deepspeech_scorer = []
    deepspeech_noscorer = []
    amazon = []
    azure = []
    watson = []

    firstrow = 0
    for row in reader:
        if firstrow == 0:
            firstrow = 1
        else:
            groundtruths.append(stripper(row[1]))
            deepspeech_scorer.append(stripper(row[2]))
            deepspeech_noscorer.append(stripper(row[3]))
            amazon.append(stripper(row[4]))
            azure.append(stripper(row[5]))
            watson.append(stripper(row[6]))

    groundtruths = [x.upper().lstrip() for x in groundtruths]
    deepspeech_scorer = [x.upper().lstrip() for x in deepspeech_scorer]
    deepspeech_noscorer = [x.upper().lstrip() for x in deepspeech_noscorer]
    amazon = [x.upper().lstrip() for x in amazon]
    azure = [x.upper().lstrip() for x in azure]
    watson = [x.upper().lstrip() for x in watson]

    DS_S = []
    DS_NS = []
    AMA = []
    AZU = []
    WAT = []

    for i in range(len(groundtruths)):
        DS_S.append(editdistance.eval(groundtruths[i],deepspeech_scorer[i]))
        DS_NS.append(editdistance.eval(groundtruths[i],deepspeech_noscorer[i]))
        AMA.append(editdistance.eval(groundtruths[i], amazon[i]))
        AZU.append(editdistance.eval(groundtruths[i], azure[i]))
        WAT.append(editdistance.eval(groundtruths[i], watson[i]))

    print(DS_S)
    print(groundtruths[2])
    print(deepspeech_scorer[2])

    print("DS_S: " + str(average_calculator(DS_S, deepspeech_scorer)))
    print("DS_NS: " + str(average_calculator(DS_NS, deepspeech_noscorer)))
    print("AMA: " + str(average_calculator(AMA, amazon)))
    print("AZU: " + str(average_calculator(AZU, azure)))
    print("WAT: " + str(average_calculator(WAT, watson)))
