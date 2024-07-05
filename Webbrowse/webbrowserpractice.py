# importing the webbrowser module
import webbrowser

# opening an URL in different web browser
chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))

web = webbrowser.get('chrome')
web.open("https://www.javatpoint.com/snmp-module-in-python")
web.open_new_tab("https://www.javatpoint.com/speech-recognition-python")