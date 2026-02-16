from nicegui import ui, app
from pages import home, pictures, prices, map_and_drawing, contact, about


app.add_static_files('/static', 'static')


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

ui.run()
