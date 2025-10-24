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
    # Wrapper com try-except para capturar erros na criação da view
    try:
        drawer = criar_menu(page)
    except Exception as e:
        print(f"Erro ao criar menu: {e}")
        drawer = None

    ano_atual = datetime.now().year
    mes_atual = datetime.now().month
    
    # Encontra o nome do mês atual
    mes_atual_nome = None
    for nome, num in meses.items():
        if num == mes_atual:
            mes_atual_nome = nome
            break
    
    ano_dropdown = ft.Dropdown(
        label="Ano",
        options=[ft.dropdown.Option(str(a)) for a in range(ano_atual - 2, ano_atual + 1)],
        value=str(ano_atual),
        width=150
    )

    month_dropdown = ft.Dropdown(
        label="Mês",
        options=[ft.dropdown.Option(m) for m in meses.keys()],
        value=mes_atual_nome,  # Define o mês atual como valor inicial
        width=150
    )

    resultado_text = ft.Text("", size=16)
    
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
        pg = None
        try:
            mes_nome = month_dropdown.value
            mes_numero = meses.get(mes_nome)
            ano_valor = ano_dropdown.value

            if not mes_nome or not mes_numero or not ano_valor:
                resultado_text.value = "Selecione um mês e ano"
                resultado_text.color = ft.Colors.ORANGE
                resultado_text.update()
                return

            pg = Progresso(page, "Atualizando o Faturamento")
            pg.Mostrar()
            
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
                    total_text.value = f"Total Geral: R$ {converte_valor(total_faturamento)}"
                else:
                    resultado_container.content = None
                    resultado_text.value = "Nenhum resultado encontrado"
                    resultado_text.color = ft.Colors.ORANGE
                    total_text.value = ""  
            else:
                resultado_container.content = None
                resultado_text.value = "Sem faturamento no período"
                resultado_text.color = ft.Colors.RED_50
                total_text.value = ""  
            
            if pg:
                pg.Fechar()
            
            resultado_text.update()
            resultado_container.update()
            total_text.update()

            page.snack_bar = ft.SnackBar(
                ft.Text(f"Mês selecionado: {mes_nome} → {mes_numero}"),
                duration=2000
            )
            page.snack_bar.open = True
            page.update()
            
        except Exception as ex:
            print(f"Erro em selection_changed: {ex}")
            import traceback
            traceback.print_exc()
            
            if pg:
                try:
                    pg.Fechar()
                except:
                    pass
                    
            resultado_container.content = None
            resultado_text.value = f"Erro ao carregar dados: {str(ex)}"
            resultado_text.color = ft.Colors.RED
            total_text.value = ""
            
            try:
                resultado_text.update()
                resultado_container.update()
                total_text.update()
                page.update()
            except:
                pass

    def ano_changed(e):
        selection_changed(e)

    month_dropdown.on_change = selection_changed
    ano_dropdown.on_change = ano_changed

    # Cria a view
    view = ft.View(
        "/faturamento",
        controls=[
            ft.IconButton(
                icon=ft.Icons.MENU,
                icon_size=30,
                tooltip="Abrir Menu",
                on_click=lambda e: page.open(drawer) if drawer else None
            ),
            ft.Row(
                [ft.Text("Faturamento", size=24, weight=ft.FontWeight.BOLD)],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [ano_dropdown, month_dropdown],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            ),
            resultado_text,
            resultado_container,
            ft.Divider(height=20, color=ft.Colors.BLUE),
            ft.Row(
                [total_text],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        drawer=drawer,
        scroll=ft.ScrollMode.AUTO
    )
    
    return view