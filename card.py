import flet as ft 

def main(page: ft.page):
  page.title = 'Card Exemple'
  page.add(
      ft.card(
          content=ft.Container(
              content=ft.column(
                  [
                      ft.ListTile(
                          leading=ft.Icon(ft.icons.ALBUM),
                          title=ft.Text('The Enchanted Nightingale'),
                          subtitle=ft.Text(
                              'Music by Julie Gable. Lyrics by Sidney Stein.'
                          ),
                      ),
                      ft.Row(
                          [ft.TextButton('Buy tickets'), ft.TextButto('Listen')], alignment=ft.MainAxisAlignment.END,
                      ),
                  ]
          ),
              width=400,
              padding=10,
      )
  )

)
    

ft.add(target=main, view=ft.WEB_BROWSER)  