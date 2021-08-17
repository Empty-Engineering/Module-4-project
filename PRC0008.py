import csv
def GET_ROW_COUNT():
    with open('battle_royale.csv', 'r') as source:
        battleRoyaleData = csv.reader(source, delimiter=',')
        row_count = sum(1 for row in battleRoyaleData)
    return row_count
def DISPLAY_PLAYERS():
    with open('battle_royale.csv', 'r') as source:
        battleRoyaleData = csv.reader(source, delimiter=',')
        for row in battleRoyaleData:
            print(row)
def WRITE_PLAYER(avatarName, name):
    csv_list = []
    rowCount = GET_ROW_COUNT()
    with open('battle_royale.csv', 'r') as source:
        battleRoyaleData = csv.reader(source, delimiter=',')
        for row in battleRoyaleData:
            csv_list.append(row)
        csv_list.append([f"'{avatarName}'", f"'{name}'", f"'{rowCount}'"])
    with open('battle_royale.csv', 'w', newline='') as csvfile:
        newWrite = csv.writer(csvfile, delimiter=',')
        newWrite.writerows(csv_list)
