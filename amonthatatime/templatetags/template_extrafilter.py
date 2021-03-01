from django import template
from django.utils.safestring import mark_safe

register = template.Library()
import math



def picturegrid (photos, arg):
    cnt = math.ceil(photos.count())
    rows = math.ceil(photos.count()/arg)
    html='<div class="row">'

    html_dic={}

    for i in range(0,arg):
        html_dic[i]='<div class="column">'

    for i in range(0,rows):
        if photos.count()<(i+1)*arg:
            column=photos.count()%arg
        else:
            column=arg
        for j in range(0,column):
            html_dic[j]=html_dic[j]+'<div class="container"> <img src="{url}"> <div class="overlay">{caption}</div> </div>'.format(url=photos[i*arg+j].urls,caption=photos[i*arg+j].caption)

    for i in range(0,arg):
        html=html+html_dic[i]+'</div>'

    html=html+'</div>'



    return mark_safe(html)
    #return html


register.filter('picturegrid', picturegrid)
