from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Blog

def add_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        image = request.FILES.get('image')

        Blog.objects.create(
            title=title,
            content=content,
            author=author,
            image=image
        )

        return redirect('blog_list')

    return render(request, 'add_blog.html')






def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html'
                  , {'blogs': blogs})




def edit_blog(request, id):
    blog = Blog.objects.get(id=id)

    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.content = request.POST.get('content')
        blog.author = request.POST.get('author')

        if 'image' in request.FILES:
            blog.image = request.FILES['image']

        blog.save()
        return redirect('blog_list')

    return render(request, 'edit_blog.html', {'blog': blog})



def delete_blog(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('blog_list')
