from nicegui import ui
from components.leftdrawer import LeftDrawer



def create():
    LeftDrawer()
    ui.label("Kontakt").classes('text-2xl font-bold text-black')
    
    with ui.label(
        "För frågor om bokning, tillgänglighet eller andra funderingar:").classes('text-lg text-gray-700'):
        pass
    with ui.card().classes('p-6 space-y-3 shadow-md'):
        
        ui.label("📧 E-post, 📞 Telefon").classes('text-lg font-semibold')
        ui.label("Rickard Anderberg").classes('text-lg text-gray-800')
        ui.label("robalo54@gmail.com").classes('text-lg text-gray-800') 
        ui.label("076‑8437888").classes('text-lg text-gray-800')


        ui.separator()

        ui.label("📍 Adress till huset").classes('text-lg font-semibold')
        ui.label("Falkstigen 1, 84092 Vemdalen").classes('text-lg text-gray-800')

    
