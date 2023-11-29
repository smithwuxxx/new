from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


# def my_view(request):
#     if request.method == 'POST':
#         # Process the POST data
#         post_data = request.POST
#         # Do something with post_data
#         return render(request, 'my_template.html', {'post_data': post_data})




