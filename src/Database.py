from kivy.app import App
import os


class Database:
	def __init__(self):
		self.filename = os.path.join(App.get_running_app().user_data_dir, "data.txt")
		self.history = self.load()

	def load(self):
		with open(self.filename, "r", encoding="utf-8") as f:
			history = [float(line) for line in f]
		return history
	
	def add(self, number):
		self.history.append(number)
	
	def get_history(self):
		return self.load()
	
	def save(self):
		with open(self.filename, "w", encoding="utf-8") as f:
			for number in self.history:
				f.write(str(number) + "\n")
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.save()
	
	def __enter__(self):
		return self

