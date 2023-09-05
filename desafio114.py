import urllib
from urllib import request

try:
    site = urllib.request.urlopen('https://wellnet.smartolt.com/auth/login')

except urllib.error.URLError:    #poderia ser só o "except"
    print('Erro ao acessar o site \033[0;31\"https://wellnet.smartolt.com/auth/login\"\033[m')

else:
    print('O site está acessível!')
