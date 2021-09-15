from pywinauto.application import Application
from pywinauto.findwindows import find_window
from pywinauto import keyboard
import pywinauto
import win32gui


def no_double_click_time():
    return 0

win32gui.GetDoubleClickTime = no_double_click_time

def limitOn():

    # app = Application().connect(process=(GTA_PID))
    hello = find_window(best_match='Realm Grinder')
    app = Application().connect(handle=hello)
    win = app.window(title='Realm Grinder')

    win32gui.GetDoubleClickTime = no_double_click_time #removes the click delay in windows


    win.SetFocus()
    while True:
        pywinauto.mouse.click(button='left', coords=(3011, 553))
        #keyboard.send_keys("{%}")
        #pywinauto.mouse.click(button='left', coords=(3225, 459))


isRunning = True

while True:
    no_double_click_time()
    limitOn()

