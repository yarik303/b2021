import colorama
import inspect


print(colorama. __name__)

print(inspect.ismodule(colorama))
print(inspect.isclass(colorama))
print(inspect.isfunction(colorama))
print(inspect.getmodule(colorama))

print('\033[31m' + 'Colorama is a library that makes support for colors in text')
print('\x1b[1;33m' + 'its used by many people according to pypistats.org Downloads for colorama last month: 120,166,954')
print('\x1b[3;33m' + 'Makes ANSI escape character sequences (for producing colored terminal text and cursor positioning) work under MS Windows.')
print('\033[39m') # and reset to default color
print("and that preety much it.")