import flet

def main(page: flet.Page):
    page.window_height = 300
    page.window_width = 400
    page.title = "Flet demo"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    
    text_num = flet.TextField(value="0", text_align=flet.TextAlign.RIGHT, width=200)
    
    def substract_click(e):
        text_num.value = str(int(text_num.value) - 1)
        page.update()
    
    def add_click(e):
        text_num.value = str(int(text_num.value) + 1)
        page.update()
        
    page.add(
        flet.Row(
            [
                flet.IconButton(flet.icons.REMOVE, on_click=substract_click),
                text_num,
                flet.IconButton(flet.icons.ADD, on_click=add_click)
            ],
            alignment=flet.MainAxisAlignment.CENTER
        )
    )
    
def tab(page: flet.Page):
    page.window_height = 300
    page.window_width = 400
    page.title = "Flet demo"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    
    tabs = flet.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            flet.Tab(
                text="Tab 1",
                content=flet.Container(
                    content=flet.Text("This is Tab 1"), alignment=flet.alignment.center
                ),
            ),
            flet.Tab(
                tab_content=flet.Icon(flet.icons.SEARCH),
                content=flet.Column(
                    [
                        flet.Text("This is Tab 2"),
                        flet.TextField(value="input", text_align=flet.TextAlign.RIGHT, width=200)
                    ],
                    )
            ),
            flet.Tab(
                text="Tab 3",
                icon=flet.icons.SETTINGS,
                content=flet.Text("This is Tab 3"),
            ),
        ],
        expand=1,
    )

    page.add(tabs)

if __name__ == "__main__":
    flet.app(target=tab)