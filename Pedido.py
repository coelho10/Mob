import flet as ft
from menu import criar_menu
from dialogo_modal import MsgInfo


def pedido_view(page: ft.Page):   
    
    # Cria o drawer usando a função importada
    drawer = criar_menu(page)
    
    # Criação dos campos
    nome_input = ft.TextField(
        label="Nome",
        width=400,
        autofocus=True,
        text_size=16
    )
    
    endereco_input = ft.TextField(
        label="Endereço",
        width=400,
        text_size=16
    )
    
    numero_input = ft.TextField(
        label="Número",
        width=400,
        text_size=16,
        keyboard_type=ft.KeyboardType.NUMBER,
        max_length=10  # Define o número máximo de caracteres
    )      
   
    
    # Função para trocar de campo ao pressionar Enter
    def nome_on_submit(e):
        endereco_input.focus()
    
    def endereco_on_submit(e):
        numero_input.focus()
    
    def numero_on_submit(e):
        salvar_pedido()
    
    def salvar_pedido():
        
        nome = nome_input.value
        endereco = endereco_input.value
        numero = numero_input.value
        
        if nome and endereco and numero:            
          
            MsgInfo(page, 
                   "Registro", 
                   "Registro Feito Sucesso", 
                   "sucesso")

            # Limpa os campos após salvar
            nome_input.value = ""
            endereco_input.value = ""
            numero_input.value = ""
            
            # Retorna o foco para o primeiro campo
            nome_input.focus()
        else:
            MsgInfo(
                page, 
                "Campos Obrigatórios", 
                "Preencha todos os campos antes de salvar!",
                "erro"
            )
        
        page.update()
    
    # Adiciona os eventos on_submit aos campos
    nome_input.on_submit = nome_on_submit
    endereco_input.on_submit = endereco_on_submit
    numero_input.on_submit = numero_on_submit
    
    # Botão para salvar
    salvar_btn = ft.ElevatedButton(
        text="Salvar Pedido",
        icon=ft.Icons.SAVE,
        on_click=lambda e: salvar_pedido(),
        width=400
    )
    
    return ft.View(       
        "/pedido",
        controls=[
            ft.IconButton(
                icon=ft.Icons.MENU,
                icon_size=30,
                tooltip="Abrir Menu",
                on_click=lambda e: page.open(drawer)
            ),
            ft.Row(
                [ft.Text("Pedidos", size=24)],
                alignment=ft.MainAxisAlignment.START
            ),
            ft.Container(height=10),
            ft.Column(
                controls=[
                    nome_input,
                    endereco_input,
                    numero_input,
                    ft.Container(height=10),
                    salvar_btn
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5
            )
        ],
        drawer=drawer
    )