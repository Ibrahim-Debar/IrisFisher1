from django.shortcuts import render 
from django.views import generic 
#import pandas as pd
from django.http import HttpResponse
from .models import IrisManagement
from rest_framework import generics
from .serializers import IrisManagementSerializer

def import_data(request):
	df = pd.read_csv('/Users/afafbenzinoun/Iris/management/iriss.csv', sep=',', engine='python')
	attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width", "classe"]
	df.columns = attributes
 
	for index, row in df.iterrows():
		_, created = IrisManagement.objects.get_or_create(
                sepal_length=row[0],
                sepal_width=row[1],
                petal_length=row[2],
                petal_width=row[3],
                classe=row[4],
                )

	response = "Import done!"
	return HttpResponse(response )



class All(generics.ListCreateAPIView):
    queryset = IrisManagement.objects.all()
    serializer_class = IrisManagementSerializer


class Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IrisManagement.objects.all()
    serializer_class = IrisManagementSerializer