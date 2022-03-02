from kivy.app import App
from request import ConsultaPath, Verify
from entry_exit import SettingsTyre
import os.path
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label

from kivy.core.window import Window
Window.size = (300, 600)


class MyTyre(ScreenManager):
  pass

class TyreC(Screen):

  def __init__(self, **kwargs):
    super().__init__()

  def busc(self, *args):
    i = self.ids["cr"].text
    
    if len(i)>= len('21000'):

        if Verify.verf_on(i):
            self.ids["dados_CR"].text = ConsultaPath.seach_bd(i)
            self.ids["cr"].text = ''

        else:
            App.get_running_app().root.current = 'cri'
            self.ids["cr"].text = ''

    else:
        App.get_running_app().root.current = 'cri'

class Log(Screen):
  ...

class Cadastro(Screen):

    def insertd(self, *args):
        y = self.ids["cr"].text
        
        if len(y)>= len('21000'):

            y = self.ids["cr"].text
            l = self.ids["ci"].text

            ConsultaPath.new_creat(y,l)

            self.ids["cr"].text = ''
            self.ids["ci"].text = ''

        else:
            App.get_running_app().root.current = 'cri'
            
class CriBd(Screen):
    ...

class Actions(Screen):
  ...

class Entry_Exit(Screen):
    ...

class Saidap(Screen):
    global l
    l = []

    def criar_l(self, *args):
        verif = self.ids["li"].text
        if verif == '':
            ...
        else:
            k = self.ids["li"].text
            l.append(int(k))
            self.ids["li"].text = '' 

    def criar(self, *args):
        verif = self.ids["os"].text
        if verif == '':
            ...
        else:
            os = self.ids["os"].text
            SettingsTyre.creat_note(os, l)
            self.ids["os"].text = ''
    def limp(self):
        l.clear()

class Entrap(Screen):
    global lit
    lit = []
    def listEntry(self, *args):
        verif = self.ids["nu"].text
        if verif == '':
            ...
        else:
            nu = self.ids["nu"].text
            lit.append(int(nu))
            self.ids["nu"].text = ''
            SettingsTyre.input_update(lit)


class Atualize(Screen):
    
    def buscr(self,*args):
        c = self.ids["ar"].text

        if len(c) >= len('21000'):

            if Verify.verf_on(c):
                c = self.ids["ar"].text
                f = self.ids["br"].text

                ConsultaPath.inserir(c,f)

                self.ids["ar"].text = ''
                self.ids["br"].text = ''
            else:
                App.get_running_app().root.current = 'cri'

        else:
            App.get_running_app().root.current ='cri'
 
class Relatorio(Screen):

    def addWidget(self, **kargs):

        if Verify.verf():
            dic = dict(SettingsTyre.os_open())
            key = list(dic.keys())

            for chv in key:
                e = f'OS: {chv} = {dic[chv]}'
                self.ids.box.add_widget(Label(text = f'{e}', font_size=12, size_hint_y = None, height= 100)) 
            key.clear()
            dic.clear()
        else:
            self.ids.box.add_widget(Label(text='INFORMAÇOES NAO ENCONTRADA!', font_size=15, size_hint_y = None, center_y = 0.5))

class Tyre(App):
  def build(self):
    return MyTyre()

if __name__ == '__main__':
    Tyre().run()
