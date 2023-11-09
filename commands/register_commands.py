import requests
import yaml


TOKEN = "MTE3MTcxNjgyNzQ1MDE4MzcwMA.G1be0F.NYgbAFji8dqCTPwYu1T7IH5b0Y1rf_ahJ4kQQ4"
APPLICATION_ID = "1171716827450183700"
URL = f"https://discord.com/api/v9/applications/{APPLICATION_ID}/commands"


with open("discord_commands.yaml", "r") as file:
    yaml_content = file.read()

commands = yaml.safe_load(yaml_content)
headers = {"Authorization": f"Bot {TOKEN}", "Content-Type": "application/json"}

# Send the POST request for each command
for command in commands:
    response = requests.post(URL, json=command, headers=headers)
    command_name = command["name"]
    print(f"Command {command_name} created: {response.status_code}")
