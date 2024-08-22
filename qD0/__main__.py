"""
Testing layouts for the main qD0 app.
"""

from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal, HorizontalScroll, VerticalScroll, Vertical
from textual.events import Mount
from textual.screen import ModalScreen, Screen
from textual.widgets import Button, Footer, Header, Label, Placeholder, Static, TextArea, ListView, ListItem, Input


class Column(VerticalScroll):
    def compose(self) -> ComposeResult:
        yield Task(id=f"Task")

class Task(Placeholder):
    pass


class NewProjectModal(ModalScreen):
    """Creates Model Screen to get new project name"""
    def compose(self) -> ComposeResult:
        with Container():
            yield Label("New Project Name")
            with Horizontal():
                yield Input(placeholder="Project Name")
                yield Button.success("Yes", id="yes")
                yield Button.error("No", id="no")

    @on(Button.Pressed)
    def submit(self, event):
        if event.button.id == "yes":
            self.action_dismiss()

class YesOrNo(ModalScreen):
    """Creates Model Screen with Yes or No."""
    def __init__(self, question):
        self.question = question
        super().__init__()

    def compose(self) -> ComposeResult:
        with Container():
            yield Label(self.question)
            with Horizontal():
                yield Button.success("Yes", id="yes")
                yield Button.error("No", id="no")

    @on(Button.Pressed)
    def leave_modal_screen(self, event):
        self.dismiss(event.button.id == "yes")

class qD0(App):
    BINDINGS = [
        Binding(key="ctrl+q", action="maybe_quit", description="Quit the app")
     ]
    
    CSS_PATH = "layout.tcss"
    
    def compose(self) -> ComposeResult:
        yield Header(id="Header")
        with Horizontal():
            yield ListView(name="Project", id="c1")

            with Static(id="c3"):
                with Vertical(id="r1"):
                    yield Static(id="s1")
                    yield Static(id="s2")
                    yield Static(id="s3")
                yield Static(id="r2")
                yield TextArea(id="r3")
                yield TextArea(id="r4")
        yield Footer()

    def on_mount(self, event: Mount) -> None:
        epl = self.query_one("#c1")
        projects = ["Work", "Home"]
        for i in projects:
            epl.append(ListItem(Label(i)))
            
    def action_maybe_quit(self):
        self.push_screen(YesOrNo("Exit qD0?"), self.maybe_exit_app)
    
    def maybe_exit_app(self, bool):
        if bool:
            self.exit()

if __name__ == "__main__":
    app = qD0()
    app.run()
