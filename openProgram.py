import os
import webbrowser


def openBrave():
    url = 'https://oldschool.runescape.wiki/w/Graceful_outfit'
    webbrowser.register('brave', None, webbrowser.BackgroundBrowser(
        "C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\Brave.exe"))
    # os.startfile('brave.exe')
    webbrowser.get('brave').open(url)


openBrave()
