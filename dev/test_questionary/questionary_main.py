import questionary

name = questionary.text("What is your username:").ask()
password = questionary.password("What's your password:").ask()

print(f"your name: {name}, pw: {password}")

amazed = questionary.confirm("Are you amazed?", default=False).ask()
choice = questionary.select("What do you want to do?", choices=["A", "B", "C"],).ask()
checks = questionary.checkbox("What do you like?", choices=["foo", "bar", "baz"]).ask()

req_file = questionary.path("What is the path to your requirements file?").ask()
print(req_file)
