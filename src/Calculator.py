from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from enum import Enum
from Operation import Add, Subtract, Multiply, Divide


class Calculator(BoxLayout):
	class State(Enum):
		DEFAULT = 0
		NUMBER = 1
	
	def __init__(self, listener, **kwargs):
		super(Calculator, self).__init__(**kwargs, orientation='vertical')
		self.listener = listener
		self.buffer = 0
		self.current = "0"
		self.operation_buffer = Add()
		self.state = Calculator.State.DEFAULT
		self.label = Label(text=self.current)
		button = Button(text='V', on_press=self.on_validation_press)
		hlayout = BoxLayout(orientation='horizontal')
		hlayout.add_widget(self.label)
		hlayout.add_widget(button)
		glayout = GridLayout(cols=4, rows=5)
		buttons_grid = [
			("7", self.on_number_press), ("8", self.on_number_press), ("9", self.on_number_press), ("/", lambda instance:self.on_operation_press(instance, Divide())), 
			("4", self.on_number_press), ("5", self.on_number_press), ("6", self.on_number_press), ("*", lambda instance:self.on_operation_press(instance, Multiply())), 
			("1", self.on_number_press), ("2", self.on_number_press), ("3", self.on_number_press), ("-", lambda instance:self.on_operation_press(instance, Subtract())), 
			("0", self.on_number_press), (".", self.on_dot_press), ("=", self.on_result_press), ("+", lambda instance:self.on_operation_press(instance, Add())), 
			("R", self.on_reset_press), ("", None), ("", None), ("<", self.on_backspace_press)
		]
		for text, callback in buttons_grid:
			if callback is None:
				button = Button(text=text)
			else:
				button = Button(text=text, on_press=callback)
			glayout.add_widget(button)
		
		self.add_widget(hlayout)
		self.add_widget(glayout)
	
	def __operate(self):
		self.buffer = self.operation_buffer(self.buffer, float(self.current))
		self.current = "0"
		self.label.text = str(self.buffer)
		self.operation_buffer = Add()
		self.state = Calculator.State.DEFAULT
		
	def on_number_press(self, instance):
		if self.state == Calculator.State.DEFAULT:
			self.current = instance.text
			self.state = Calculator.State.NUMBER
		else:
			self.current += instance.text
		self.label.text = self.current
	
	def on_operation_press(self, instance, operation):
		if self.state != Calculator.State.DEFAULT:
			self.__operate()
		self.operation_buffer = operation
	
	def on_result_press(self, instance):
		if self.state != Calculator.State.DEFAULT:
			self.__operate()
	
	def on_backspace_press(self, instance):
		if self.state != Calculator.State.DEFAULT:
			self.current = str(self.current)[:-1]
			if self.current == "":
				self.current = "0"
			self.label.text = self.current
	
	def on_dot_press(self, instance):
		if "." not in self.current:
			self.current += "."
		self.label.text = self.current
		self.state = Calculator.State.NUMBER
	
	def on_validation_press(self, instance):
		if self.state != Calculator.State.DEFAULT:
			self.__operate()
		value = float(self.buffer)
		self.buffer = 0
		self.listener.onResultConfirmationPress(value)
	
	def on_reset_press(self, instance):
		self.current = "0"
		self.label.text = self.current

