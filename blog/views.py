from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog
from django.core.paginator import Paginator
from django.utils import timezone


# Create your views here.

def home(request):
    blogs = Blog.objects #blog안의 데이터들 
    blog_list=Blog.objects.all()
    paginator = Paginator(blog_list,3) #블로그 객체 세 개를 한 페이지로 자르기
    page = request.GET.get('page')#request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    posts = paginator.get_page(page)  #request된 페이지를 얻어온 뒤 return 해 준다
    return render(request,'home.html',{'blogs':blogs,'posts':posts})
    # blogs라는 변수를 template에서 쓸때 blogs라는 이름으로 가져오겠다


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id) # object를 가져오고 없으면 404 에러를 띄우라
    return render(request, 'detail.html', {'blog': blog_detail})

def write(request):
    return render(request, 'write.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))