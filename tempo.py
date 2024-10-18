import flet as ft
import time 

def principal( page = ft . Page ): 
    linha = ft.Row ( controls =[ft.Text("Estas são"), ft.Text("cidades"), ft.Text("brasileiras")]) 
    page.add(linha) 
    t = ft.Text() 
    page.add(t) # é um atalho para page.controls.append(t) e depois page.update() 
    cidades=["Belo Horizonte", "Curitiba", "São Paulo", "Salvador", "**fim**" ] 
    for i in range(5): 
        t.value = cidades [i] 
        page.update () 
        time.sleep (1)  
        page.add( 
        ft.Row ( controls =[ 
            ft.TextField (label = "Sua cidade" ), 
            ft.ElevatedButton (text = "Clique aqui para inserir o nome de sua cidade!" )]))
     

ft . app (target=principal)
