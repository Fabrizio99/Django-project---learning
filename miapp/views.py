from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
layout="""
"""
def index(request):
    estudiantes = []
    return render(request,'index.html',{
        'titulo'      : 'Inicio',
        'mensaje'     : 'Proyecto Web con Django (Desde el View)',
        'estudiantes' : estudiantes
    })

def saludo(request):
    
    return render(request,'saludo.html',{
        'titulo'  : 'Saludo',
        'nombre_autor' : 'Fabrizio Raul Condori Guzman'
    })

def rango(request):
    a = 10
    b = 20
    rango = range(a,b+1)
    #inicio = a
    #rango = []
    #while inicio<=b:
        #rango.append(inicio)
        #inicio+=1


    return render(request,'rango.html',{
        'titulo'  : 'Rango',
        'a' : a,
        'b' : b,
        'rango_numeros' : rango
    })

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
