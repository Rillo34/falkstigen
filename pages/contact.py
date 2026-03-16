from nicegui import ui
from components.leftdrawer import LeftDrawer


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
    ui.label("Kontakt").classes('text-2xl font-bold text-black')
    
    with ui.label(
        "För frågor om bokning, tillgänglighet eller andra funderingar:").classes('text-lg text-gray-700'):
        pass
    with ui.card().classes('p-6 space-y-3 shadow-md'):
        
        ui.label("📧 E-post, 📞 Telefon").classes('text-lg font-semibold')
        ui.label("robalo54@gmail.com").classes('text-lg text-gray-800') 
        ui.label("076‑8437888").classes('text-lg text-gray-800')

        ui.separator()

        ui.label("📍 Adress").classes('text-lg font-semibold')
        ui.label("Falkstigen 1, 84092 Vemdalen").classes('text-lg text-gray-800')

    ui.label(
        "\nUthyrare:\n"
        "Rickard Anderberg\n"
        
    ).classes('text-lg text-gray-600 whitespace-pre-line')  # vänster + radbrytningar

