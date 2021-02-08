from django import template
from django.utils.safestring import mark_safe

register = template.Library()
import math



def picturegrid (photos, arg):
    rows = math.ceil(photos.count()/arg)
    html=''
    for i in range(0,rows):
        html=html+'<div class="row">'
        if photos.count()<(i+1)*arg:
            column=photos.count()%arg
        else:
            column=arg
        for j in range(0,column):
            html=html+'<div class="column"> <img src="{url}" style="width:100%"> </div>'.format(url=photos[i*arg+j].grams.url)
        html=html+'</div>'

    return mark_safe(html)
    #return html


register.filter('picturegrid', picturegrid)
