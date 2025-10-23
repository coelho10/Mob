import flet as ft

from menu import criar_menu  # Importa a função do menu


def cadcliente_view(page: ft.Page):   
    
    # Cria o drawer usando a função importada
    drawer = criar_menu(page)
    
    return ft.View(       
        "/cadcliente",
        controls=[
            ft.IconButton(
                icon=ft.Icons.MENU,
                icon_size=30,
                tooltip="Abrir Menu",
                on_click=lambda e: page.open(drawer)
            ),            
            ft.Text("Cadastro Clientes", size=24)
        ],
        drawer=drawer
    )