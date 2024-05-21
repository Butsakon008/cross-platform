from kivy.app import App
from kivy.uix.screenmanager import Screen

class UI(Screen): #ทำหน้าที่แสดง UI เชื่อมโยงไป kv
    def Add_item(self):
        #นำค่าที่เพิ่ม ไปเพิ่มใน spinner
        self.ids.spin_lang.values.append(self.ids.txt_input.text)
    pass

class spinnerApp(App):
    def build(self):
        return UI()
    
if __name__ == "__main__":
    spinnerApp().run()