from django.shortcuts import render

# Create your views here.
def home(request):
    # products = Product.objects.all().filter(is_available=True)
    # context = {
    #     'products': products,
    # }
    return render(request, 'home.html')