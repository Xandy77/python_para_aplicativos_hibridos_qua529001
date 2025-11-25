import flet as ft


def main(page: ft.Page):
    
    page.add( # conteudo da pagina
        ft.SafeArea( # é uma area aonde se coloca o cabeçalho
            ft.Container( # é uma especie de caixa aonde coloca-se os elementos, é equivalente a uma div
                ft.Text("Minha primeira aplicação.",size=30, weight="bold"),# Esse é o print do Flet
                
                alignment=ft.alignment.center,
            )
            
        ),
        ft.Container(
            ft.Image(
                src="God_of_War_2005_capa.png",
                fit=ft.ImageFit.CONTAIN,
                error_content=ft.Text("Não foi possível carregar a imagem.")            
            ),
            alignment=ft.alignment.center 
        )

    )


ft.app(main)
