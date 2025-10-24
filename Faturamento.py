import flet as ft
from menu import criar_menu
from bd.FunBD import RetFaturamento
from datetime import datetime
from geral import converte_valor
from Progress import Progresso


meses = {
    "JAN": 1, "FEV": 2, "MAR": 3, "ABR": 4,
    "MAI": 5, "JUN": 6, "JUL": 7, "AGO": 8,
    "SET": 9, "OUT": 10, "NOV": 11, "DEZ": 12
}

def faturamento_view(page: ft.Page):
    drawer = criar_menu(page)

    ano_atual = datetime.now().year
    ano_dropdown = ft.Dropdown(
        label="Ano",
        options=[ft.dropdown.Option(str(a)) for a in range(ano_atual - 2, ano_atual + 1)],
        value=str(ano_atual)
    )

    resultado_text = ft.Text("")
    
    # Container para exibir os resultados
    resultado_container = ft.Container(
        content=None,
        expand=True,
        padding=10
    )
    
    # Text para exibir o total
    total_text = ft.Text(
        "",
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE
    )

    def selection_changed(e):
        mes_nome = month_dropdown.value
        mes_numero = meses.get(mes_nome)
        ano_valor = ano_dropdown.value

        if mes_numero and ano_valor:
            pg = Progresso(page,"atualizado o faturamento da empresa neilar")                        
            #pg.mostrar()  # Aparece
            sucesso, msg = RetFaturamento(int(ano_valor), int(mes_numero))
            if sucesso:
                if isinstance(msg, list) and msg:
                    

                    # Calcula o total
                    total_faturamento = sum(item.get("Faturamento", 0) for item in msg)
                    
                    # Cria o ListView
                    resultado_listview = ft.ListView(
                        controls=[
                            ft.ListTile(
                                title=ft.Text(
                                    str(item.get("NomeRepresentante", "")),
                                    size=15,
                                    color=ft.Colors.BLUE
                                ),
                                subtitle=ft.Text(
                                    f"Faturamento: R$ {converte_valor(item.get('Faturamento', 0))}",
                                    size=15
                                )
                            )
                            for item in msg
                        ],
                        expand=True,
                        spacing=5,
                        padding=10
                    )
                    
                    # Atualiza o conteúdo do container
                    resultado_container.content = resultado_listview
                    resultado_text.value = ""
                    
                    # Atualiza o total
                    total_text.value = f"Total Geral: R$ "+converte_valor(total_faturamento)
                else:
                    resultado_container.content = None
                    resultado_text.value = "Nenhum resultado encontrado"
                    resultado_text.color = ft.Colors.ORANGE
                    total_text.value = ""  
            else:
                resultado_container.content = None
                resultado_text.value = f"Sem faturamento no período"
                resultado_text.color = ft.Colors.RED_50
                total_text.value = ""  
            
            resultado_text.update()
            resultado_container.update()
            total_text.update()
            pg.Fechar()

        page.snack_bar = ft.SnackBar(ft.Text(f"Mês selecionado: {mes_nome} → {mes_numero}"))
        page.snack_bar.open = True
        page.update()

    month_dropdown = ft.Dropdown(
        label="Mês",
        options=[ft.dropdown.Option(m) for m in meses.keys()],
        on_change=selection_changed,
    )

    def ano_changed(e):
        selection_changed(e)

    ano_dropdown.on_change = ano_changed

    return ft.View(
        "/faturamento",
        controls=[
            ft.IconButton(
                icon=ft.Icons.MENU,
                icon_size=30,
                tooltip="Abrir Menu",
                on_click=lambda e: page.open(drawer)
            ),
            ft.Row(
                [ft.Text("Faturamento", size=24)],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [ano_dropdown, month_dropdown],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            resultado_text,
            resultado_container,
            ft.Divider(height=20, color=ft.Colors.BLUE),  # Linha divisória
            ft.Row(
                [total_text],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        drawer=drawer
    )