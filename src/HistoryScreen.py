from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from Database import Database
from List import List


class HistoryScreen(Screen):
	def __init__(self, **kwargs):
		super(HistoryScreen, self).__init__(**kwargs)
		self.history = List([])
		self.loadHistory()
		back_button = Button(text='Back', on_press=self.onBackButtonPress)
		layout = BoxLayout(orientation='vertical')
		layout.add_widget(back_button)
		layout.add_widget(self.history)
		self.add_widget(layout)
	
	def loadHistory(self):
		with Database() as db:
			self.history.setList(db.get_history()) 
	
	def onBackButtonPress(self, instance):
		self.manager.current = 'main'
	
	def on_enter(self, *args):
		self.loadHistory()

