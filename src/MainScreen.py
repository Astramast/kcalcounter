from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from NumberHolder import NumberHolder
from Calculator import Calculator
from Database import Database

class MainScreen(Screen):
	def __init__(self, number, **kwargs):
		super(MainScreen, self).__init__(**kwargs)
		self.main_number = NumberHolder(number, self)
		history_button = Button(text='History', on_press=self.onHistoryButtonPress)
		reset_button = Button(text='Reset', on_press=self.onResetButtonPress)
		calculator = Calculator(self)

		# Layouts
		button_layout = BoxLayout(orientation='horizontal')
		button_layout.add_widget(history_button)
		button_layout.add_widget(reset_button)

		main_layout = BoxLayout(orientation='vertical')
		main_layout.add_widget(self.main_number)
		main_layout.add_widget(button_layout)
		main_layout.add_widget(calculator)
		self.add_widget(main_layout)
	
	def onNumberConfirmationPress(self, number):
		with Database() as db:
			db.add(number)
		self.main_number.setNumber(0)

	def onHistoryButtonPress(self, instance):
		self.manager.current = 'history'

	def onResetButtonPress(self, instance):
		self.main_number.setNumber(0)

	def onResultConfirmationPress(self, number):
		self.main_number.setNumber(self.main_number.number + number)

