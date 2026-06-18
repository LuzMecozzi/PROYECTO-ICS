import flet as ft
import os

def saludo():
    return "Bom dia"


def main(page: ft.Page):
    # 1. Configuración general de la ventana
    page.title = "PROYECTO CI/CD-ICS"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER    
    page.bgcolor = "#0F172A"
    page.padding = 20


    # 2. Creación de los elementos de texto
    titulo = ft.Text(
        value=saludo(),
        size=50,
        weight=ft.FontWeight.W_900,
        color="#38BDF8",            
        text_align=ft.TextAlign.CENTER,
    )


    subtitulo = ft.Text(
        value="Proyecto CI/CD - Luz Mecozzi.",
        size=18,
        color=ft.Colors.WHITE70,    
        text_align=ft.TextAlign.CENTER,
    )


    # 3. Creación de un botón interactivo
    boton_falso = ft.ElevatedButton(
        content="Comenzar Exploración",
        icon="rocket_launch",        
        color=ft.Colors.WHITE,      
        bgcolor="#6366F1",          
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15),
            padding=20,              
        )
    )


    # 4. Agrupar todo dentro de una "Tarjeta"
    tarjeta_principal = ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                subtitulo,
                ft.Divider(color="transparent", height=20),
                boton_falso
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor="#1E293B",
        padding=50,                  
        border_radius=20,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=20,
            color=ft.Colors.BLACK54,
            offset=ft.Offset(0, 10),
        )
    )


    # 5. Agregar la tarjeta a la pantalla
    page.add(tarjeta_principal)


if __name__ == "__main__":
    ft.run(main)
