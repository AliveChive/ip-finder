import requests
import pyperclip
src = requests.get('http://checkip.dyndns.org/').text
src = src = src[76:].replace('</body></html>','').rstrip()
print (src + " Is Your IP.")
print ('Press c to copy')
choice = input ()
if choice.lower() == 'c':
    pyperclip.copy(src)
    print ('Copied')
input()
