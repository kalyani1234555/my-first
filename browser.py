import webbrowser

webbrowser.open("https://www.python.org/", new=1)
#
# help(webbrowser)
# for i in range(10):
#     print(1, 2, 3, 4, 5, 6, 7, 8, sep="; ", end=" ")

# chrome = webbrowser.get(using='google-chrome')
# chrome.open("https://www.python.org/")
# chrome.open_new("https://www.python.org/")
 
chrome = webbrowser.get('google-chrome %s').open_new_tab("https://www.python.org/")
