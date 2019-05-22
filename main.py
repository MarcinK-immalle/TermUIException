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

class MyAppExceptions(ValueError):
    pass

class PassToShortException(MyAppExceptions):
    pass

class StartsWithAException(MyAppExceptions):
    pass

class OutOfRangeException(MyAppExceptions):
    pass



def validatePass(password):
    if len(password) < 3:
        raise  PassToShortException
    if password.startswith('A'):
        raise StartsWithAException

def validateNum(number):
    if number < 1 or number > 4:
        raise OutOfRangeException



input = ""

input = click.prompt('Enter your password ', type=str)
print(input)

try:
    validatePass(input)
except PassToShortException:
    print("Password needs to be longer")
except StartsWithAException:
    print("Password cannot start with A")


input = click.prompt("Choose a number: \n1, 2, 3, 4 \n", type=int)
validateNum(input)


try:
    validatePass(input)
except OutOfRangeException:
    print("U need to choose out of the avilable numbers")