import os.path
import sqlite3

class ConsultaPath:
   
  def inserir(w, y, l):

      con = sqlite3.connect(f'Bancod/{w}.bd')
      editor = con.cursor()

      con.execute("""
      INSERT INTO tyre (fogo, carreta, data)
      VALUES (?, ?, ?)
      """,(y, w, l))
      
      con.commit()
      con.close()

  def seach_bd(i):

      con = sqlite3.connect(f'Bancod/{i}.bd')
      editor = con.cursor()
    
      r = editor.execute(
      'SELECT * FROM tyre WHERE carreta = ?', (i,))
      count = 0
      for row in r.fetchall():
            count += 1
 
      e = editor.execute('SELECT * FROM tyre WHERE carreta = ?', (i,))
      if e.fetchone()[2] == i:
          e = editor.execute(
          'SELECT * FROM tyre WHERE id = ?', (count,))
          y = e.fetchall()[0]

      f = (f'''Carreta: {y[2]}
Nº Fogo:  {y[1]}
Ultima data: {y[3]}''')
      return f

      con.close()

  def new_creat(n):
      
    e = '''
  A Carreta nao exite, deseja criar novo veiculo?
  Sim [1] / Não [2].
  '''

    if newv in '1':
      print ('Criando banco de dados...')
      con = sqlite3.connect(f'Bancod/{n}.bd')
      print ('Conectando ao banco de dados ....')
      editor = con.cursor()

      print('Gerando tabelas...')

      editor.execute("""
      CREATE TABLE tyre (
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      fogo INTEGER,
      carreta INTERGER,
      data DATE NOT NULL
      );
      """)

      fogo = input('Nº Fogo: ')
      data = input('Data YYYY-MM-DD: ')
      ConsultaPath.inserir(n, fogo, n, data)
