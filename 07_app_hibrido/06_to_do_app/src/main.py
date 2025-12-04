import flet as ft

class Task(ft.Container):
    def __init__(self, text, delete_callback):
        super().__init__()

        self.completed = False
        self.delete_callback = delete_callback
        self.text_value = text

        # Checkbox
        self.checkbox = ft.Checkbox(value=False, on_change=self.update_status)

        # Texto da tarefa
        self.label = ft.Text(text, size=16, selectable=True)

        # Botão deletar
        self.delete_btn = ft.IconButton(icon=ft.Icons.DELETE_OUTLINE, icon_color="red", on_click=self.delete_clicked)

        # Botão editar
        self.edit_btn = ft.IconButton(icon=ft.Icons.EDIT, icon_color="#0288D1", on_click=self.edit_task)

        # Row da tarefa
        self.row = ft.Row(
            [self.checkbox, self.label, self.edit_btn, self.delete_btn],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )

        super().__init__(
            content=self.row,
            padding=ft.padding.symmetric(vertical=5, horizontal=10),
            margin=ft.margin.only(bottom=5),
            bgcolor="#F5F5F5",  # cor clara para tom sobre tom
            border_radius=10,
            shadow=ft.BoxShadow(color="#B0BEC5", blur_radius=5, offset=ft.Offset(2,2)),
        )

    def update_status(self, e):
        self.completed = self.checkbox.value
        self.label.style = ft.TextStyle.LINE_THROUGH if self.completed else ft.TextStyle.NORMAL
        self.update()

    def delete_clicked(self, e):
        self.delete_callback(self)

    def edit_task(self, e):
        # Substitui o texto por um TextField para editar
        self.input_edit = ft.TextField(
            value=self.label.value,
            expand=True,
            on_submit=self.save_edit,
            autofocus=True
        )
        self.row.controls[1] = self.input_edit
        self.update()

    def save_edit(self, e):
        # Salva a edição
        self.label.value = self.input_edit.value
        self.row.controls[1] = self.label
        self.update()


class TodoApp(ft.Column):
    def __init__(self):
        super().__init__()

        # Campo de nova tarefa
        self.new_task = ft.TextField(
            hint_text="Nova Tarefa...",
            expand=True,
            border_radius=10,
            on_submit=self.add_clicked,
        )

        self.items_left = ft.Text("0 itens ativos", size=14, color="#263238")
        self.tasks = ft.Column(spacing=5, scroll="auto")

        # Filtros
        self.filter = ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(text="Todas"),
                ft.Tab(text="Ativas"),
                ft.Tab(text="Concluídas"),
            ],
            on_change=self.update_filter,
        )

        # Layout geral com tom sobre tom
        self.controls = [
            ft.Container(
                content=ft.Text("Lista de Tarefas", size=28, weight=ft.FontWeight.BOLD, color="#263238"),
                alignment=ft.alignment.center,
                padding=ft.padding.only(bottom=15),
            ),
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD,
                        bgcolor="#0288D1",
                        on_click=self.add_clicked,
                        tooltip="Adicionar Tarefa",
                    ),
                ],
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Column(
                spacing=20,
                controls=[
                    self.filter,
                    self.tasks,
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            self.items_left,
                            ft.OutlinedButton(
                                text="Limpar Concluídas", on_click=self.clear_clicked
                            ),
                        ],
                    ),
                ],
            ),
        ]

    def add_clicked(self, e):
        if self.new_task.value.strip() == "":
            return

        task = Task(self.new_task.value, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.new_task.focus()  # mantém o foco
        self.before_update()
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.before_update()
        self.update()

    def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                self.task_delete(task)

    def update_filter(self, e):
        self.before_update()
        self.update()

    def before_update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0

        for task in self.tasks.controls:
            if status == "Todas":
                task.visible = True
            elif status == "Ativas":
                task.visible = not task.completed
            elif status == "Concluídas":
                task.visible = task.completed

            if not task.checkbox.value:
                count += 1

        self.items_left.value = f"{count} item(s) ativo(s)"


def main(page: ft.Page):
    page.title = "Todo App"
    page.window_width = 600
    page.padding = 20
    page.bgcolor = "#ECEFF1"  # fundo tom sobre tom
    page.scroll = "auto"

    app = TodoApp()
    page.add(app)


ft.app(main)