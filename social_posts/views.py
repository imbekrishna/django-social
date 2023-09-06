from django.shortcuts import render


# Create your views here.
def home_view(request):
    print(request.META)
    return render(request, "social_posts/home.html")
