#!/opt/homebrew/bin/python3

import json

input = 'data/schacon.repos.json'
output = 'chacon.csv'

with open(input, 'r') as file:
	data = json.load(file)

with open(output, 'w') as csv_file:
	for repo in data[:5]:
		name = repo.get('name', '')
		html_url = repo.get('html_url', '')
		updated_at = repo.get('updated_at', '')
		visibility = repo.get('visibility', '')

		csv_file.write(f"{name},{html_url},{updated_at},{visibility}\n")	
