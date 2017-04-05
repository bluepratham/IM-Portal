from django.shortcuts import redirect,render, HttpResponse

# Create your views here.

def home(request):
    if not request.user.is_authenticated():
        print("i am anonymous")
        return redirect("/login/")
    print(request.user.is_authenticated(),
          request.user.username)
    return render(request, 'home.html')
