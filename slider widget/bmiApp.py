from kivy.app import App
from kivy.uix.screenmanager import ScreenManager , Screen

class Scr_bmi(Screen): #หน้าจอที่ 2
    def cal_bmi(self): 
        weight= float(self.ids.txt_weight.text)
        height= int(self.ids.txt_height.text)
        height= height/100
        bmi = weight/(height*height)
        self.ids.lbl_bmi.text=str(bmi)
        if bmi > 35 :
            self.ids.lbl_bmi.color='#FF0000'
            self.ids.img_bmi.source='pic/r.PNG'
        elif bmi > 30:
            self.ids.lbl_bmi.color='#FF6600'
            self.ids.img_bmi.source='pic/o.PNG'
        elif bmi > 25:
            self.ids.lbl_bmi.color='#FFFF00'
            self.ids.img_bmi.source='pic/y.PNG'
        elif bmi > 18:
            self.ids.lbl_bmi.color='#33CC00'
            self.ids.img_bmi.source='pic/g.PNG'
        else:
            self.ids.lbl_bmi.color='#66CCFF'
            self.ids.img_bmi.source='pic/b.PNG'
        
class UI(ScreenManager): #ทำหน้าที่จัดการหน้าจอต่างๆ
    pass

class Scr_KnowledGe(Screen): #หน้าจอที่ 1
    pass

class bmiApp(App):
    def build(self):
        return UI()
     
if __name__=="__main__":
    bmiApp().run()