import sqlite3

conn = sqlite3.connect('PlasticPollution.db')

cur = conn.cursor()

# myKeys = list()
# myDict = dict()

# with open("plastic-pollution.csv", "r") as FILE:
#     cntr = 0
#     cntr2 = -1

#     for line in FILE:
#         cntr += 1
#         cntr2 = -1
#         if cntr != 1:
#             for word in line.split(","):
#                 cntr2 += 1
#                 myDict[myKeys[cntr2]].append(word)
#         else:
#             for word in line.split(","):
#                 myDict[word] = []
#                 myKeys.append(word)

itemCollect = list()
myDataSet = list()

with open("plastic-pollution.csv", "r") as FILE:
    cntr = -1

    for line in FILE:
        cntr += 1
        if cntr != 0:
            for word in line.split(","):
                itemCollect.append(word)
            temp = tuple(itemCollect)
            itemCollect.clear()
            myDataSet.append(temp)

cur.execute("""CREATE TABLE IF NOT EXISTS plasticPollution(
    Entity TEXT,
    Code TEXT,
    Year TEXT,
    Plastic TEXT);
""")

cur.executemany("INSERT INTO plasticPollution VALUES(?,?,?,?);", myDataSet)

conn.commit()