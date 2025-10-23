import flet as ft

def criar_menu(page: ft.Page):    
    
    def handle_dismissal(e):
        print(f"Drawer dismissed!")

    def handle_change(e):
        selected = e.control.selected_index
        print(f"Selected Index changed: {selected}")
        page.close(drawer)

        # Navega baseado no índice selecionado
        if selected == 0:  # Pedido
            page.go("/pedido")
        elif selected == 1:  # Cadastro Cliente
            page.go("/cadcliente")
        elif selected == 2:  # Faturamento
            page.go("/faturamento")
        elif selected == 3:  # Sair
            page.go("/login")

    drawer = ft.NavigationDrawer(
        on_dismiss=handle_dismissal,
        on_change=handle_change,
        controls=[
            ft.Container(height=8),
            ft.NavigationDrawerDestination(
                label="Pedidos",
                icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.MAIL_OUTLINED),
                label="Cadastro Clientes",
                selected_icon=ft.Icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.RECEIPT_LONG_OUTLINED),
                label="Faturamento",
                selected_icon=ft.Icons.RECEIPT_LONG_OUTLINED,                                
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.LOGOUT_OUTLINED),
                label="Sair",
                selected_icon=ft.Icons.LOGOUT,
            ),
        ],
    )
    
    return drawer