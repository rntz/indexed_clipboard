from talon import Module, Context, actions, clip, imgui

mod = Module()
ctx = Context()
indexed_clipboard = {}

mod.list('clipboard_index', desc="Names of indices into the indexed clipboard.")

def update_index_names():
    ctx.lists['self.clipboard_index'] = list(indexed_clipboard.keys())

@imgui.open()
def gui(gui: imgui.GUI):
    gui.text("Indexed clipboard")
    gui.line()
    for index, value in indexed_clipboard.items():
        gui.text(f'{index}: {value}'
                 if len(value) <= 20 else
                 f'{index}: {value[:20]}...')

@mod.action_class
class ModuleActions:
    def indexed_clipboard_copy(index: str):
        """Copies the selection into the indexed clipboard."""
        indexed_clipboard[index] = actions.edit.selected_text()
        update_index_names()

    def indexed_clipboard_paste(index: str):
        """Pastes from the given index of the indexed clipboard."""
        actions.user.paste(indexed_clipboard[index])

    def indexed_clipboard_clear(index: str):
        """Clears the given index from the indexed clipboard."""
        del indexed_clipboard[index]
        update_index_names()

    def indexed_clipboard_toggle():
        """Views the indexed clipboard."""
        if gui.showing: gui.hide()
        else: gui.show()
