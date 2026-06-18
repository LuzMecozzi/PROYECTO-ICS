import flet as ft

def saludo():
    return "Hola Mundo"

def main(page: ft.Page):
    page.title = "Mi App Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    texto = ft.Text(value=saludo(), size=30, color=ft.Colors.BLUE)
    page.add(texto)

if __name__ == "__main__":
    ft.app(target=main)