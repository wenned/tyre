import json
from pathlib import Path

def creat_note():
  dados = {}
  insert_d = []
  os = input('nº os: ')
  for i in range(3):
    os_x = int(input('nº tyre: '))
    insert_d.append(os_x)
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

