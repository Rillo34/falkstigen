from nicegui import ui
from components.leftdrawer import LeftDrawer

def create():
    LeftDrawer()
    about_text = """
    Välkomna till Skalsterrassen och ett boende mitt i Vemdalsskalet med nära till allt. 
    
    
    Huset byggdes 2011 och består av tre olika lägenheter, detta är den stora och ljusa övervåningen med två våningar.

    Läget är optimalt, längst ner på Skalsterrassen (bredvid Hildings backe) i Vemdalsskalet och har en härlig vid utsikt rakt in i Hovdemassivet och backarna Hovde och Turisten. Huset är exklusivt, med bland annat dubbla bastu (torr- och ångbastu).

    Till backen tar man sig genom att glida ner mot skidbron och över till liften Hovde Express, det är cirka 150 meter från huset. Man når huset till fots från alla nedfarter på grund av det centrala läget.

    Det är drygt 100 meter till ICA, Vemdalsskalets högfjällshotell och Skalets torg med restauranger, Skistarshop, afterski och bageri. Spårcentralen ligger cirka 400 meter bort. Parkering finns i anslutning till entrén på övervåningen eller på den stora gårdsplanen, där finns det plats för 6–8 bilar och till säsongen två laddare typ 2.

    Huset har 12 bäddar och är på totalt 158 m2 fördelat enligt följande:
    - 6 sovrum (ett med TV), två med våningssäng. Ett sovrum ligger på loftet där det också finns en WC.
    - 2 badrum med dusch (ett med dubbeldusch)
    - 2 separata WC
    - 2 bastur: torrbastu och ångbastu
    - Kök med spishäll, ugn, kyl/frys, diskmaskin, micro och matplats
    - Stort vardagsrum med öppen spis, matplats, soffgrupp och TV
    - Allrum med TV på loftet
    - Omklädningsrum med tvättmaskin, torktumlare, torkskåp och pjäxtorkare
    - Skidförråd
    - Altan i söderläge med sol och utsikt
    - Wifi

    Vissa av bilderna har olika möbler eftersom vissa möbler uppgraderats.

    OBS: Husdjur är absolut förbjudna (kraftig allergi i familjen) och rökning är inte tillåten i huset.
    """


    ui.label(text =about_text).classes('text-lg text-gray-600 mt-6 whitespace-pre-line')