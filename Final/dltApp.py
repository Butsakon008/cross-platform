from kivy.app import App
from kivy.uix.screenmanager import ScreenManager , Screen

class UI(ScreenManager): #ทำหน้าที่จัดการหน้าจอต่างๆ
    pass

class Dlt_1(Screen): #หน้าจอที่ 1
    pass

class Dlt_2(Screen): #หน้าจอที่ 2
    def check_data(self):
        txt_Dlt1 = self.ids.txt_Dlt1.text
        txt_Dlt3 = self.ids.txt_Dlt3.text 
        
        if len(txt_Dlt1) != 13 or len(txt_Dlt3) != 10:
            self.ids.btn_regis.text='ไม่พร้อมบันทึกข้อมูล'
        else:
            self.ids.btn_regis.text='พร้อมบันทึกข้อมูล'

class dltApp(App):
    def build(self):
        return UI()
     
if __name__=="__main__":
    dltApp().run()