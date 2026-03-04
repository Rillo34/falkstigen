from nicegui import ui
from components.leftdrawer import LeftDrawer

def create():
    LeftDrawer()
    ui.label("Kontakt").classes('text-2xl font-bold text-black')


    with ui.card().classes('p-6 space-y-3 shadow-md'):
        
        ui.label("📧 E-post").classes('text-lg font-semibold')
        ui.label("robalo54@gmail.com").classes('text-lg text-gray-800')

        ui.separator()

        ui.label("📞 Telefon").classes('text-lg font-semibold')
        ui.label("076‑8437888").classes('text-lg text-gray-800')

        ui.separator()

        ui.label("📍 Adress").classes('text-lg font-semibold')
        ui.label("Falkstigen 1, 84092 Vemdalen").classes('text-lg text-gray-800')

    ui.label(
        "Fam Anderberg\n"
        "Svartensgatan 26\n"
        "11620 Stockholm"
    ).classes('text-md text-gray-600 whitespace-pre-line')  # vänster + radbrytningar

