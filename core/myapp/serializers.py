from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from myapp.models import Company, Employes


class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = '__all__'

class EmployesSerializer(serializers.ModelSerializer):    
    companyid= CompanySerializer()

    class Meta:
        model = Employes
        fields = '__all__'

class AddEmployesSerializer(serializers.ModelSerializer):        

    class Meta:
        model = Employes
        fields = '__all__'


class UpdateEmployesSerializer(serializers.ListSerializer):
    """ Recibe dos listas para comparar los datos """

    class Meta:
        model = Employes
        fields = '__all__'


    def update(self, instance, validated_data):        

        #instance = valor original (de la bd)
        #validated_data = valor a comparar
        mapping = {emp.employeid: emp for emp in instance}
        data_mapping = {item['employeid']: item for item in validated_data}
        
        # Realizamos las creaciones si no se encuentran en data_mapping,
        # y las actualizaciones si se encuentran keys en data_mapping
        ret = []
        for _id, data in data_mapping.items():
            emp = mapping.get(_id, None)            
            if emp is None:                
                ret.append(self.child.create(data))             #Si no se encuentra se crea
            else:                
                ret.append(self.child.update(emp, data))        #Se se encuentra se actualiza

        # Realizamos las eliminaciones, si no se encuentra en data_mapping
        for _id, data in mapping.items():
            if _id not in data_mapping:
                data.delete()

        return ret



class AddListEmployesSerializer(serializers.ModelSerializer):
    employeid = serializers.IntegerField()

    class Meta:
        list_serializer_class = UpdateEmployesSerializer  #list_serializer_class , nos sirve para trabajar con varios objetos en forma de listas, util para Insert, Update, Delete
        model = Employes
        fields = '__all__'


