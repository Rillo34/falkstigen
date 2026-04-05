from nicegui import ui
from components.leftdrawer import LeftDrawer
from pathlib import Path




# Root av projektet
BASE_DIR = Path(__file__).resolve().parent.parent
image_folder = BASE_DIR / 'static'

def sort_key(filename):
    return int(filename.split('*')[1])


image_files = sorted(
    [f.name for f in image_folder.iterdir() if f.is_file() and '*' in f.name],
    key=sort_key
)

label_list = [
    "Planlösning entreplan",
    "Planlösning loft",
    "Pistkarta"
]

def create():
    LeftDrawer()
    
    with ui.element('div').classes('mx-auto w-full max-w-7xl px-4 py-6'):
        # Masonry-liknande: columns istället för grid → automatisk packning
        with ui.element('div').classes(
            # 'columns-1 gap-4 sm:columns-2 md:columns-3 lg:columns-4 xl:columns-5'
            'columns-1'
        ):
            for i, filename in enumerate(image_files):
                with ui.card().classes(
                    'overflow-hidden break-inside-avoid mb-4 '
                    'hover:shadow-xl transition-shadow duration-300 rounded-lg'
                ):
                    # Bilden fyller bredden, behåller SIN NATURLIGA proportion (ingen fast aspect!)
                    ui.image(f'/static/{filename}').classes(
                        'w-full h-auto object-cover rounded-t-lg'  # rounded bara upptill för snyggt kort
                    ).props('loading="lazy"')  # lazy loading för snabbare sida
                    
                    # Label under, med lite bakgrund för kontrast
                    ui.label(label_list[i]).classes(
                        'text-base md:text-lg text-center p-3 bg-gray-50 dark:bg-gray-800'
                    )
    
    # # Din karta efter galleriet (fullbredd)
    # ui.image('/static/map*2*Plan1.jpg').classes(
    #     'w-full mt-8 rounded-lg shadow-lg object-cover'
    # )