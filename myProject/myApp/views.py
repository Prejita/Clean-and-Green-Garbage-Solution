from django.shortcuts import render

def index(request):
    context={}
    return render(request, "myApp/index.html", context)

def login(request):
    context={}
    return render(request, "myApp/login.html", context)

def about(request):
    context={}
    return render(request, "myApp/about.html", context)

def blog_post1(request):
    context={}
    return render(request, "myApp/blog-post-1.html", context)

def blog_post2(request):
    context={}
    return render(request, "myApp/blog-post-2.html", context)

def blog_post3(request):
    context={}
    return render(request, "myApp/blog-post-3.html", context)

def blog_post4(request):
    context={}
    return render(request, "myApp/blog-post-4.html", context)

def blog(request):
    context={}
    return render(request, "myApp/blog.html", context)

def contact(request):
    context={}
    return render(request, "myApp/contact.html", context)

def dashboard(request):
    context={}
    return render(request, "myApp/dashboard.html", context)

def termsandconditions(request):
    context={}
    return render(request, "myApp/terms-and-conditions.html", context)



