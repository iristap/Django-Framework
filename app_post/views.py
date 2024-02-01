from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime

all_posts = [
    {
        'id':1,'title': 'หาเพื่อนตีแบดเย็นนี้','quantity': 4 ,'status':0,
        'datestart': datetime(2023,1,31)
    },
    {
        'id':2,'title': 'หาตี้กินหมูกะทะ','quantity': 5 ,'status':0,
        'datestart': datetime(2023,2,5)
    },
    {
        'id':3,'title': 'หาเพื่อนดูหนังเย็นนี้','quantity': 3 ,'status':1,
        'datestart': datetime(2023,1,25)
    }
]

# Create your views here.
def posts(request):
    context = {'posts': all_posts}
    return render(request, 'app_post/posts.html',context)

def post(request,post_id):
    one_post = None
    try:
        one_post = [p for p in all_posts if p['id'] == post_id][0]
    except IndexError:
        print('ไม่มีpostนี้')
    context = {'post' : one_post}
    return render(request, 'app_post/post.html',context)