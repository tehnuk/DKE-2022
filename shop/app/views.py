from django.shortcuts import render


from django.shortcuts import render


def main_page(request):
    return render(request, 'app/main_page.html', {})