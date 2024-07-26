from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from MainScreen import MainScreen
from HistoryScreen import HistoryScreen


class MyApp(App):
	def build(self):
		self.ensure_datafile_exists()
		sm = ScreenManager()
		sm.add_widget(MainScreen(0, name='main'))
		sm.add_widget(HistoryScreen(name='history'))
		return sm
	
	def ensure_datafile_exists(self):
		if not os.path.exists(os.path.join(App.get_running_app().user_data_dir, "data.txt")):
			with open(os.path.join(App.get_running_app().user_data_dir, "data.txt"), "w") as f:
				f.write("0")

if __name__ == '__main__':
	MyApp().run()
