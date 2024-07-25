from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from History import History
from Memory import Memory

class HistoryScreen(Screen):
	def __init__(self, **kwargs):
		super(HistoryScreen, self).__init__(**kwargs)
		self.memory = Memory()
		history = History(self.memory.get_history())
		back_button = Button(text='Back', on_press=self.onBackButtonPress)
		layout = BoxLayout(orientation='vertical')
		layout.add_widget(back_button)
		layout.add_widget(history)
		self.add_widget(layout)

	def onBackButtonPress(self):
		self.manager.current = 'main'

