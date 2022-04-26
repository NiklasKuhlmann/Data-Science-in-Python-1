import pandas as pd
class CrispDm():
	def __init__(self):
		pass

	def load(self):
		data = pd.read_csv("covtype.data")
		self.data = data
		print(data)

	def data_understanding(self, data=None):
		pass

	def data_preparation(self, data=None):
		# data = CrispDm.data_preparation_cleansing(data=data)
		return data

	def data_preparation_split(self, data=None, target=None):
		from sklearn.model_selection import train_test_split

		X_train, X_test, y_train, y_test = train_test_split(data,
															target,
															stratify=target,
															random_state=666
															)
		return X_train, y_train, X_test, y_test

	def modeling(self, x_train=None, y_train=None):
		model = {}

		return model

	def auswertung(self):
		pass

	def visuals(self):
		pass

c = CrispDm()
c.load()