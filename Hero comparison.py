from pprint import pprint
import requests

class Hero:
	def __init__(self, name):
		self.name = name
		self.url = "https://superheroapi.com/api/2619421814940190//search/" + self.name
		self.response = requests.get(self.url)
		self.stat_list = self.response.json()
		self.info = self.stat_list.get('results')

	def hero_intelegence(self):
		for dic in self.info:
			name1 = dic.get('name')
			stats = dic.get('powerstats')
			if name1 == self.name:
				intelligence = stats.get('intelligence')
			return intelligence

	def hero_comparison(self, other):
		if self.hero_intelegence() > other.hero_intelegence():
			print(f'{self.name} "умнее" {other.name}')
		elif self.hero_intelegence() < other.hero_intelegence():
			print(f'{other.name} "умнее" {self.name}')
		elif self.hero_intelegence() == other.hero_intelegence():
			print("Ничья")


Captain_America = Hero("Captain America")
Hulk = Hero("Hulk")
print(Hulk.hero_intelegence())
print(Captain_America.hero_intelegence())
Hulk.hero_comparison(Captain_America)







#def test_request():
#	url = "https://httpbin.org/get"
#	response = requests.get(url)
#	print(response.status_code)
#	pprint(response)

#test_request()

