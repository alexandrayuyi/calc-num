from flet import *
from metodos import *


def main(page: Page):
    page.title = "E2 Cálculo Numérico"
    page.window_resizable = False  # window is not resizable
    page.window_maximized = True

    def cramer_click(e):
        texto.value= "La regla de Cramer es un método para resolver sistemas de ecuaciones lineales. Se basa en el cálculo de determinantes, y es aplicable a sistemas con tantas ecuaciones como incógnitas, siempre y cuando el determinante de la matriz de coeficientes sea distinto de cero."
        limpiar.disabled = False
        title1.color= '#3679a8'
        title2.color='#3679a8'
        title1.value="Matriz de coeficientes de las incognitas:"
        title2.value="Vector de Valores Independientes:"
        titulo1.value="Vector de las soluciones del Sistema:"
        titulo2.value=""
        titulo1.color='#3679a8'
        Solucion = SistemaEcuaciones()
        op1.value= Solucion.MostrarMatriz() + "\n"
        op2.value= Solucion.MostrarVectorIndependiente()
        res1.value=Solucion.MostrarSoluciones()
        res2.value=""
        page.update()

    def pot_click(e):
        limpiar.disabled = False
        texto.value="El método de las potencias es un método para resolver ecuaciones no lineales. Consiste en aproximar la solución de la ecuación por una serie de potencias de la variable independiente. Esta serie se construye de manera iterativa. En cada iteración la solución se aproxima aún más a la solución real."
        title1.color= '#3679a8'
        title2.color='#3679a8'
        title1.value="Matriz Inicial:"
        title2.value="Vector Inicial:"
        titulo1.value="Lista de Autovalores de la Matriz:"
        titulo2.value="Lista de Autovectores de la Matriz:"
        titulo1.color='#3679a8'
        titulo2.color='#3679a8'
        op1.value, op2.value, res1.value, res2.value= MostrarPotencias()
        page.update()

    def lagrange_click(e):
        limpiar.disabled = False
        texto.value= "La interpolación de Lagrange es un método que permite aproximar en un intervalo a una función desconocida a partir de un conjunto de puntos conocidos. Consiste en construir un polinomio de grado n, donde n es el número de puntos conocidos y el polinomio pasa por todos los puntos conocidos."
        title1.color= '#3679a8'
        title2.color='#3679a8'
        title1.value="Valores:"
        title2.value="Valor a interpolar:"
        titulo1.value="Resultado de la interpolacion:"
        titulo2.value=""
        titulo1.color='#3679a8'
        res2.value=""
        op1.value, op2.value, res1.value = MostrarInterpolacion()
        page.update()

    def limpiar_click(e):
        limpiar.disabled = True
        texto.value= "Haz click en un botón para ejecutar las funciones del método elegido y ver el resultado."
        title1.color='#b6adc9'
        title1.value="Operación..."
        title2.value=""
        op1.value=""
        op2.value=""
    
        titulo1.value= "Resultados..."
        titulo1.color='#b6adc9'
        titulo2.value=""
        res1.value=""
        res2.value=""
        page.update()

    cramer = FilledTonalButton("Regla de Cramer", on_click=cramer_click)
    pot = FilledTonalButton("Método de Potencia", on_click=pot_click)
    lagrange = FilledTonalButton("Interpolación de Lagrange", on_click=lagrange_click)
    limpiar = OutlinedButton("Limpiar", on_click=limpiar_click, disabled=True)

    texto = Text("Para comenzar haz click en un botón para ejecutar las funciones del método elegido.")
    
    title1 = Text("Operación...", color='#b6adc9', style= TextThemeStyle.HEADLINE_SMALL)
    title2 = Text(style= TextThemeStyle.HEADLINE_SMALL)
    op1= Text(style=TextThemeStyle.HEADLINE_SMALL)
    op2= Text(style=TextThemeStyle.HEADLINE_SMALL)
    
    titulo1= Text("Resultados...", color='#b6adc9', style= TextThemeStyle.HEADLINE_SMALL)
    titulo2= Text(style= TextThemeStyle.HEADLINE_SMALL)
    res1= Text(style=TextThemeStyle.HEADLINE_SMALL)
    res2 = Text(style=TextThemeStyle.HEADLINE_SMALL)

    botones = Container(padding=padding.only(top=10, bottom=10), width=100, height=50, content=Row(
        alignment=MainAxisAlignment.CENTER, spacing=60, controls=[cramer, pot, lagrange, limpiar],), margin=margin.only(bottom=10), bgcolor='#e6f0ff')

    definicion = Container(height=50,content=texto, margin=margin.only(bottom=15, left=30, right=30))
    definicion.alignment = alignment.center

    entrada = Container(width=420, height=40, margin= margin.only(right=20, left=20, bottom=30), border_radius=10, padding=padding.all(20), content=ListView(
        controls=[title1, op1, title2, op2]
    ))
    entrada.border = border.all(3, '#322b45')
    salida = Container(width=740, height=40, border_radius=10, margin= margin.only(left=20, bottom=30), padding=padding.all(20), content=ListView(controls=[titulo1,res1,titulo2,res2]))
    salida.border = border.all(3, '#322b45')

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


app(target=main)
