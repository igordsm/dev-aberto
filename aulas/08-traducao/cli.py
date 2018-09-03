from datetime import date
from babel.dates import format_date, format_datetime, format_time
from babel.numbers import format_number, format_decimal, format_percent
import gettext
gettext.install('cli', localedir='locale')





LANGUAGE = 'en_US.utf8'

if __name__ == '__main__':    
    today = date.today()
    print(format_date(today, locale=LANGUAGE))
    
    print(format_decimal(240000000000.32212, locale=LANGUAGE))
    
    name = input(_('Input your name: '))
    print(_('Hello {}'.format(name)))
