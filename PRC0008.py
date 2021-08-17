import csv
def GET_ROW_COUNT() -> int:
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
def IS_REGISTERED(avatarName):
    csv_list = []
    with open('battle_royale.csv', 'r') as source:
        battleRoyaleData = csv.reader(source, delimiter=',')
        for row in battleRoyaleData:
            csv_list.append(row)
        if not any(avatarName in x for x in csv_list):
           return True
        else:
            return False
def main():
    wouldLikeToCheckIfRegistered = input("Would you like to check if your avatar name is registered? \n")
        if wouldLikeToCheckIfRegistered.lower() == 'yes' or wouldLikeToCheckIfRegistered.lower() == 'y':
            avatarName = input("Enter avatar name. \n")
            if IS_REGISTERED():
                print("You are already registered. \n")
            else:
                print("You are not registered, would you like to register under that avatar name? ")
                wouldLikeToRegister = input("\n")
                if wouldLikeToRegister.lower() == 'y' or wouldLikeToRegister.lower() == 'yes':
                    name = input("Enter your name.\n")
                    WRITE_PLAYER(avatarName, name)
if __name__ == "__main__":
    main()
else:
    exit