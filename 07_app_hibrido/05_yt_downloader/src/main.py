import flet as ft
from pytubefix import YouTube

import os
import threading

def main(page: ft.Page):
    page.title = "YouTube Downloader"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.icon = "assets/youtube.png"

    # cria as pastas caso não existam
    caminho_videos = 'videos'
    caminho_audios = 'audios'
    os.makedirs(caminho_videos, exist_ok=True)
    os.makedirs(caminho_audios, exist_ok=True)

    # componentes da interface gráfica
    titulo = ft.Text("Use uma URL", color=ft.Colors.Black, size=20, weight=ft.Fontweight.BOLD)
    URL = ft.TextField(
        label="Cole a URL do video do YouTube aqui",
        width=400,
        border_radius=10
    )

    base_path = os.path.dirname(__file__)
    logo_path = os.path.join(base_path, "assets", "youtube.png")
    logo_cabecalho = ft.Image(src=logo_path, width=300, height=300)

    # componentes para mostrar informações do video
    video_info = ft.Container(
        content=ft.Column([]),
        visible=False,
        padding=10,
        bgcolor=ft.Colors.BLUE_GREY_50,
        border_radius=10,
        width=400
    )

    # barra de progresso
    progress_bar = ft.ProgressBar(
        visible=False,
        width=400,
        color=ft.Colors.BLUE,
        bgcolor=ft.Colors.BLUE_GREY_100
    )

    # mmostra as informações de video na interface
    def mostrar_info_videos(yt):
        try:
            # limpa o container
            video_info.content.controls.clear()

            # adiciona informações do video
            video_info.content.controls.extend(
                [
                    ft.Text(f"Título: {yt.title}", size=14, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Canal: {yt.author}", size=12),
                    ft.Text(f"Duração: {yt.length/60}:{yt.length%60:02d}", size=12),
                    ft.Text(f"Visualizações: {yt.views:,}", size=12),

                ]
            )

            video_info_visible = True
            page.update()

        except Exception as e:
            status_text.value = f"Erro ao obter informações: {str(e)}."
            status_text.color = ft.Colors.RED
            page.update()

    # função para baixar video
    def baixar_video(e):
        if not url.value.strip():
            status_text.value = "Por favor, insira uma URL válida."
            status_text.color = ft.Colors.ORANGE
            page.update()

        def downloade_thread():
            try:
                # mostra progresso
                progress_bar.visible = True
                progress_bar.value = "Analisando video..."
                status_text.color = ft.Colors.BLUE
                page.update()

                # cria objeto do youtube
                yt = YouTube(url.value.strip())

                # mostra as funções do video
                mostrar_info_videos(yt)

                # inicia download
                status_text.value = f"Baixando video: {yt.title}..."
                page.update()

                # pega a maior reolução possível
                stream = yt.streams.get_highest_resolution()

                # TODO: fazer if else do stream
            except Exception as e:
                progress_bar.visible = False
                status_text.value = f"Erro {str(e)}."
                status_text.color = ft.Colors.RED
                page.update()

        # executa em thread separada para não travar a interface
        threading.Thread(target=downloade_thread, daemon=True).start()
    
    page.add(
        ft.SafeArea(
            ft.Container(
                
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )

ft.app(main)