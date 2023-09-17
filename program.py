from flet import *
from metododecramer import *


def main(page: Page):
    page.title = "E2 Cálculo Numérico"
    page.window_resizable = False  # window is not resizable
    page.window_maximized = True

    def cramer_click(e):
        texto.value= "La regla de Cramer es un método para resolver sistemas de ecuaciones lineales. Se basa en el cálculo de determinantes, y es aplicable a sistemas con tantas ecuaciones como incógnitas, siempre y cuando el determinante de la matriz de coeficientes sea distinto de cero."
        limpiar.disabled = False
        page.update()

    def pot_click(e):
        limpiar.disabled = False
        texto.value="El método de las potencias es un método para resolver ecuaciones no lineales. Consiste en aproximar la solución de la ecuación por una serie de potencias de la variable independiente. Esta serie se construye de manera iterativa. En cada iteración la solución se aproxima aún más a la solución real."
        page.update()

    def lagrange_click(e):
        limpiar.disabled = False
        texto.value= "La interpolación de Lagrange es un método que permite aproximar en un intervalo a una función desconocida a partir de un conjunto de puntos conocidos. Consiste en construir un polinomio de grado n, donde n es el número de puntos conocidos y el polinomio pasa por todos los puntos conocidos."
        page.update()

    def limpiar_click(e):
        limpiar.disabled = True
        texto.value= ""
        page.update()

    cramer = FilledTonalButton("Regla de Cramer", on_click=cramer_click)
    pot = FilledTonalButton("Método de Potencia", on_click=pot_click)
    lagrange = FilledTonalButton("Interpolación de Lagrange", on_click=lagrange_click)
    limpiar = OutlinedButton("Limpiar", on_click=limpiar_click, disabled=True)

    texto = Text()

    botones = Container(padding=padding.only(top=10, bottom=10), width=100, height=50, content=Row(
        alignment=MainAxisAlignment.CENTER, spacing=60, controls=[cramer, pot, lagrange, limpiar],), margin=margin.only(bottom=10), bgcolor='#e6f0ff')

    definicion = Container(height=50,content=texto, margin=margin.only(bottom=5, left=10, right=10))
    definicion.alignment = alignment.center

    entrada = Container(width=800, height=100, margin= margin.only(right=20), border_radius=10)
    entrada.border = border.all(5, '#343536')
    salida = Container(width=430, height=100, border_radius=10)
    salida.border = border.all(5, '#343536')

    proceso = ListView(horizontal=True, height=500, width=500, controls=[entrada, salida])

    container = Container(border_radius=10, width=2000, height=620, shadow=BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=colors.BLUE_GREY_300,
        offset=Offset(0, 0),
        blur_style=ShadowBlurStyle.OUTER,),
        content=ListView(
        controls=[
            botones,
            definicion,
            proceso
        ]
    ))
    container.margin = margin.all(5)
    page.add(container)
    page.update()

    # row = ft.Row(alignment= ft.MainAxisAlignment.CENTER ,spacing=60, controls=[cramer,pot,lagrange,limpiar])
    # page.add(row)
    # page.update()

    # desc = ft.Text("Headline Small", style=ft.TextThemeStyle.HEADLINE_MEDIUM)
    # c= ft.Container(content= desc, padding=60, border_radius=10,
    # width=2000,
    # height=100,
    # shadow=ft.BoxShadow(
    #     spread_radius=1,
    #     blur_radius=15,
    #     color=ft.colors.BLUE_GREY_300,
    #     offset=ft.Offset(0, 0),
    #     blur_style=ft.ShadowBlurStyle.OUTER,))
    # c.margin= ft.margin.all(20)
    # page.add(c)

    # txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)


app(target=main)
