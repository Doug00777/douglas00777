import flet as ft 

def main(page: ft.page): 
    
    # lista de tarefas 
    
    tarefas = [] 
    
    # função para adicionar uma nova tarefa 
    def adicionar_tarefa(e): 
        if entrada_tarefa.value: 
            tarefas.append(entrada_tarefa.value) 
            atualizar_lista_tarefas() 
            entrada_tarefa.value = ''
            entrada_tarefa.focus() 
            page.update() 
            
            # função para remover uma tarefa 
    def remover_tarefa(e): 
        tarefas.remove(e.control.data) 
        atualizar_lista_tarefas() 
        
     # função para atualizar a lista de tarefas 
    def atualizar_lista_tarefas(e):
        lista_tarefas.controls.clear()
        for tarefa in tarefas:
            lista_tarefas.controls.append(ft.ListTile(
                title=ft.Text('Tarefa'),
                trailing=ft.IconButtom(icon=ft.icons.DELETE, on_click=remover_tarefa, data=tarefa
                                       ),
                )
            )
            page.update() 
            
            # campo de entrada de tarefa 
    entrada_tarefa = ft.TextField(label='Digite a tarefa', autofocus=True, on_submit=adicionar_tarefa, )
        
        # botão para adicionar a tarefa 
    botao_adicionar = ft.ElevatedButton(text='Adicionar tarefa', on_click=adicionar_tarefa) 
    
        # lista que exibirá as tarefas 
    lista_tarefas = ft.column() 
    
        # adicionar os componentes à página  
    page.add(
        entrada_tarefa,
        botao_adicionar,
        lista_tarefas 
    )   

    # inicializar a aplicação 
ft.app(target=main)  

                
         
              
     
    