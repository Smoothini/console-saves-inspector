import flet as ft
import os
import parsers.ps3 as ps3
import parsers.psv as psv


def main(page: ft.Page):
    page.title = "Console Saves Inspector"
    page.scroll = "auto"

    console = ps3

    top_text = ft.Text("Select a folder with your savegames:", size=20)
    bottom_text = ft.Text("Made by smoothini!", size=12)

    def dropdown_changed(e):
        selected = e.control.value
        nonlocal console
        if selected == "ps3":
            console = ps3
            print("PS3 context selected")
        elif selected == "psv":
            console = psv
            print("PS Vita context selected")
        page.update()

    dropdown = ft.Dropdown(
        label="Pick one",
        options=[
            ft.dropdown.Option("ps3", "PlayStation 3"),
            ft.dropdown.Option("psv", "PlayStation Vita"),
        ],
        value="ps3",  # initial value
        on_change=dropdown_changed
    )

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
        ids = console.get_titleids()
        try:
            subfolders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
            
            table_data.clear()
            print(f"found {len(subfolders)} subfolders")
            for f in subfolders:
                game, media, region = console.parse_title(f[:9], ids)
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
        dropdown,
        pick_button,
        selected_folder,
        table,
        bottom_text,
    )

ft.app(target=main)
