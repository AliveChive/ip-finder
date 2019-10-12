import requests
import pyperclip
src = requests.get('https://api.ipify.org').text
print (src + " Is Your IP.")
print ('Press c to copy')
choice = input ()
if choice.lower() == 'c':
    pyperclip.copy(src)
    print ('Copied')
input()
