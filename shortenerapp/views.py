from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import URLModel
from .forms import URLSubmitForm


def url_redirect(request, shortcode=None):
    obj = get_object_or_404(URLModel, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)


def home(request):
    if request.method == 'POST':
        form = URLSubmitForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            obj, created = URLModel.objects.get_or_create(url=url)
            return redirect('success', shortcode=obj.shortcode)
    else:
        form = URLSubmitForm()
    context = {
        'form': form,
    }
    return render(request, 'home.html', context)


def success(request, shortcode=None):
    obj = get_object_or_404(URLModel, shortcode=shortcode)
    context = {
        'obj': obj,
    }
    return render(request, 'success.html', context)
