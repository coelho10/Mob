import flet as ft

def principal_menu_view(page: ft.Page):
    
    #View do menu principal que é carregada após o login
    
    
    def handle_dismissal(e):
        print(f"Drawer dismissed!")

    def handle_change(e):
        print(f"Selected Index changed: {e.control.selected_index}")
        page.close(drawer)
        
        # Aqui você pode adicionar navegação para diferentes seções
        if e.control.selected_index == 0:
            print("Navegar para Item 1")
        elif e.control.selected_index == 1:
            print("Navegar para Item 2")
        elif e.control.selected_index == 2:
            print("Navegar para Item 3")

    drawer = ft.NavigationDrawer(
        on_dismiss=handle_dismissal,
        on_change=handle_change,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Item 1",
                icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.MAIL_OUTLINED),
                label="Item 2",
                selected_icon=ft.Icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.PHONE_OUTLINED),
                label="Item 3",
                selected_icon=ft.Icons.PHONE,
            ),
        ],
    )
    
    def logout_click(e):
        page.go("/login")
    
    return ft.View(
        "/principal_menu",
        controls=[
            ft.AppBar(
                title=ft.Text("Menu Principal"),
                center_title=True,
                bgcolor=ft.Colors.SURFACE_VARIANT,
                actions=[
                    ft.IconButton(
                        ft.Icons.LOGOUT,
                        tooltip="Sair",
                        on_click=logout_click
                    )
                ]
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("Bem-vindo ao Sistema!", size=24, weight=ft.FontWeight.BOLD),
                    ft.ElevatedButton(
                        "Abrir Menu",
                        icon=ft.Icons.MENU,
                        on_click=lambda e: page.open(drawer)
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20),
                alignment=ft.alignment.center,
                expand=True
            )
        ]
    )