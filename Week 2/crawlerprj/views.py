# Create your views here.
from django.http import HttpResponse
from django import forms
from django.shortcuts import render_to_response
import crawler

class SearchForm(forms.Form):
    searchstring = forms.CharField()
    urlseed = forms.CharField()
    depth = forms.CharField(max_length=2)

def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            searchstring = form["searchstring"].data
            urlseed = form["urlseed"].data
            depth = form["depth"].data
            result = crawler.crawl(searchstring,urlseed,int(depth))
            html = "<html><body>Url's containing search text are: %s</body></html>" % result
            return HttpResponse(html)
    else:
        form = SearchForm()
    return render_to_response('searchhome.html', { 'form' : form,})



