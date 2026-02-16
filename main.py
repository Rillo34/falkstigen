from nicegui import ui, app
from pages import home, pictures, prices, map_and_drawing, contact, about
import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
app.add_static_files('/static', str(BASE_DIR / 'static'))


@ui.page('/')
def home_page():
    home.create()

@ui.page('/pictures')
def pictures_page():
    pictures.create()

@ui.page('/prices')
def prices_page():
    prices.create()

@ui.page('/about')
def about_page():
    about.create()

@ui.page('/contact')
def contact_page():
    contact.create()

@ui.page('/map_and_drawing')
def map_and_drawing_page():
    map_and_drawing.create()

port = int(os.environ.get("PORT", 8080))
ui.run(host="0.0.0.0", port=port)
