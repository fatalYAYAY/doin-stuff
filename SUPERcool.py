from flask import Flask, request
import win32gui

app = Flask(__name__)

def move_window_by_hwnd(hwnd, x, y, width, height):
    if hwnd == 0 or hwnd is None:
        return "Window not found", 404
    win32gui.MoveWindow(hwnd, x, y, width, height, True)
    return "Window moved", 200

def find_roblox_studio_window():
    results = []
    def enum_windows(hwnd, results):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if "Roblox Studio" in title:
                results.append(hwnd)
    win32gui.EnumWindows(enum_windows, results)
    return results[0] if results else None

@app.route('/moveWindow', methods=['POST'])
def move_window():
    data = request.get_json()
    x = data.get('x')
    y = data.get('y')
    width = data.get('width', 1280)
    height = data.get('height', 720)
    hwnd = find_roblox_studio_window()
    return move_window_by_hwnd(hwnd, x, y, width, height)

if __name__ == "__main__":
    app.run(port=1337)
