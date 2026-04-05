from nicegui import ui
from components.leftdrawer import LeftDrawer

about_text = """
    Välkomna till Falkstigen !
    
    Exklusivt 12 bäddars, 160m2 boende på soliga Skalsterrassen mitt i Vemdalsskalet med nära till allt. Bilen kan man låta stå. 
    Huset har en härlig utsikt mot Hovdemassivet och backarna Hovde och Turisten.

    Huset byggdes 2011  och ligger längst ner på Skalsterrassen (bredvid Hildings backe) i ett av de mest attraktiva områdena i Vemdalsskalet. 
    Det består av tre olika lägenheter, detta är den stora och ljusa övervåningen med två våningar.

    Till backen tar man sig genom att glida ner mot skidbron och över till liften Hovde Express, det är drygt 100 meter från huset. Man når huset till fots från alla nedfarter på grund av det centrala läget.
    Det är drygt 100 meter till ICA, Vemdalsskalets högfjällshotell och Skalets torg med restauranger, Skistarshop, afterski och bageri. Spårcentralen ligger cirka 400 meter bort. Parkering finns i anslutning till entrén på övervåningen eller på den stora gårdsplanen, där finns det plats för 6–8 bilar och två st laddare typ 2.
    
    Byte sker på lördagar och endast hela veckor hyrs ut. Städning är inkluderat i hyran.

    Vissa av bilderna har olika möbler eftersom vissa möbler uppgraderats.
    """

# Huset har 12 bäddar på 160m2 fördelat enligt följande:
#     - 6 sovrum (ett med TV), två med våningssäng. Ett sovrum ligger på loftet där det också finns en WC.
#     - 2 badrum med dusch (ett med dubbeldusch)
#     - 2 separata WC
#     - 2 bastu: torrbastu och ångbastu
#     - Kök med spishäll, ugn, kyl/frys, diskmaskin, micro och matplats
#     - Stort vardagsrum med öppen spis, matplats, soffgrupp och TV
#     - Allrum med TV på loftet
#     - Omklädningsrum med tvättmaskin, torktumlare, torkskåp och pjäxtorkare
#     - Skidförråd
#     - Altan i söderläge med sol och utsikt
#     - Wifi

def bullet_point(icon: str, text: str, detail: str = '', icon_color: str = 'blue-600'):
    with ui.row().classes('items-start gap-3 py-1'):
        # Ikonen fungerar som bullet
        ui.icon(icon).classes(f'text-2xl {icon_color} mt-0.5')
        
        with ui.column().classes('gap-0'):
            # Huvudtext och detaljtext i en kolumn
            ui.label(text).classes('text-lg font-medium text-slate-800 line-height-tight')
            if detail:
                ui.label(detail).classes('text-sm text-slate-500')

def create():
    LeftDrawer()
    with ui.row().classes('items-center gap-6 text-lg'):
        with ui.column().classes('w-1/2 pr-8 border-r border-gray-200'):
            ui.label("Om huset och info").classes('text-2xl font-bold text-black')
            ui.label(text =about_text).classes('text-lg  mt-6 whitespace-pre-line')
        with ui.column().classes('w-1/3 gap-2'):
            ui.label("Faciliteter").classes('text-3xl font-bold mt-8 mb-4')
            bullet_point('bed', '6 sovrum', '12 bäddar totalt, inkl. loftrum med WC och rum med våningssängar.')
            bullet_point('shower', '2 badrum', 'Duschrum, varav ett med dubbeldusch.')
            bullet_point('wc', '2 separata WC', 'Utöver badrummens faciliteter.')
            bullet_point('hot_tub', '2 bastu', 'Både torrbastu och ångbastu finns.', 'text-orange-500')
            bullet_point('restaurant', 'Fullutrustat kök', 'Spishäll, ugn, kyl/frys, diskmaskin och micro.', 'text-emerald-600')
            bullet_point('weekend', 'Stort vardagsrum', 'Öppen spis, matplats och soffgrupp.', 'text-amber-700')
            bullet_point('tv', 'Allrum på loftet', 'Extra sällskapsytor med TV.', 'text-indigo-500')
            bullet_point('local_laundry_service', 'Klädvård', 'Tvättmaskin, torktumlare, torkskåp och pjäxtorkare.')
            bullet_point('inventory_2', 'Skidförråd')
            bullet_point('wb_sunny', 'Altan i söderläge')
            bullet_point('wifi', 'Wifi')
            bullet_point('ev_station', 'Laddplats', 'Två laddare typ 2 tillgängliga ', 'text-green-600')

    with ui.card().tight().classes('bg-red-50 border-l-4 border-red-600 p-4 mt-8 w-full'):
        with ui.row().classes('items-center gap-3'):
            ui.icon('warning', color='red-600').classes('text-2xl')
            ui.label("VIKTIG INFORMATION").classes('font-bold text-red-800')
            ui.label("Husdjur är absolut förbjudna (kraftig allergi i familjen) och rökning är inte tillåten i huset.").classes('text-red-700 font-medium mt-1')

# Vi skapar ett grid som har 1 kolumn på mobil, 2 på tablet och 3 på desktop
    