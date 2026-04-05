from nicegui import ui, app
from components.leftdrawer import LeftDrawer
import os

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-GELVE5TP2P"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-GELVE5TP2P');
</script>



def create():
    LeftDrawer()

    with ui.element('div').classes(
        'relative w-full bg-center bg-no-repeat flex items-center'
        'min-h-[450px] sm:min-h-[550px] md:min-h-[650px] lg:min-h-[80vh]'  # mer flexibel höjd
    ).style(
        'background-image: url("/static/2-fasad.jpg");'
        'background-size: contain;'  # ← nyckeländringen!
    ):
        with ui.column().classes('bg-black/40 p-8 rounded-xl ml-6 max-w-xl'):
            ui.label('Falkstigen 1 – ').classes(
                'text-4xl sm:text-5xl md:text-6xl font-bold text-white drop-shadow-xl'
            )
            ui.label('12p hus på Skalsterrassen, Vemdalsskalet').classes(
                'text-4xl sm:text-5xl md:text-6xl font-bold text-white drop-shadow-xl'
            )
            ui.label('Mittemot Hovdebacken • Skalsterrassen • Bredvid Hildings backe • Nära till allt').classes(
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
            ui.icon('fireplace').classes('text-amber-700')
            ui.label('Öppen spis')

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

