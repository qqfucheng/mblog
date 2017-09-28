from django.shortcuts import render

# Create your views here.


from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from datetime import datetime
from django.shortcuts import redirect

# def homepage(request):
#     posts=Post.objects.all()
#     post_lists=list()
#     for count,post in enumerate(posts):
#         post_lists.append("No.{}:".format(str(count))+str(post)+"<hr>")
#         post_lists.append("<small>" +str(post.body.encode('utf-8')) +"</small><br><br>")
#     return HttpResponse(post_lists)

def homepage(request):
    template=get_template('index.html')
    posts=Post.objects.all()
    now=datetime.now()
    html=template.render(locals())
    return HttpResponse(html)

def showpost(request,slug):
    template=get_template('post.html')
    try:
        post=Post.objects.get(slug=slug)
        if post != None:
            html=template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')