from Components.logs import logMessage
from PIL import ImageGrab
import os
from datetime import datetime

def takeScreenshot(output_folder="./ExceptionScreenshots"):
    logMessage("[takeScreenshot] - Started", "INFO")
    os.makedirs(output_folder, exist_ok=True)
    screenshot = ImageGrab.grab()
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    screenshot.save(os.path.join(output_folder, filename), "PNG")
    print()
    logMessage(f"Screenshot saved: {filename}", "ERROR")
    logMessage("[takeScreenshot] - Ended", "INFO")

