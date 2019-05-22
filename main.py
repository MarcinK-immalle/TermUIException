# Maak een Console UI waarin je de gebruiker om user input vraagt.
# Daarna moet je deze user-input valideren en een heel specifieke exception werpen uit je eigen exception-hierarchie.
# Vbdn:
# - Wachtwoordvereisten (minimum lengte, gebruik van een speciaal karakter, ...)
# - Een menu-systeem waarin elk menu-item een nummer heeft en een exception wordt geworpen bij een niet bestaand nummer
# - User input die moet beginnen met een hoofdletter
# - ...
# Extra: vergelijk je eigen user-input afhandeling met die van de click-library
# https://click.palletsprojects.com/en/7.x/prompts/
# Vbdn:
# - Gebruik `click.prompt` om de gebruiker om een getal te vragen. Wat gebeurt er als er een letter wordt ingegeven?

import click

input = ""

input = click.prompt('Enter your name ', type=str)

print(input)