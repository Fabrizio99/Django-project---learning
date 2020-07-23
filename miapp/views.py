from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
layout="""
    <h1>Proyecto Web (LP3) | Fabrizio Condori</h1>
    <hr>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/saludo">Mensaje de Saludo</a>
        </li>
        <li>
            <a href="/rango">Mostrar los números</a>
        </li>

    </ul>
    <hr>
"""
def index(request):
    #*mensaje="""
    #   <h1>Inicio</h1>
    #"""
    return HttpResponse(request,'index.html')

def saludo(request):
    
    return HttpResponse(request,'saludo.html')

def rango(request):
    a = 10
    b = 20
    resultado = f"""
        <h2>Numeros de [{a},{b}] </2>
        Resultado: <br>
        <ul>
    """
    while a<=b:
        resultado +=f"<li>{a}</li>"
        a+=1
    resultado+="</ul>"

    return HttpResponse(layout+resultado)

def rangos2(request,a=0,b=100):
    if a>b:
        return redirect('rango2',a=b,b=a)
    resultado = f"""
        <h2>Numeros de [{a},{b}] </2>
        Resultado: <br>
        <ul>
    """
    while a<=b:
        resultado +=f"<li>{a}</li>"
        a+=1
    resultado+="</ul>"

    return HttpResponse(layout+resultado)
