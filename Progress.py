import flet as ft

class Progresso():
    def __init__(self, page: ft.Page, texto="Aguarde..."):
        self.page = page
        self.texto = texto
        self.label = ft.Text(
            self.texto, 
            size=18,
            no_wrap=False,
            width=300
        )
        self.dialog = ft.AlertDialog(
            modal=True,
            open=False,
            content=ft.Column([
                ft.Row([
                    ft.ProgressRing(),
                    self.label
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=20)
            ],
            tight=True),
        )
        self.page.overlay.append(self.dialog)

    def Mostrar(self):
        self.label.value = self.texto
        self.dialog.open = True
        self.page.update()

    def Fechar(self):
        self.dialog.open = False
        self.page.update()