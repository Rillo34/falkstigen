# from nicegui import ui

# class LeftDrawer:
#     def __init__(self):
#         with ui.left_drawer(bordered=True, elevated=True, fixed=False).props('width=240 bordered'):
#             ui.menu()
#             ui.button('Hem', color='purple', icon='house',on_click=lambda: ui.navigate.to('/')).classes('w-40')
#             ui.button('Bilder', on_click=lambda: ui.navigate.to('/pictures')).classes('w-40')
#             ui.button('Priser', on_click=lambda: ui.navigate.to('/prices')).classes('w-40')
#             ui.button('Om huset', on_click=lambda: ui.navigate.to('/about')).classes('w-40')
#             ui.button('Karta och planlösning', on_click=lambda: ui.navigate.to('/map_and_drawing')).classes('w-40')
#             ui.button('Kontakt', on_click=lambda: ui.navigate.to('/contact')).classes('w-40')


from nicegui import ui


class LeftDrawer:
    def __init__(self):
        
            # Hamburger-knapp – bara på mobil / mindre skärmar
        with ui.row().classes('items-center gap-4 p-2'):
            ui.button(icon='menu', on_click=lambda: drawer.toggle()).props('flat round color=primary')
            # ui.label('Menu').classes('text-xl font-bold')

        with ui.left_drawer(value=False, bordered=True, elevated=True) as drawer:
            drawer.props('width=240 bordered')

            with ui.list().classes('w-full bg-transparent'):
                # Hem (med purple som tidigare)
                with ui.item(on_click=lambda: ui.navigate.to('/')).props('tag=a'):
                    with ui.item_section():
                        ui.item_label('Hem').classes('text-lg text-purple-700')
                    with ui.item_section().props('side'):
                        ui.icon('house').classes('text-purple-700')

                ui.separator()

                with ui.item(on_click=lambda: ui.navigate.to('/pictures')).props('tag=a'):
                    with ui.item_section():
                        ui.item_label('Bilder').classes('text-lg')
                    with ui.item_section().props('side'):
                        ui.icon('photo_library')

                with ui.item(on_click=lambda: ui.navigate.to('/prices')).props('tag=a'):
                    with ui.item_section():
                        ui.item_label('Priser').classes('text-lg')
                    with ui.item_section().props('side'):
                        ui.icon('euro')

                with ui.item(on_click=lambda: ui.navigate.to('/about')).props('tag=a'):
                    with ui.item_section():
                        ui.item_label('Om huset').classes('text-lg')
                    with ui.item_section().props('side'):
                        ui.icon('info')

                with ui.item(on_click=lambda: ui.navigate.to('/map_and_drawing')).props('tag=a'):
                    with ui.item_section():
                        ui.item_label('Karta och planlösning').classes('text-lg')
                    with ui.item_section().props('side'):
                        ui.icon('map')

                with ui.item(on_click=lambda: ui.navigate.to('/contact')).props('tag=a'):
                    with ui.item_section():
                        ui.item_label('Kontakt').classes('text-lg')
                    with ui.item_section().props('side'):
                        ui.icon('contact_mail')