from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse

from BetweenTheoryAndPracticeEX2App.models import User
from BetweenTheoryAndPracticeEX2App.serializers import UserSerializer
import xlwt
import re

from django.core.files.storage import default_storage


# Create your views here.


@csrf_exempt
def userApi(request, id=0):
    if request.method == 'GET':
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)


@csrf_exempt
def filteredData(request):
    if request.method == 'GET':
        data = request.GET
        users = User.objects.all()

        chosen_city = data.get('city')
        from_date = data.get('from')
        till_date = data.get('till')
        if chosen_city:
            users = users.filter(city=chosen_city)

        elif from_date and till_date:
            date = re.compile(r"\d{4}-\d{2}-\d{2}")

            if re.fullmatch(date, from_date) and re.fullmatch(date, till_date):
                users = users.filter(birth_date__range=[from_date, till_date])

        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)


@csrf_exempt
def exportToExcel(request):
    if request.method == 'GET':
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=Summary.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users Summary')
        row_num = 0

        cols = [
            '#id',
            'First Name',
            'Last Name',
            'Birth Date',
            'Address',
            'City',
            'Zip Code',
            'Landline',
            'Cellular Phone',
            'Is Covid 19 Infected',
            'Have Diabetes',
            'Have Cardio Problems',
            'Have Allergies',
            'Have Other Medical Conditions',
        ]

        for i, value in enumerate(cols):
            ws.write(row_num, i, value)

        rows = User.objects.all().values_list(
            'id',
            'first_name',
            'last_name',
            'birth_date',
            'address',
            'city',
            'zip_code',
            'landline',
            'cellular_phone',
            'is_covid_19_infected',
            'have_diabetes',
            'have_cardio_problems',
            'have_allergies',
            'have_other_medical_conditions'
        )

        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, str(row[col_num]))

        wb.save(response)
        return response
