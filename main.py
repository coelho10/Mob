import flet as ft
import os
from Principal import principal_view
from Faturamento import faturamento_view  
from CadCliente import cadcliente_view  
from Pedido import pedido_view  
from ValidaUsuario import validar_usuario  # Mudança aqui
from Progress import *

#https://flet-controls-gallery.fly.dev/navigation/navigationdrawer

def salvar_email(email):
    #Salva o email no arquivo lg.txt
    try:
        with open("lg.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(email)
    except Exception as e:
        print(f"Erro ao salvar email: {e}")

def carregar_email():
    #Carrega o email do arquivo lg.txt
    try:
        if os.path.exists("lg.txt"):
            with open("lg.txt", "r", encoding="utf-8") as arquivo:
                return arquivo.read().strip()
    except Exception as e:
        print(f"Erro ao carregar email: {e}")
    return ""  # Retorna vazio se não existir ou houver erro

def login_view(page: ft.Page):
    # Carrega o email salvo
    email_salvo = carregar_email()
    
    email_input = ft.TextField(
        label="Email", 
        width=300, 
        value=email_salvo 
        #if email_salvo else "jalmir@neilar.com.br"
    )
    senha_input = ft.TextField(
        label="Senha", 
        password=True, 
        can_reveal_password=True, 
        width=300, 
        #value="1010"
    )
    status_text = ft.Text("")

    # Função para salvar email ao sair do campo
    def email_on_blur(e):
        salvar_email(email_input.value)
    
    # Adiciona o evento on_blur ao campo de email
    email_input.on_blur = email_on_blur
    
    def acessar_click(e):
        email = email_input.value
        senha = senha_input.value

        status_text.value = ""
        status_text.color = None

        # Salva o email também ao fazer login
        salvar_email(email)
        pg = Progresso(page, "Aguarde Login...")
        pg.Mostrar()              
        sucesso, msg = validar_usuario(email, senha)
        pg.Fechar()
        if sucesso:            
            page.go("/faturamento")
        else:        
            status_text.value = f"Email ou senha incorretos. {msg}"
            status_text.color = ft.Colors.RED        
        status_text.update()

    acessar_btn = ft.ElevatedButton(
        text="Acessar",
        icon=ft.Icons.LOGIN,
        on_click=acessar_click
    )

    return ft.View(
        "/login",
        controls=[
            ft.Container(
                content=ft.Column([
                    ft.Image(
                        src="logoNeilar.webp",
                        width=200,
                        fit=ft.ImageFit.CONTAIN
                    ),
                    ft.Text("Login", size=30),
                    email_input,
                    senha_input,
                    acessar_btn,
                    status_text
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,            
                spacing=20),
                alignment=ft.alignment.center
            )    
        ]
    )

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    
    def route_change(route):
        try:
            print(f"Navegando para: {page.route}")  # Debug
            page.views.clear()
        
            if page.route == "/login":
                print("Carregando login_view...")  # Debug
                page.views.append(login_view(page))
            
            elif page.route == "/principal":
                print("Carregando principal_view...")  # Debug
                page.views.append(principal_view(page))
            
            elif page.route == "/faturamento":
                print("Carregando faturamento_view...")  # Debug
                page.views.append(faturamento_view(page))
                print("faturamento_view carregado com sucesso!")  # Debug
            
            elif page.route == "/pedido":
                print("Carregando pedido_view...")  # Debug
                page.views.append(pedido_view(page))
            
            elif page.route == "/cadcliente":
                print("Carregando cadcliente_view...")  # Debug
                page.views.append(cadcliente_view(page))
            
            page.update()
            print("Page atualizado com sucesso!")  # Debug
        
        except Exception as e:
            print(f"ERRO no route_change: {e}")  # Debug
            import traceback
            traceback.print_exc()  # Mostra o erro completo

    page.on_route_change = route_change
    page.go("/login")


ft.app(target=main, view=ft.WEB_BROWSER, host="0.0.0.0", port=8800, assets_dir="assets")
