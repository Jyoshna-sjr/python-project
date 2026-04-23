import json 
data = { "name": "Milind", "course": "Data Science", "skills": ["Python", "SQL", "Machine Learning"] } 
# Create JSON file with open("data.json", "w") as file: json.dump(data, file, indent=4) print("JSON file created successfully!")

import json # Open and read JSON file with open("data.json", "r") as file: data = json.load(file) print(data)

