from django.shortcuts import render

# Index page view
def index(request):
    return render(request, 'index.html')

# About page view
def about(request):
    return render(request, 'about.html')  # This points to the 'about.html' template
