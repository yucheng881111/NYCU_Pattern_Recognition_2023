import pandas as pd
import os
import csv

TASK = "task3"
# folder path
dir_path = "C:\\Users\\yucheng\\Desktop\\PR_final\\dataset\\train\\" + TASK + "\\output"


# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

is_generated = []
for p in res:
    if not p.startswith('_groundtruth_'):
        is_generated.append(p)
#print(len(is_generated))

d = {}
anno_path = r"C:\Users\yucheng\Desktop\PR_final\dataset\train\annotations.csv"
with open(anno_path, newline='') as csvfile:
    for row in csv.reader(csvfile, delimiter=','):
        li = row[0].split('/')
        if len(li) == 2:
            d[li[1]] = row[1]

#for item in d.items():
#    print(item[0], item[1])

labels = []
for p in is_generated:
    k = p.split('_')[2]
    labels.append(d[k])
    
df = pd.DataFrame(list(zip(is_generated, labels)), columns =['filename', 'label'])
print(df) 

df.to_csv(os.path.join(dir_path, 'annotations.csv'))

