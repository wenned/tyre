import json
from pathlib import Path

class SettingsTyre:

    def creat_note(os, lista):
        dados = {}
        insert_d = []

        for nu in lista:
            insert_d.append(nu)
        dados[f"{os}"]=insert_d

        with open('data.json', 'r') as ty:
            dice = json.load(ty)
            dice.update(dados)
        filePath=Path("data.json")
        try:
            filePath.unlink()
        except OSError as e:
            print(f"Error:{ e.strerror}")

        with open('data.json', 'a') as ty:
            json.dump(dice, ty)

    def input_update(x):

        with open('data.json', 'r') as ty:
            dice = json.load(ty)
        y= dice.keys()

        for i in y:
            (dice[f'{i}'][:])

            if x in dice[f'{i}'][:]:
                for e in range(13):
                    if x == dice[f'{i}'][e]:
                        dice[f"{i}"][e] = str(x)+'entry'

                        with open('data.json', 'w') as ty:
                            json.dump(dice, ty)
                        break
            else:
                ...
