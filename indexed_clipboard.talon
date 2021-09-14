clip copy <user.word>: user.indexed_clipboard_copy(word)
clip paste {user.clipboard_index}: user.indexed_clipboard_paste(clipboard_index)
clip clear {user.clipboard_index}: user.indexed_clipboard_clear(clipboard_index)
clip list: user.indexed_clipboard_toggle()
