from nicegui import ui
from components.leftdrawer import LeftDrawer
from pathlib import Path

# Root av projektet
BASE_DIR = Path(__file__).resolve().parent.parent
image_folder = BASE_DIR / 'static'

def sort_key(filename):
    # Tar allt före första '-' och gör om till int
    num = filename.split('-', 1)[0]
    return int(num)

# Läs in alla bilder med '-' i filnamnet
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
    i = 0
    with ui.grid().classes('grid grid-cols-1 sm:grid-cols-2 md:grid-cols-5 gap-4'):
        for filename in image_files:
            with ui.card():
                ui.image(f'/static/{filename}').classes('w-64 h-auto')
                ui.label(label_list[i]).classes('text-lg')
            i += 1
