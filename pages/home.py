from nicegui import ui, app
from components.leftdrawer import LeftDrawer
import os

app.add_static_files('/static', '/home/rickard/Python/Falkstigen_web/static')


def create():
    LeftDrawer()

    with ui.element('div').classes(
        'relative h-[450px] sm:h-[550px] md:h-[650px] w-full bg-cover bg-center flex items-center'
    ).style(
        'background-image: url("/static/2-fasad.jpg")'
    ):
        with ui.column().classes('bg-black/40 p-8 rounded-xl ml-6 max-w-xl'):
            ui.label('Falkstigen 1 – 160m2 mitt i Vemdalsskalet').classes(
                'text-4xl sm:text-5xl md:text-6xl font-bold text-white drop-shadow-xl'
            )
            ui.label('12 bäddar • Skalsterrassen • 2st Bastu • Nära till allt • Inga husdjur').classes(
                'text-xl sm:text-2xl text-white mt-4 drop-shadow'
            )
    with ui.row().classes('items-center gap-6 text-lg'):
        with ui.row().classes('items-center gap-2'):
            ui.icon('downhill_skiing').classes('text-indigo-600')
            ui.label('100m till Hovdebacken')
        with ui.row().classes('items-center gap-2'):
            ui.icon('whatshot').classes('text-orange-600')
            ui.label('Torrbastu')

        with ui.row().classes('items-center gap-2'):
            ui.icon('spa').classes('text-blue-500')
            ui.label('Ångbastu')

        with ui.row().classes('items-center gap-2'):
            ui.icon('wc')
            ui.label('Omklädningsrum')

        with ui.row().classes('items-center gap-2'):
            ui.icon('bed')
            ui.label('12 bäddar')

        with ui.row().classes('items-center gap-2'):
            ui.icon('ev_station').classes('text-green-600')
            ui.label('Laddplats')

        with ui.row().classes('items-center gap-2'):
            ui.icon('location_on').classes('text-red-500')
            ui.label('Centralt')

        with ui.row().classes('items-center gap-2'):
            ui.icon('square_foot').classes('text-gray-600')
            ui.label('160 m²')

