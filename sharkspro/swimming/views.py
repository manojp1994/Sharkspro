from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.clickjacking import xframe_options_exempt
from django.core.context_processors import csrf
from django.template import RequestContext
from forms import ReviewsForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from swimming.models import *
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

# Create your views here.
def index(request):
	args={}
	return render_to_response("index.html",args)

def accomplishments(request):
	args={}
	return render_to_response("Accomplishments.html",args)

@xframe_options_exempt
def about(request):
	args={}
	return render_to_response("about.html",args)

def safetymeasures(request):
	args={}
	return render_to_response("safetymeasures.html",args)

def home(request):
	args={}
	return render_to_response("index.html",args)

def contact(request):
	args={}
	return render_to_response("contact.html",args)

def gallery(request):
	args={}
	return render_to_response("gallery.html",args)

@csrf_protect
def reviews(request):
	print "manoj"
	args = {}
	args.update(csrf(request))
	name = request.POST.get('PostedName')
	mobile = request.POST.get('PostedMobile')
	review = request.POST.get('PostedReview')
	if request.POST:
		form = ReviewsForm(request.POST)
		if form.is_valid():
			form.save()
			html = "<html><body>Your review has been posted.Thanks for review</body></html>"
			return HttpResponse(html)
	print name
	print mobile
	print review
	html = "<html><body>Form Error</body></html>"
	return HttpResponse(html)
	# return render_to_response('index.html',{'form':form}, context_instance=RequestContext(request))