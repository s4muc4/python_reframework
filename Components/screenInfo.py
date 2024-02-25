from screeninfo import get_monitors

def get_screen_resolution():
    monitors = get_monitors()
    
    if monitors:
        primary_monitor = monitors[0]
        width, height = primary_monitor.width, primary_monitor.height
        return f'Your resolution is: {width}x{height}'
    else:
        return 'Was not possible to get resolution'


