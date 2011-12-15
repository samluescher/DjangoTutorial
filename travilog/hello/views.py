from django.http import HttpResponse
from django.template import Context, loader

def hello(request):


	template = loader.get_template('hello.html')
	context = Context({
		'title': 'Hello World',
		'body': 'This is getting confusing.'
	})

	content = template.render(context)



	return HttpResponse(content)