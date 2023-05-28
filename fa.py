print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")
try:
    try:
        print("start cod")
        print(10/0)
        print("no error")
    except (NameError, ZeroDivisionError):
        print("we have an error")
except (NameError, ZeroDivisionError):
    print("we have an error")
print("code after capsule")

def chek(var_1):
    if type(var_1)!=str:
        raise TypeError(f"Sorry, we can't work with {type(var_1)}," f"we need class str")
    else:
        return var_1
first_var=10
chek(first_var)

class BuildingError(Exception):
    def __str__(self):
        return f"З такоюб кількістю матеріалів будинок побудувати не можливо"
def check_material(amount_material, limit_value):
    if amount_material>limit_value:
        return f"Матеріалу достатньо"
    else:
        raise BuildingError(amount_material)
materials=123
check_material(materials,300)

class HomeworkError(Exception):
    def __str__(self):
        return f"Ти не доробив домашнє"
def check_homework(amount_of_homework, finishes):
    if amount_of_homework>finishes:
        return f"Доробив все домашнє"
    else:
        raise HomeworkError(amount_of_homework)
homework=15
check_homework(homework,15)