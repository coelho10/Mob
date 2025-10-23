import flet as ft

def MsgInfo(page: ft.Page, titulo, mensagem, tipo="info"):
        
    def fechar_dlg(e):
        dlg.open = False
        page.update()
    
    # Define cores e ícones baseado no tipo
    cores = {
        "info": ft.Colors.BLUE,
        "sucesso": ft.Colors.GREEN,
        "erro": ft.Colors.RED,
        "aviso": ft.Colors.ORANGE
    }
    
    icones = {
        "info": ft.Icons.INFO,
        "sucesso": ft.Icons.CHECK_CIRCLE,
        "erro": ft.Icons.ERROR,
        "aviso": ft.Icons.WARNING
    }
    
    cor = cores.get(tipo, ft.Colors.BLUE)
    icone = icones.get(tipo, ft.Icons.INFO)
    
    dlg = ft.AlertDialog(
        modal=True,
        title=ft.Row([
            ft.Icon(icone, color=cor, size=30),  
            ft.Text(titulo, size=25)
        ]),
        content=ft.Text(mensagem, size=20),
        actions=[
            ft.TextButton("OK", on_click=fechar_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    
    # Adiciona o diálogo à sobreposição da página para exibir por cima dos outros controles
    page.overlay.append(dlg)
    # Define a propriedade 'open' do diálogo como True, fazendo com que seja exibido na tela
    dlg.open = True
    page.update()