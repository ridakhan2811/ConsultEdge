from django.shortcuts import render

# Create your views here 
def home(request):
    """
    Renders the home.html template for the main page.
    """
    # The render() function takes the request object, the template path,
    # and a dictionary of context to pass to the template.
    # In this case, we are not passing any context.
    return render(request, 'accounts/home.html')
