import csv
def GET_ROW_COUNT() -> int:
    with open('battle_royale.csv', 'r') as source:
        battleRoyaleData = csv.reader(source, delimiter=',')
        row_count = sum(1 for row in battleRoyaleData)
    return row_count
def DISPLAY_PLAYERS() -> None:
    data = []
    with open('battle_royale.csv', 'r') as source:
        battleRoyaleData = csv.reader(source, delimiter=',')
        for row in battleRoyaleData:
            print(row)
def WRITE_PLAYER(avatarName: str, name: str) -> None:
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
def IS_REGISTERED(avatarName: str):
    csv_list = []
    with open('battle_royale.csv', 'r') as source:
        battleRoyaleData = csv.reader(source, delimiter=',')
        for row in battleRoyaleData:
            csv_list.append(row)
        return any(avatarName in x for x in csv_list)
def main():
    wouldLikeToCheckIfRegistered = input("Would you like to check if your avatar name is registered? \n")
    if wouldLikeToCheckIfRegistered.lower() == 'yes' or wouldLikeToCheckIfRegistered.lower() == 'y':
        avatarName = input("Enter avatar name. \n")
        matchName = str("'%s'" % avatarName)
        if IS_REGISTERED(matchName) == True:
            print("You are already registered. ")
        else:
            print("You are not registered, would you like to register under that avatar name? ")
            wouldLikeToRegister = input("")
            if wouldLikeToRegister.lower() == 'y' or wouldLikeToRegister.lower() == 'yes':
                name = input("Enter your name.\n")
                WRITE_PLAYER(avatarName, name)
    else:
        wouldLikeList = input("Would you like a list of participants? ")
        wantLikeList = lambda wouldLikeList : wouldLikeList.lower() == "y" or wouldLikeList.lower() == 'yes'
        if wantLikeList:
            DISPLAY_PLAYERS()
            exit()
        else:
            wouldLikeToRegister = input("Would you like to register? \n")
            if wouldLikeToRegister.lower() == 'y' or wouldLikeToRegister.lower() == 'yes':
                avatarName = input("Enter avatar name.\n")
                name = input("Enter name.\n")
                WRITE_PLAYER(avatarName, name)
                exit()
            else:
                exit()
if __name__ == "__main__":
    main()
else:
    exit