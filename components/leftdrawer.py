from nicegui import ui

class LeftDrawer:
    def __init__(self):
        with ui.left_drawer(bordered=True, elevated=True, fixed=False).props('width=240 bordered'):
            ui.menu()
            ui.button('Hem', color='purple', icon='house',on_click=lambda: ui.navigate.to('/')).classes('w-40')
            ui.button('Bilder', on_click=lambda: ui.navigate.to('/pictures')).classes('w-40')
            ui.button('Priser', on_click=lambda: ui.navigate.to('/prices')).classes('w-40')
            ui.button('Om huset', on_click=lambda: ui.navigate.to('/about')).classes('w-40')
            ui.button('Karta och planlösning', on_click=lambda: ui.navigate.to('/map_and_drawing')).classes('w-40')
            ui.button('Kontakt', on_click=lambda: ui.navigate.to('/contact')).classes('w-40')

