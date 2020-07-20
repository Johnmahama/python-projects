import webbrowser

url = input("Paste URL to download: ")
download =url[:12]+"ss"+url[12:]
webbrowser.open_new(download)