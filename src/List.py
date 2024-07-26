from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class List(BoxLayout):
	def __init__(self, list_, **kwargs):
		super(List, self).__init__(**kwargs, orientation='vertical')
		self.list = list_
		for record in self.list:
			self.add_widget(Label(text=str(record)))
	
	def setList(self, list_):
		self.list = list_
		self.clear_widgets()
		for record in self.list:
			self.add_widget(Label(text=str(record)))

