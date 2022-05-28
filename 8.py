import colorama
class BuildingError(Exception):
    def __str__(self):
        return f"With so much material the house that can not build!"
def CheckMaterial(amount_Of_Material,limit):
    if amount_Of_Material > limit:
        return "enough material"
    else:
        raise BuildingError(amount_Of_Material)
CheckMaterial(int(input()),500)
a = int(input())
try:
    print(10 / a)
    print("sucessful")
except ZeroDivisionError:
    print(colorama.Fore.RED + "It is~nt possible to divide by zero")
except TypeError:
    print(colorama.Fore.RED + "It is~nt possible to divide by str")
except NameError:
    print(colorama.Fore.RED + "You are accessing an object that does~nt exist")
else:
    print(colorama.Fore.GREEN + "Nothing went wrong")
finally:
    print(colorama.Fore.CYAN + "The try except is finished")


input()