import flet as ft


def main(page: ft.Page):
    # função do evento
    def exibir_nome(e): # O (e) é para quando o usuário clicar o botão seja ativado
        nome_saida.value = nome.value
        nome_saida.update() # update: Atualiza a pagina
    # PROPRIEDADES DA PÁGINA
    page.title = "App de manipulação de eventos"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # declaração de variáveis
    nome = ft.TextField(label="Informe seu nome: ", on_submit=exibir_nome) # TextField é o input
    nome_saida = ft.Text() # Text é o print()
    
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Trabalhando com Eventos", size=35, weight="bold"),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        
        nome, 
        ft.ElevatedButton("Enviar", on_click=exibir_nome),
        nome_saida
        )
    

ft.app(main)
