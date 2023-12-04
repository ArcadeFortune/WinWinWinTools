# GPT-3: in python, how do i get the height of my windows taskbar?
import ctypes


def get_taskbar_height():
    # Load the user32.dll library
    user32 = ctypes.windll.user32

    # Get the handle to the primary monitor
    # 0 means primary monitor, 2 is MONITOR_DEFAULTTONEAREST
    h_monitor = user32.MonitorFromWindow(0, 2)

    # Create a MONITORINFO structure to store monitor information
    class MONITORINFO(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_uint),
                    ("rcMonitor", ctypes.c_int * 4),
                    ("rcWork", ctypes.c_int * 4),
                    ("dwFlags", ctypes.c_uint)]

    monitor_info = MONITORINFO()
    monitor_info.cbSize = ctypes.sizeof(MONITORINFO)

    # Get monitor information
    user32.GetMonitorInfoW(h_monitor, ctypes.byref(monitor_info))

    # Calculate the taskbar height
    taskbar_height = monitor_info.rcMonitor[3] - monitor_info.rcWork[3]

    return taskbar_height

# GPT-4: in python, how do i get the height of my windows taskbar?
# import ctypes
# from ctypes import wintypes

# # Constants for SystemParametersInfo
# SPI_GETWORKAREA = 48

# # Define RECT structure
# class RECT(ctypes.Structure):
#     _fields_ = [("left", ctypes.c_long),
#                 ("top", ctypes.c_long),
#                 ("right", ctypes.c_long),
#                 ("bottom", ctypes.c_long)]

# def get_taskbar_height():
#     # Create an instance of RECT
#     rect = RECT()

#     # Get the work area (screen size minus the taskbar)
#     ctypes.windll.user32.SystemParametersInfoW(SPI_GETWORKAREA, 0, ctypes.byref(rect), 0)

#     # Screen size
#     screen_width = ctypes.windll.user32.GetSystemMetrics(0) # width
#     screen_height = ctypes.windll.user32.GetSystemMetrics(1) # height

#     # Work area size
#     work_width = rect.right - rect.left
#     work_height = rect.bottom - rect.top

#     # Calculate taskbar height
#     taskbar_height = screen_height - work_height
#     return taskbar_height
