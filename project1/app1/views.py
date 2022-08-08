from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from . import models
from . import forms
from django.views.decorators.cache import cache_control
# Create your views here.


@cache_control(no_cache=True,must_revalidate=True,no_store=True) 
def logging(req):
    if req.method=="POST":
        u=req.POST['username']
        p=req.POST['passw']
        if u=='tamil' and p=='tamil':
            req.session['authoriser']=u
            return render(req,"home.html")
        else:
            return render(req,"login.html",{"info":"invalid credentials"})
    else:
        return render(req,"login.html")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)    
def show(req):
    if req.session.has_key('authoriser'):
      return render(req,"home.html")
    else:
      return render(req,"login.html")    


@cache_control(no_cache=True,must_revalidate=True,no_store=True)    
def callCreate(req):
    if req.session.has_key('authoriser'):
        if req.method=="POST":
           object=forms.MoviesForm(req.POST)
           if object.is_valid():
               object.save()    
               #return render("/tamil/new")
               obj=forms.MoviesForm()
               return render(req,"create.html",{"hey":obj,"title":"New Movie added"})
        else:
           obj=forms.MoviesForm()
           return render(req,"create.html",{"hey":obj,"title":"New Movie"})  
    else:
       return render(req,"login.html")

         
@cache_control(no_cache=True,must_revalidate=True,no_store=True)    
def callEdit(request,new):
   if request.session.has_key('authoriser'): 
        if request.method=="POST":
           obj=models.Movies.objects.get(id=new)
           exist=forms.MoviesForm(request.POST,instance=obj)
           if exist.is_valid():
               exist.save()
               return redirect('/tamil/home');
        else:
           obj=models.Movies.objects.get(id=new)
           exist=forms.MoviesForm(instance=obj)
           return render(request,"edit.html",{"hey":exist,"title":"UPDATE THE MOVIE"})
   else:
        return render(request,'login.html')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)            
def callDelete(req,remove):
    if req.session.has_key('authoriser'): 
        obj=get_object_or_404(models.Movies,id=remove)
        models.Movies.delete(obj)
        return redirect("/tamil/home")    
    else:
        return render(req,'login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)            
def callRead(req,number):
    if req.session.has_key('authoriser'): 
       obj=models.Movies.objects.get(id=number)
       return render(req,"read.html",{"single":obj})
    else:
        return render(req,'login.html')   
    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)            
def callList(req):
   if req.session.has_key('authoriser'): 
      obj=models.Movies.objects.all()
      return render(req,"list.html",{"mylist":obj})
   else:
        return render(req,'login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)            
def callShort(req):
    if req.session.has_key('authoriser'): 
        if req.method=="POST":
            data=[]
            yr=req.POST['year']
            lg=req.POST['languages']
            rt=req.POST['rating']
            if yr!="" and lg=="" and rt=="":
               print("Based on released year")
               yr=int(yr)
               data=models.Movies.objects.filter(ReleasedYear__gte=yr)
            elif yr=="" and lg!="" and rt=="":
               print("Based on Languages")
               data=models.Movies.objects.filter(Languages__icontains=lg)
            elif yr=="" and lg=="" and rt!="":
               print("Based on Rating")
               rt=float(rt)
               data=models.Movies.objects.filter(Rating__gte=rt)
            else:
               print("invalid")
               return render(req,"list.html",{"mylist":data})
        else:
           return render(req,"shortlist.html")
    else:
        return render(req,'login.html')       


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def callOut(req):
    if req.session.has_key('authoriser'): 
        req.session['authoriser']=""
        del req.session['authoriser']
        return redirect("/tamil/")   
    else:
        return render(req,'login.html')          