from django.shortcuts import render
from .models import Image, Category, Location
# Create your views here.



def welcome(request):
    images = Image.get_all_images()
    categories = Category.objects.all()
    locations = Location.objects.all()
    return render(request, 'welcome.html', {"images": images, 'categories': categories,'locations':locations})


def search_image(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        found_results = Image.get_image_by_categ(search_term)
        message = f"{search_term}"
        print(found_results)

        return render(request, 'search.html',
        {'found_results': found_results, 'message': message, 'categories': categories,
        "locations": locations})
    else:
        message = 'Please search first'
        return render(request, 'search.html', {"message": message})


def category(request):
    categories = Image.get_all_images()
    return render(request, 'category.html', {"categories": categories})


def get_image_by_location(request,pahali):
    my_images = Image.get_image_by_location(pahali)
    print(my_images)
    return render(request, 'location.html', {"my_images": my_images})


def single_image(request,image_id):
    image=Image.objects.get(id = image_id)
    return render(request, 'image.html',{"image":image})