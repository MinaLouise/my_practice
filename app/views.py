from django.shortcuts import render
from app.forms import AddForm, SignUpForm

# Create your views here.
def root(request):
    context = {}
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            context["signup_success"] = True
    else:
        form = SignUpForm()
    context["form"] = form
    return render(request, "root.html", context)

def add(request):
    form = AddForm(request.GET)

    if form.is_valid():
        x = form.cleaned_data['x']
        y = form.cleaned_data['y']
        z = form.cleaned_data['z']
        answer = x+y
        return render(request,"add.html",{"form": form, "x": x, "y": y, "z": z, "answer": answer})
    else:
        return render(request,"add.html", {"form": form})
