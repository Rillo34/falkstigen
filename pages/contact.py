from nicegui import ui
from components.leftdrawer import LeftDrawer

def create():
    LeftDrawer()
    ui.label("Detta är sidan 'Kontakt'. Här kan du lägga till kontaktinformation, inklusive telefonnummer, e-postadress och eventuella kontaktformulär.").classes('text-lg text-gray-600 mt-6')