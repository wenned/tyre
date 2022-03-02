import os.path
import json
import requests
from datetime import date

class Verify:

  def verf():
    e= os.path.isfile("data.json")
    return e

  def verf_on(i):
      requisicao = requests.get("https://tyre-47d56-default-rtdb.firebaseio.com/.json?auth=O5ak0iZKz6iGaFLZ9559lm5AKVoqRGyjZjFD4Lb0")
      sr = (requisicao.json())

      for key in sr.keys():
          if sr[key]["Cart"] == str(i):
              return True
          else:
              ...

class ConsultaPath:
   
  def inserir(c, f):
      requisicao = requests.get("https://tyre-47d56-default-rtdb.firebaseio.com/.json?auth=O5ak0iZKz6iGaFLZ9559lm5AKVoqRGyjZjFD4Lb0")
      sr = (requisicao.json())

      for key in sr.keys():
          if sr[key]["Cart"] == str(c):
              data = {}
              data["Fire"] = f
              data["Date"] = str(date.today())

              key_url = requests.patch(f"https://tyre-47d56-default-rtdb.firebaseio.com/{key}.json?auth=O5ak0iZKz6iGaFLZ9559lm5AKVoqRGyjZjFD4Lb0", data=json.dumps(data))


  def seach_bd(i):
      requisicao = requests.get("https://tyre-47d56-default-rtdb.firebaseio.com/.json?auth=O5ak0iZKz6iGaFLZ9559lm5AKVoqRGyjZjFD4Lb0")
      sr = (requisicao.json())
      for key in sr.keys():
          if sr[key]["Cart"] == i:
              dice = f"""
            CARRETA : {sr[key]["Cart"]}
            Nº FOGO : {sr[key]["Fire"]}
            DATA    : {sr[key]["Date"]}
                  """
              return dice
    

  def new_creat(c, f):
      data = {}
      
      data["Cart"] = c
      data["Fire"] = f
      data["Date"] = str(date.today())

      requisicao = requests.post("https://tyre-47d56-default-rtdb.firebaseio.com/.json?auth=O5ak0iZKz6iGaFLZ9559lm5AKVoqRGyjZjFD4Lb0", data=json.dumps(data))


