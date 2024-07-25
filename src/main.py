from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from MainScreen import MainScreen
from HistoryScreen import HistoryScreen


class MyApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(MainScreen(0, name='main'))
		sm.add_widget(HistoryScreen(name='history'))
		return sm

if __name__ == '__main__':
	MyApp().run()
