from django.shortcuts import render
from blog.models import Post, Categoria # traer desde models.py de al App Blog

# Create your views here.

def blog(request):
    posts=Post.objects.all() # importe todos los objetos que hayamos construido
    return render(request,"blog/blog.html",{"posts": posts}) #return HttpResponse("Servicios")
   #return render(request,"blog/blog.html") #return HttpResponse("Blog")

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {'categoria':categoria,"posts": posts})