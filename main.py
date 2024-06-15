from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.card import MDCard
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.metrics import dp

Window.size = (360, 640)

class DeviceListScreen(Screen):
    pass

class ChatScreen(Screen):
    pass

class BluetoothChatApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        self.title = 'Bluetooth Chat App'
        self.message_side = "left"  # Başlangıç tarafı "sol"
        return Builder.load_file('main.kv')
    
    def on_start(self):
        devices = ["Tr (Galaxy A5)", "Galaxy Tab A7" , "iPhone 12", "iPad Pro", "Huawei P30", "Xiaomi Note 9"]
        for device in devices:
            self.root.get_screen('device_list').ids.device_list.add_widget(
                OneLineListItem(text=device, on_release=self.go_to_chat)
            )
            self.create_chat_screen(device)
        
    def create_chat_screen(self, device_name):
        screen = ChatScreen(name=device_name)
        self.root.add_widget(screen)
    
    def add_message(self, side, text, time, device_name):
        message_box = self.root.get_screen(device_name).ids.message_box
        alignment = 'left' if side == 'left' else 'right'
        bg_color = (0.9, 0.9, 0.9, 1) if side == 'left' else (0.5, 0, 0.5, 1)
        
        card = MDCard(
            orientation='vertical',
            size_hint=(None, None),
            width=self.root.width * 0.75,
            padding=dp(8),
            radius=[dp(15), dp(15), dp(15), dp(15)],
            pos_hint={alignment: 1},
            md_bg_color=bg_color
        )

        message_label = Label(
            text=text,
            color=(0, 0, 0, 1),
            size_hint_y=None,
            height=dp(24)
        )
        time_label = Label(
            text=time,
            color=(0.5, 0.5, 0.5, 1),
            size_hint_y=None,
            height=dp(16),
            font_size='10sp'
        )

        card.add_widget(message_label)
        card.add_widget(time_label)
        card.height = message_label.height + time_label.height + dp(16)
        
        message_box.add_widget(card)
    
    def send_message(self):
        current_screen = self.root.current
        message_input = self.root.get_screen(current_screen).ids.message_input
        message_text = message_input.text
        if message_text:
            # Mevcut tarafı kullanarak mesajı ekle
            self.add_message(self.message_side, message_text, "Now", current_screen)
            # Tarafı değiştir
            self.message_side = "right" if self.message_side == "left" else "left"
            # Mesaj kutusunu temizle
            message_input.text = ""
    
    def go_to_chat(self, instance=None):
        device_name = instance.text
        self.root.current = device_name
    
    def go_to_device_list(self):
        self.root.current = 'device_list'

if __name__ == '__main__':
    BluetoothChatApp().run()
