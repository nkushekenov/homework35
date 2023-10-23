from django.shortcuts import render

def example_template_view(request):
    return render(request, 'example_template.html')
