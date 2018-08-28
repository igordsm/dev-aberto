from datetime import date

from babel.dates import format_date
import locale
import gettext

gettext.install('messages', localedir='locale')


print(locale.getdefaultlocale())

if __name__ == '__main__':    
    today = date.today()
    print(format_date(today), today)
    
    print(240000000000.32212)
    
    name = input(_('Input your name: '))
    print(_('Hello {}').format(name))
