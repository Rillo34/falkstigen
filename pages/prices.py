from nicegui import ui
from components.leftdrawer import LeftDrawer





def create():
    LeftDrawer()
    ui.label("Priser och tillgänglighet").classes('text-2xl font-bold text-black')

    columns = [
    {'name': 'vecka', 'label': 'Vecka', 'field': 'vecka', 'required': True, 'align': 'left'},
    {'name': 'pris', 'label': 'Pris (kr)', 'field': 'pris', 'sortable': False},
    {'name': 'datum', 'label': 'Datum', 'field': 'datum', 'sortable': True},
    {'name': 'status', 'label': 'Tillgänglighet', 'field': 'status', 'sortable': True},
    {'name': 'comment', 'label': 'Noteringar', 'field': 'comment', 'sortable': False, 'align': 'center'},
    ]

    rows = [
        {'vecka': 'v52 2026', 'pris': 34000, 'datum': '20/12-27/12', 'status': 'Tillgänglig', 'comment': 'OBS: byte söndag'},
        {'vecka': 'v53 2026', 'pris': 40000, 'datum': '27/12-3/1', 'status': 'Tillgänglig', 'comment': 'OBS: byte söndag'},
        {'vecka': 'Vecka 5 2027', 'pris': 18000, 'datum': '30/1-6/2', 'status': 'Bokad'},
        {'vecka': 'Vecka 6 2027', 'pris': 20000, 'datum': '6/2-13/2', 'status': 'Tillgänglig'},
        {'vecka': 'Vecka 7 2027', 'pris': 31000, 'datum': '13/2-20/2', 'status': 'Tillgänglig'},
        {'vecka': 'Vecka 8 2027', 'pris': 35000, 'datum': '20/2-27/2', 'status': 'Tillgänglig'},
        {'vecka': 'Vecka 9 2027', 'pris': 40000, 'datum': '27/2-6/3', 'status': 'Tillgänglig'},
        {'vecka': 'Vecka 10 2027', 'pris': 22000, 'datum': '6/3-13/3', 'status': 'Tillgänglig'},
        {'vecka': 'Vecka 11 2027', 'pris': 22000, 'datum': '13/3-20/3', 'status': 'Tillgänglig'},
    ]
    table = ui.table(columns=columns, rows=rows, row_key='vecka')
    table.add_slot('body', r'''
        <q-tr :props="props" :class="props.row.status === 'Bokad' ? 'bg-red-4 text-strike' : 'bg-green-1'">
            <q-td v-for="col in props.cols" :key="col.name" :props="props">
                {{ col.value }}
            </q-td>
        </q-tr>
    ''')



    ui.label("Städning är inkluderat i hyran. Byte sker lördagar om inte annat sägs och endast hela veckor.\n Tillträde efter kl 16 och avresa senast kl 10.").classes('text-md text-black')
    ui.label("För frågor om bokning, tillgänglighet eller andra funderingar, se Kontakt").classes('text-md text-black')
