from django.shortcuts import render,redirect,reverse
from .models import asset
from .forms import LoginForm,ItemDownloadForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def publicView(request):
    if request.user.is_authenticated:
        assets = asset.objects.all()
    else:
        assets = asset.objects.filter(publicity_status="PUBLIC")
    context={
        "all_objects":assets,
    }
    return render(request,"index.html",context)

def privateAllView(request):
    assets = asset.objects.all()
    if request.user.is_authenticated:
        context={
            "all_objects":assets

        }
        return render(request,"index.html",context)
    else:
        return redirect(reverse("login_form"))
def loginForm(request):
    if request.method=="POST":
        
        user = authenticate(username=request.POST["username"],password=request.POST["password"])
        if user is not None:
            login(request,user)
            return redirect(reverse("main_view"))
        else:
            return redirect(reverse("main_view"))

    
    else:
        form = LoginForm()
        context ={"form":form}
        return render(request,"login.html",context)
    
def filedownloadView(request,i):
    item =  asset.objects.all().filter(item_id=i)[0]
    print(item)
    public_viewable=None
    if item.publicity_status=="PUBLIC":
        public_viewable = False
    else:
        public_viewable=True
    
    context={"file":item,
    "status":public_viewable,
    "PRIVATE":"PRIVATE"}
    return render(request,"download.html",context)


def downloadSearchView(request):
    if request.method=="POST":
        print(request.POST)
        
        item = asset.objects.all().filter(item_id=request.POST['item_id'])[0]
        print(item)
        url_resolve = reverse("download_view",kwargs={'i':item.item_id})
        return redirect(url_resolve)
        
    else:
        form = ItemDownloadForm()
        context ={"form":form}
        return render(request,"downloadform.html",context)

def logoutFunc(request):
    logout(request)
    return redirect(reverse("main_view"))