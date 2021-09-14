from talon import Module, Context, actions, clip

mod = Module()
mod.list('clipboard_index', desc="Names of indices into the indexed clipboard.")

ctx = Context()

indexed_clipboard = {}
def update_index_names():
    ctx.lists['self.clipboard_index'] = list(indexed_clipboard.keys())

@mod.action_class
class ModuleActions:
    def indexed_clipboard_copy(index: str):
        """Copies the selection into the indexed clipboard."""
        indexed_clipboard[index] = actions.edit.selected_text()
        update_index_names()

    def indexed_clipboard_paste(index: str):
        """Pastes from the given index of the indexed clipboard."""
        actions.user.paste(indexed_clipboard[index])
