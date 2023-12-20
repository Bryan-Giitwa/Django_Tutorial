from django.http import HttpResponse
from django.template import loader
from .models import member

def members(request):
  mymembers = member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, slug):
  mymember = member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  mydata = member.objects.all().values()
  template = loader.get_template('testing.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

