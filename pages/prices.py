from nicegui import ui
from components.leftdrawer import LeftDrawer

def create():
    LeftDrawer()
    ui.label("Detta är sidan 'Priser'. Här kan du lägga till information om priser för att hyra huset, inklusive säsongspriser och eventuella rabatter.").classes('text-lg text-gray-600 mt-6')