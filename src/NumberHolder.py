from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class NumberHolder(BoxLayout):
	def __init__(self, number, listener, **kwargs):
		super(NumberHolder, self).__init__(**kwargs, orientation='horizontal')
		self.number = number
		self.label = Label(text=str(number))
		button = Button(text='V', on_press=self.onButtonPress)
		self.add_widget(self.label)
		self.add_widget(button)

	def set_number(self, number):
		self.number = number
		self.label.text = str(number)

	def onButtonPress(self, instance):
		self.listener.onNumberConfirmationPress(self.number)

