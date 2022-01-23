from kivy.app import App
from request import ConsultaPath
import os.path
from kivy.uix.screenmanager import ScreenManager, Screen


#from kivy.core.window import Window
#Window.size = (600, 300)


class MyTyre(ScreenManager):
  pass

class TyreC(Screen):

  def __init__(self, **kwargs):
    super().__init__()

  def busc(self, *args):
    i = self.ids["cr"].text
    
    if len(i)>= len('21000'):
        y = os.path.exists(f'Bancod/{i}.bd')
     
        if y:
            self.ids["dados_CR"].text = ConsultaPath.seach_bd(int(i))
            self.ids["cr"].text = ''

    else:
        App.get_running_app().root.current = 'cri'

class Log(Screen):
  ...

class CriBd(Screen):
    ...

class Cadastro(Screen):
    #def __init_(self, **kwargs):
     #   super().__init__()

    def insertd(self, *args):
        y = self.ids["cr"].text
        
        if len(y)>= len('21000'):
            vr = ConsultaPath.new_creat(y)
            l = self.ids["ci"].text
            i = self.ids["cy"].text
            ConsultaPath.inserir(y,l,i)

        else:
            #h= self.CriBD.ids["tl"].text = 'DADOS INVALIDOS!'
            App.get_running_app().root.current ='cri'

class Actions(Screen):
  ...

class Atualize(Screen):
    def buscr(self,*args):
        y = self.ids["ar"].text

        if len(y) >= len('21000'):
            a = os.path.exists(f'Bancod/{y}.bd')

            if a:
                a = self.ids["ar"].text
                b = self.ids["br"].text
                c = self.ids["cy"].text

                ConsultaPath.inserir(a,b,c)

                self.ids["ar"].text = ''
                self.ids["br"].text = ''
                self.ids["cy"].text = ''
            else:
                ...
        
        else:
            App.get_running_app().root.current ='cri'

class Tyre(App):

  def build(self):
  
    return MyTyre()
   
Tyre().run()
