#! python3

#This is a tutorial on the rich module.
#The rich module modifies text printed to the terminal to support
#bolding, italics, underlines, colors, and more.

from rich.console import Console

console = Console()

console.print('Text')
console.print('Bold text', style="bold")
console.print('Bold underline text', style="bold underline")
console.print('Bold underline green text', style="bold underline green")
console.print('Color and background', style="red on white")
console.print('[bold]All bold, [cyan]some[/] colored text[/]')


#Rich text objects
from rich.text import Text

text = Text('Hello world')
text.stylize("bold magenta", 0, 6)
console.print(text)


#Themes
from rich.theme import Theme

custom_theme = Theme({"success": "green", "error": "bold red"})
console = Console(theme=custom_theme)

console.print("Operation success", style="success")
console.print("Operation failed", style="error")
console.print("Operation [error]failed[/error]")


#Log printout (Prints timestamps and line that was run)
import time

console = Console()

for i in range(10):
    console.log(f'Doing important stuff... {i}')
    time.sleep(0.2)


#Nicer error tracebacks
from rich.traceback import install
install()

myList=[1,2,3]
for i in range(10):
    print(myList[i])
