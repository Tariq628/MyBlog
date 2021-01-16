from django.shortcuts import render
from .models import Blogpost, Contact
# Create your views here.
def index(request):
    allProds = []
    products = Blogpost.objects.all()
    for i in products:
        allProds.append(i)
    return render(request, "blog/index.html", {"allProds":allProds})
def prodview(request, myid):
    products = Blogpost.objects.filter(id=myid)
    return render(request, "blog/prodview.html", {"product":products[0]})
def addpost(request):
    if request.method == "POST":
        image = request.FILES["image"]
        heading = request.POST.get("heading", default="")
        content = request.POST.get("content", default="")
        blogpost = Blogpost(image=image, heading=heading, content=content)
        blogpost.save()
    return render(request, "blog/addpost.html")
def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get("name", "default")
        phone = request.POST.get("phone", "default")
        email = request.POST.get("email", "default")
        textarea = request.POST.get("textarea", "default")
        contact = Contact(name=name, phone=phone, email=email, textarea=textarea)
        contact.save()
        thank = True
    return render(request, "blog/contact.html", {"thank":thank})
def search(request):
    return render(request, "blog/search.html")
def blogpost(request):
    return render(request, "blog/blogpost.html")
def about(request):
    return render(request, "blog/about.html")