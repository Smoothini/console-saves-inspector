import flet as ft
import os

def get_titleids():
    ids = {}
    with open("titleid.txt", "r", encoding="utf-8") as file:
        for line in file:
            code = line[:9]
            title = line[10:]
            ids[code] = title
    return ids

def parse_title(title, ids):
    media = { #first
        "B": "Physical",
        "N": "Digital"
    }
    region = { #third
        "A": "Asia",
        "C": "China",
        "E": "Europe",
        "H": "Hong Kong",
        "J": "Japan",
        "K": "Korea",
        "U": "USA"
    }

    if title[0] in media.keys():
        media_type = media[title[0]]
    else:
        media_type = "Unknown"

    if title[2] in region.keys():
        region_type = region[title[2]]
    else:
        region_type = "Unknown"

    if title in ids.keys():
        game = ids[title]
    else:
        game = "Unknown"

    return game, media_type, region_type

def main(page: ft.Page):
    page.title = "PS3 Saves Inspector"
    page.scroll = "auto"

    top_text = ft.Text("Select a folder with your savegames:", size=20)
    bottom_text = ft.Text("Made by smoothini!", size=12)

    # Table and data
    table_data = []

    table = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Folder"), on_sort=lambda e: sort_table(e.column_index, e.ascending)),
            ft.DataColumn(label=ft.Text("Game"), on_sort=lambda e: sort_table(e.column_index, e.ascending)),
            ft.DataColumn(label=ft.Text("Region"), on_sort=lambda e: sort_table(e.column_index, e.ascending)),
            ft.DataColumn(label=ft.Text("Medium"), on_sort=lambda e: sort_table(e.column_index, e.ascending)),
        ],
        rows=[],
    )

    ids = get_titleids()

    def update_table():
        table.rows = [
            ft.DataRow(
                cells = [
                    ft.DataCell(ft.Text(row[0])),
                    ft.DataCell(ft.Text(row[1])),
                    ft.DataCell(ft.Text(row[2])),
                    ft.DataCell(ft.Text(row[3])),
                ]
            )
            for row in table_data
        ]
        page.update()

    def sort_table(col_index, ascending):
        nonlocal table_data
        table_data.sort(key=lambda x: x[col_index].lower(), reverse=not ascending)
        update_table()

    def load_folders(path):
        nonlocal table_data
        try:
            subfolders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
            
            table_data.clear()
            for f in subfolders:
                game, media, region = parse_title(f[:9], ids)
                table_data.append((f, game, region, media))
        except Exception as e:
            print("Error:", e)

    def on_folder_picked(e: ft.FilePickerResultEvent):
        if e.path:
            selected_folder.value = e.path
            load_folders(e.path)
            update_table()
            page.update()

    # File picker setup
    file_picker = ft.FilePicker(on_result=on_folder_picked)
    page.overlay.append(file_picker)

    selected_folder = ft.Text("No folder selected")

    pick_button = ft.ElevatedButton("Pick Folder", on_click=lambda _: file_picker.get_directory_path())


    # Layout
    page.add(
        top_text,
        pick_button,
        selected_folder,
        table,
        bottom_text,
    )

ft.app(target=main)
