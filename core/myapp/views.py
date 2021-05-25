from rest_framework.serializers import Serializer
import myapp
from myapp.models import Employes
from myapp import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import  status
from django.shortcuts import render

# Create your views here.
class EmployesApiView(GenericAPIView):

    def get(sef, request):
       
        #Obtener todos los empleados
        emp = Employes.objects.all()
        #Serializar el objeto empleados
        se = serializers.EmployesSerializer(emp, many=True)       
        
        payload = {
            'codigo': status.HTTP_200_OK,
            'mensaje': 'Ok',
            'data': se.data 
        }          

        #Retornamos el valor
        return Response(payload, status=status.HTTP_200_OK);

    def put(self, request):
         # Obtener el  JSON
         data = request.data

         # Serializar los datos
         se = serializers.AddEmployesSerializer(data=data)

         #validar y guardar
         if se.is_valid():
            se.save()
            payload = {
               'codigo': status.HTTP_200_OK,
               'mensaje': 'Ok',
               'data': se.data 
            }
         else:
            payload = {
                'codigo': status.HTTP_400_BAD_REQUEST,
                'mensaje': 'Fallo',
                'data': se.errors
            }   

         return Response(payload, status=status.HTTP_200_OK);
    
    def post(self, request):
        """ Ejemplo de manejo de listas en Serializer

         
          Para este ejemplo asumimos lo siguiente:
          Se tienen que enviar todos los datos existentes de los empleados en el JSON ya que
          se comparara con la base de datos y :
           1.- Si se encuentran se actualizan los datos,
           2.- Si no existen en la base de datos  se crean,
           3.- Si se encuentran en la base de datos, pero no fueron pasados en el JSON se elimnan.

         """

        # Obtener el  JSON.
        data = request.data

        # Obtener los datos de la base de datos        
        emp = Employes.objects.all()
        #Es necesario pasarlo a listas
        _arr_emp = [entry for entry in emp]

        # Serializar los datos
        se = serializers.AddListEmployesSerializer(instance=_arr_emp, data = data, many = True)
        

        #validar y guardar
        if se.is_valid():            
            se.save()
            payload = {
                'codigo': status.HTTP_200_OK,
                 'mensaje': 'Ok',  
                 'data': se.data 
            }
        else:
            payload = {
                'codigo': status.HTTP_400_BAD_REQUEST, 
                'mensaje': 'Fallo',  
                'data': se.errors
            }   

        return Response(payload, status=status.HTTP_200_OK);