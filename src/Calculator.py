from kivy.uix.button import Button
from NumberHolder import NumberHolder
from kivy.uix.widget import Widget


class Calculator(Widget):
	def __init__(self, listener, **kwargs):
		super(Calculator, self).__init__(**kwargs)
		self.listener = listener
		layout = BoxLayout(orientation='vertical')
		layout.add_widget(NumberHolder(0, self.on_number_press))
		self.add_widget(layout)

	def on_number_press(self, number):
		self.listener.onNumberConfirmationPress(number)

