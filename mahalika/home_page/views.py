from django.shortcuts import render

posts = [
    {
        'author': 'M',
        'title': '1st Post',
        'content': '1st Content',
        'date_posted': 'October 5, 2022',
    }  , {
        'author': 'D',
        'title': '2nt Post',
        'content': '2nt Content',
        'date_posted': 'October 6, 2022',
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request,'home-page/home.html',context)

def about(request):
    return render(request,'home-page/about.html',{'title':'About'})
