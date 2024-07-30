from curses.textpad import Textbox

class qbox(Textbox):
    """
    A custom textbox class that inherits from `curses.textpad.Textbox` which overides the `do_command` method.
    This was created because the author of qD0 uses Zellig and `Ctrl-G` is utilized there.
    The `Enter` key is a way better choice anyway. 
    
    Methods
    -------
    do_command():
        Method handles the Enter or ESC key, set exit_without_saving to True if applicable, and return 0 to exit the edit mode.
    """

    def __init__(self, win):
        """
        Parameters
        ----------
        win: object
            A `curses.window` object.
        Example: 
            `win = curses.newwin(box_height, box_width, start_y, start_x)` 
            `textbox = qbox(win)`
        """
        super().__init__(win)
        self.exit_without_saving = False

    def do_command(self, ch):
        if ch == 10:  # Enter key
            return 0
        elif ch == 27:  # ESC key
            self.exit_without_saving = True
            return 0
        else:
            return super().do_command(ch)