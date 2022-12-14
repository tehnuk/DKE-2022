import json

from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse


def main_page(request):
    return render(request, 'app/main_page.html', {})


def get_count_client(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT count(distinct "Код клиента") from Клиент''')
    result = cursor.fetchone()
    response_data = {
        'data': result[0],
        'status': 200,
        'message': 'Ok.'
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")



