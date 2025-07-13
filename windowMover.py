import requests, win32gui

def find_roblox_studio_window():
    results = []
    def enum_windows(hwnd, results):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if "Roblox Studio" in title:
                results.append(hwnd)
    win32gui.EnumWindows(enum_windows, results)
    return results[0] if results else None

def move_window(hwnd, x, y, width, height):
    if not hwnd:
        print("Window not found.")
        return
    win32gui.MoveWindow(hwnd, x, y, width, height, True)
    print(f"Moved window to ({x},{y}) size {width}x{height}")

# 👇 just replace this with your GitHub raw URL
raw_url = "https://raw.githubusercontent.com/youruser/yourrepo/main/position.json"

try:
    data = requests.get(raw_url).json()
    hwnd = find_roblox_studio_window()
    move_window(
        hwnd,
        data.get("x", 100),
        data.get("y", 100),
        data.get("width", 1280),
        data.get("height", 720)
    )
except Exception as e:
    print("Error:", e)