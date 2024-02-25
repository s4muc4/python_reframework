from Components.logs import logMessage
from Components.killProcess import killProcess



def killAllProcess():

    logMessage("[killAllProcess] - Started", "INFO")

    killProcess("chrome")
    killProcess("excel")

    logMessage("[killAllProcess] - Ended", "INFO")