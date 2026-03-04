from nicegui import ui
from components.leftdrawer import LeftDrawer

def create():
    LeftDrawer()
    ui.label("Priser och tillgänglighet").classes('text-2xl font-bold text-black')

    columns = [
    {'name': 'vecka', 'label': 'Vecka', 'field': 'vecka', 'required': True, 'align': 'left'},
    {'name': 'pris', 'label': 'Pris (kr)', 'field': 'pris', 'sortable': False},
    {'datum': 'Datum', 'label': 'Datum', 'field': 'datum', 'sortable': True},
    {'name': 'tillgänglighet', 'label': 'Tillgänglighet', 'field': 'tillgänglighet', 'sortable': True},

    ]
    rows = [
        {'vecka': 'Vecka 5 2027', 'pris': 18000, 'datum': '30/1-6/2', 'tillgänglighet': 'Bokad', 'classes': 'bg-red-100'},
        {'vecka': 'Vecka 6 2027', 'pris': 19000, 'datum': '6/2-13/2', 'tillgänglighet': 'Tillgänglig'},
        {'vecka': 'Vecka 7 2027', 'pris': 31000, 'datum': '13/2-20/2', 'tillgänglighet': 'Tillgänglig'},
        {'vecka': 'Vecka 8 2027', 'pris': 34000, 'datum': '20/2-27/2', 'tillgänglighet': 'Tillgänglig'},
        {'vecka': 'Vecka 9 2027', 'pris': 39000, 'datum': '27/2-6/3', 'tillgänglighet': 'Tillgänglig'},
        {'vecka': 'Vecka 10 2027', 'pris': 22000, 'datum': '6/3-13/3', 'tillgänglighet': 'Tillgänglig'},
        {'vecka': 'Vecka 11 2027', 'pris': 22000, 'datum': '13/3-20/3', 'tillgänglighet': 'Tillgänglig'},
    ]
    table = ui.table(columns=columns, rows=rows, row_key='vecka')
    
    ui.label("Städning är inkluderat i hyran. Byte sker lördagar och endast hela veckor.").classes('text-md font-bold text-black')