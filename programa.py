import flet as ft 

def principal(page: ft.page):
    page.title = 'Novo App'
    page.vertical_alignment = ft.MainAxisAlignmet.CENTER 
    def diminuir(e): 
        caixa_texto = str(int(caixa_texto.value) - 1)
        page.update() 
    def somar(e):
        caixa_texto = str(int(caixa_texto.value) + 1)
        page.update()
        
        # criar os itens que queremos a página.
        botao_menos = ft.IconButton(ft.icons.REMOVE, on_click=diminuir) 
        caixa_texto = ft.TextField(value='0', width=100, text_align=ft.TextAlign.CENTER) 
        botao_mais = ft.IconButton(ft.icons.ADD, on_click=somar) 
        
        # adicionar  os itens na página 
        page.add(
            ft.Row([botao_menos, caixa_texto, botao_mais],
alignment=ft.MainAxisAlignmment.CENTER)
        )
        
ft.app(target=principal, view=ft.WEB_BROWSER)    

