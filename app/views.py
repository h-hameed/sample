from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Header, Line
from .forms import HeaderForm, LineFormSet

def header_create_view(request):
    if request.method == "POST":
        form = HeaderForm(request.POST)
        formset = LineFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            header = form.save()
            lines = formset.save(commit=False)
            for line in lines:
                line.header = header
                line.save()
            return redirect('header_list')  # Replace with your success URL
    else:
        form = HeaderForm()
        formset = LineFormSet()
    return render(request, 'app/header_form.html', {'form': form, 'formset': formset})