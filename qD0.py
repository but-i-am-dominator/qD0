import curses

lop = ["Project 1", "Project 2", "Project 3"]

def m1_draw_top(stdscr, width):
    '''Draw the top of the working menu.'''
    title = "qD0 - Task Manager for the Command Line!"
    version = "Version: 0.1"
    full = title + " " * (width - len(title) - len(version) - 3) + version 
    if width > (len(title) + len(version) + 3):
        stdscr.addstr(0, 3, full, curses.color_pair(2))
        stdscr.refresh()
    return True

def m1_draw_bottom(stdscr, width, height):
    '''Draw the bottom of the working menu.'''
    navigate = "Navigate List: ↑, ↓"
    new_task = "New Task / Project: n"
    step_back = "Step back: Esc"
    quit = "Quit: Q ♞"
    buffer = int((width - len(navigate) - len(new_task) - len(step_back) - len(quit) - 4) / 3)
    full = navigate + " " * buffer + new_task + " " * buffer + step_back + " " * buffer + quit
    stdscr.addstr(height - 1, 3, full, curses.color_pair(2))
    stdscr.refresh()
    return True

def c_win(height, width, by, bx, title):
    '''Create Window.'''
    w = curses.newwin(height, width, by, bx)
    w.border(0)
    w.addstr(0, 2, title, curses.color_pair(1))
    w.refresh()
    return w

def set_active(active_window, window_list):
    for w in window_list:
         w[0].addstr(0, 2, w[1], curses.color_pair(3))
         w[0].refresh()
    active_window[0].addstr(0, 2, active_window[1], curses.A_REVERSE)
    active_window[0].move(2, 3)
    active_window[0].refresh()
    return active_window[0]

def draw_project_win(project_win, project_col_width, lop):
     # Project Lists
    l = 11
    project_win.addstr(2, 2,"Dynamic Lists", curses.color_pair(1))
    project_win.addstr(3, 2,"-" * (project_col_width - 4), curses.color_pair(1))
    project_win.addstr(5, 2, "- " + "Today", curses.color_pair(3))
    project_win.addstr(6, 2, "- " + "Tomorrow", curses.color_pair(3))
    project_win.addstr(7, 2, "- " + "Upcoming", curses.color_pair(3))
    project_win.addstr(9, 2, "Projects", curses.color_pair(1))
    project_win.addstr(10, 2,"-" * (project_col_width - 4), curses.color_pair(1))
    for i in lop:
        project_win.addstr(l, 2, "- " + i, curses.color_pair(3))
        l += 1
    return True


def main(stdscr):
    '''Main Function'''
    stdscr.clear()
    stdscr.refresh()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)


    stdscr.clear()
    height, width = stdscr.getmaxyx()
    
    # Draw the Top of the Menu
    m1_draw_top(stdscr, width)
    
    # Draw the Bottom of the Menu
    m1_draw_bottom(stdscr, width, height)
    
    # Window Width
    project_col_width = int(width * 0.15)
    tasks_col_width = int(width * 0.30)
    details_col_width = width - project_col_width - tasks_col_width
    
    # Titles
    project_title = "Projects - F2"
    task_title = "Tasks - F3"
    detail_title = "Task Details - F4"

    project_win = c_win(height - 2, project_col_width, 1, 0, project_title)
    tasks_win = c_win(height - 2,  tasks_col_width, 1, project_col_width, task_title)
    details_win = c_win(height - 2,  details_col_width, 1, project_col_width + tasks_col_width, detail_title)


    draw_project_win(project_win, project_col_width, lop)
        

    # Set the initial active window
    current_win = 1
    aw = set_active((project_win, project_title), [(tasks_win, task_title),(details_win, detail_title)])
    while True:
        key = stdscr.getch()

        # Move between windows
        if key == curses.KEY_F2:
            set_active((project_win, project_title), [(tasks_win, task_title),(details_win, detail_title)])
        elif key == curses.KEY_F3:
            set_active((tasks_win, task_title), [(project_win, project_title),(details_win, detail_title)])
        elif key == curses.KEY_F4:
            set_active((details_win, detail_title), [(project_win, project_title), (tasks_win, task_title)])
        #elif key == curses.KEY_F7:
        #    a = curses.getch()
            
        elif key == ord('q'):
            break





            

if __name__ == "__main__":
    curses.wrapper(main)

