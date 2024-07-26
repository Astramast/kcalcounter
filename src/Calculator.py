from kivy.uix.button import Button
from NumberHolder import NumberHolder
from kivy.uix.widget import Widget
from enum import Enum
from Operation import Add, Subtract, Multiply, Divide


class Calculator(Widget):
	class State(Enum):
		DEFAULT = 0
		NUMBER = 1
	
	def __init__(self, listener, **kwargs):
		super(Calculator, self).__init__(**kwargs)
		self.listener = listener
		self.buffer = 0
		self.current = "0"
		self.is_float = False
		self.operation_buffer = Add()
		self.state = Calculator.State.DEFAULT
		layout = BoxLayout(orientation='vertical')
		layout.add_widget(NumberHolder(0, self.on_number_press))
		self.add_widget(layout)
	
	def __operate(self):
		self.buffer = self.operation_buffer(self.buffer, float(self.current))
		self.current = "0"
		self.state = Calculator.State.DEFAULT
		
	def on_number_press(self, number):
		if self.state == Calculator.State.DEFAULT:
			self.current = number
			self.state = Calculator.State.INTEGER
		else:
			self.current += number
	
	def on_operation_press(self, operation):
		if self.state != Calculator.State.DEFAULT:
			self.__operate()
		self.operation_buffer = operation
	
	def on_result_press(self):
		if self.state != Calculator.State.DEFAULT:
			self.__operate()
	
	def on_backspace_press(self):
		self.current = str(self.current)[:-1]
		if self.current == "":
			self.current = "0"
	
	def on_dot_press(self):
		if "." not in self.current:
			self.current += "."

