import curses
import os
import json
import time
from spotipy import SpotifyOauthError
from qbox import qbox
from curses.textpad import rectangle
from data_manage import DatabaseManager
from data_manage import project_table
from qDify import qDify

lop = ["Project 1", "Project 2", "Project 3"]




def m1_draw_top(stdscr, width, spotify):
    '''Draw the top of the working menu.'''
    title = "qD0 - Task Manager for the Command Line!"
    version = "Version: 0.1"
    if spotify == None:
        full = title + " " * (width - len(title) - len(version) - 3) + version 
        if width > (len(title) + len(version) + 3):
            stdscr.addstr(0, 3, full, curses.color_pair(2))
            stdscr.refresh()
    else:
        track_name = spotify[0]
        artist_name = spotify[1]
        full = "qD0" + " " * 10 + track_name + "  by  " + artist_name 
        if width > len(full):
            stdscr.addstr(0, 3, "qD0" + " " * 10, curses.color_pair(2))
            stdscr.addstr(0, 16, track_name + "  by  " + artist_name, curses.color_pair(5))
            stdscr.refresh()
    return True

def m1_draw_bottom(stdscr, width, height):
    '''Draw the bottom of the working menu.'''
    navigate = "Navigate List: ↑, ↓"
    new_task = "New Task / Project: F8"
    step_back = "Step back: Esc"
    quit = "Quit: Q ♞"
    buffer = int((width - len(navigate) - len(new_task) - len(step_back) - len(quit) - 4) / 3)
    full = navigate + " " * buffer + new_task + " " * buffer + step_back + " " * buffer + quit
    stdscr.addstr(height - 1, 3, full, curses.color_pair(2))
    stdscr.refresh()
    return True

def create_window(height, width, by, bx, title):
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
    active_window[0].move(2, 2)
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

def new_project(stdscr):
    '''Function that creates a new project.'''
    stdscr.clear()
    stdscr.refresh()
    # Get the screen dimensions
    screen_height, screen_width = stdscr.getmaxyx()
    # Define the size and position of the text box
    box_height = 3
    box_width = 40
    start_y = (screen_height - box_height) // 2
    start_x = (screen_width - box_width) // 2
    # Create a window for the text box
    win = curses.newwin(box_height, box_width, start_y, start_x)
    # Create a rectangle around the text box
    rectangle(stdscr, start_y - 1, start_x - 1, start_y + box_height, start_x + box_width)
    stdscr.refresh()
    # Create the text box
    textbox = qbox(win)

    # Let the user edit until Enter is pressed
    stdscr.addstr(start_y + box_height + 1, start_x, "Press Enter to save and return to qD0. \n" + (start_x * " ") + "Press Esc to cancel.")
    stdscr.refresh()
    textbox.edit()
    # Get the contents of the text box
    text = textbox.gather()
    stdscr.clear()
    if textbox.exit_without_saving:
        return None
    else:
        return text


def main_screen(stdscr, spotify_data):
    '''Reset Main Screen.'''
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    # Draw the Top of the Menu
    m1_draw_top(stdscr, width, spotify_data)
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

    project_win = create_window(height - 2, project_col_width, 1, 0, project_title)
    tasks_win = create_window(height - 2,  tasks_col_width, 1, project_col_width, task_title)
    details_win = create_window(height - 2,  details_col_width, 1, project_col_width + tasks_col_width, detail_title)

    draw_project_win(project_win, project_col_width, lop)
    # Set the initial active window
    current_win = 1
    aw = set_active((project_win, project_title), [(tasks_win, task_title),(details_win, detail_title)])
    return True


def main(stdscr):
    '''Main Function'''
    
    # Checks if DB file exists.
    if os.path.exists('qD0.db'):
        pass
    else:
        db_manager = DatabaseManager('qD0.db')
        db_manager.create_tables()
    

    stdscr.clear()
    stdscr.refresh()
    
    # Curses Color Pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_GREEN)

    height, width = stdscr.getmaxyx()
    
    # Spotify Integration
    with open("spotify.json") as file:
        data = json.load(file)

    try:
       spot = qDify(data)
       spotify_data = spot.get_currently_playing_track()
       prev_song_info = spotify_data[0]
    except SpotifyOauthError:
        spotify_data = None

    # Window Width
    project_col_width = int(width * 0.15)
    tasks_col_width = int(width * 0.30)
    details_col_width = width - project_col_width - tasks_col_width
    
    # Titles
    project_title = "Projects - F2"
    task_title = "Tasks - F3"
    detail_title = "Task Details - F4"

    project_win = create_window(height - 2, project_col_width, 1, 0, project_title)
    tasks_win = create_window(height - 2,  tasks_col_width, 1, project_col_width, task_title)
    details_win = create_window(height - 2,  details_col_width, 1, project_col_width + tasks_col_width, detail_title)
    main_screen(stdscr, spotify_data)
    stdscr.nodelay(1)
    last_refresh = time.time()
    refresh_interval = 10

    while True:
        now = time.time()
        if now - last_refresh >= refresh_interval:
            try:
                spot = qDify(data)
                spotify_data = spot.get_currently_playing_track()
                if prev_song_info != spotify_data[0]:
                    main_screen(stdscr, spotify_data)
                    prev_song_info = spotify_data[0]
            except SpotifyOauthError:
                spotify_data = None
        key = stdscr.getch()
        # Move between windows
        if key == curses.KEY_F2:
            set_active((project_win, project_title), [(tasks_win, task_title),(details_win, detail_title)])
        elif key == curses.KEY_F3:
            set_active((tasks_win, task_title), [(project_win, project_title),(details_win, detail_title)])
        elif key == curses.KEY_F4:
            set_active((details_win, detail_title), [(project_win, project_title), (tasks_win, task_title)])
        elif key == curses.KEY_F8:
            project = new_project(stdscr)
            if project != None:
                lop.append(project)
            try:
                spot = qDify(data)
                spotify_data = spot.get_currently_playing_track()
            except SpotifyOauthError:
            # Checks if .cache file exists from Spotipy integration.
                #if os.path.exists('.cache'):
                    #os.remove('.cache')
                spotify_data = None
            main_screen(stdscr, spotify_data)
        elif key == ord('q'):
            break
        time.sleep(0.1)
    
if __name__ == "__main__":
    curses.wrapper(main)
