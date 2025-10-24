from math import exp
import flet as ft

class Progress():
    def __init__(self, page: ft.Page, texto="Aguarde..."):
        self.page = page
        self.texto = texto  # Texto que aparecerá dentro do AlertDialog
        self.label = ft.Text(
            self.texto, 
            size=18,
            no_wrap=False,  # Permite quebra de linha
            width=300,  # Define uma largura máxima para forçar quebra
            expand=True
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
        #Mostrar mensagem
        self.label.value = self.texto
        self.dialog.open = True
        self.page.update()    

    def fechar(self):
        self.dialog.open = False
        self.page.update()


progress = Progress  # Para facilitar import progress = Progress(page)