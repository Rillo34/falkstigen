from nicegui import ui
from components.leftdrawer import LeftDrawer
from pathlib import Path

# Root av projektet
BASE_DIR = Path(__file__).resolve().parent.parent
image_folder = BASE_DIR / 'static'

def sort_key(filename):
    num = filename.split('-', 1)[0]
    return int(num)

image_files = sorted(
    [f.name for f in image_folder.iterdir() if f.is_file() and '-' in f.name],
    key=sort_key
)

label_list = [
    "Utsikt mot Hovdefjället",
    "Fasad",
    "Altan mot Hovdefjället",
    "Sovrum dubbelsäng",
    "Sovrum våningssäng",
    "Kök",
    "Storstuga",
    "Storstuga",
    "Loft",
    "Omklädningsrum",
    "Torrbastu",
    "Ångbastu",
    "Ångbastu",
    "Badrum vid ångbastu",
    "Badrum med dubbla duschar"
]

def create():
    LeftDrawer()
    
    with ui.grid().classes('grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4 p-4'):
        for i, filename in enumerate(image_files):
            with ui.card().classes('overflow-hidden'):  # Förhindrar att bilden sticker ut ur kortet
                # Bilden fyller hela bredden av kortet, behåller proportioner
                ui.image(f'/static/{filename}').classes('w-full h-auto object-cover')
                # Label centrerad, lite padding
                ui.label(label_list[i]).classes('text-lg text-center p-2')