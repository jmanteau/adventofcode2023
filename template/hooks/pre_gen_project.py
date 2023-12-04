import datetime
import json

# Define the path to cookiecutter.json
config_path = "../cookiecutter.json"

# Read the existing config
with open(config_path, "r") as file:
    config = json.load(file)

# Update the 'day' value with the current day
config["day"] = datetime.datetime.now().strftime("%d")

# Write the updated config back to cookiecutter.json
with open(config_path, "w") as file:
    json.dump(config, file, indent=4)
