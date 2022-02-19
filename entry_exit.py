import json
from request import Verify

class SettingsTyre:

    def creat_note(os, lista):

      if Verify.verf():

        dados = {}
        insert_d = []

        for nu in lista:
            insert_d.append(nu)
        dados[f"{os}"]=insert_d

        with open('data.json', 'r') as ty:
            dice = json.load(ty)
            dice.update(dados)

      

        with open('data.json', 'w') as ty:
            json.dump(dice, ty)
      else:
        with open('data.json', 'a') as ty:
          ty.write('{}')
        SettingsTyre.creat_note(os, lista)

    def input_update(lista):

        for nu in lista:
            with open('data.json', 'r') as ty:
                dice = json.load(ty)
            y= dice.keys()

            for i in y:
                if nu in dice[f'{i}'][:]:
                    for e in range(13):
                        if nu == dice[f'{i}'][e]:
                            dice[f"{i}"][e] = str(nu)+'entry'

                            with open('data.json', 'w') as ty:
                                json.dump(dice, ty)
                            break
                else:
                    ...

    def os_open():

      if Verify.verf():
        with open('data.json', 'r') as ty:
            dice = json.load(ty)
            y= list(dice.keys())
        cont = 0
        dtemp = {}

        for i in y:
            f = dice[f'{i}'][:]
            ltemp = []

            for e in f:
                if len(str(e)) <= len('xxxxx') and len(str(e)) > len('22') :
                    ltemp.append(e)
                    dtemp[f'{y[cont]}'] = ltemp
                else:
                    ...
            cont = cont + 1
        
        return dtemp
        dtemp.clear()
      else:
        with open('data.json', 'a') as ty:
          ty.write('{}')
          ty.close()
