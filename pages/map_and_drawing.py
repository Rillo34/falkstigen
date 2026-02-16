from nicegui import ui
from components.leftdrawer import LeftDrawer

def create():
    LeftDrawer()

    ui.label("Detta är sidan 'Karta och ritning'. Här kan du lägga till en karta över området och eventuella ritningar av huset.").classes('text-lg text-gray-600 mt-6')