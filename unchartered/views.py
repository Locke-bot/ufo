from django.shortcuts import render

# Create your views here.

def HomePage(request):
    template_name = 'homepage.html'
    categories = ['Real Time Text', 'Music Stream', 'Movie Stream', 'File Transfer']
    return render(request, template_name, context=dict(categories=categories))