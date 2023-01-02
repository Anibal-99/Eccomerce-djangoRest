from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

@api_view(['GET', 'POST']) #lo que primero devemos poner en el decorador son los metodos http que se van a permitir
def user_api_view(request):

    # lista todos los objetos
    if request.method=='GET':
        users= User.objects.all().values('id', 'username', 'email', 'password') # le decimos que traiga todos los usuarios
        users_serializer=UserSerializer(users, many=True) #convierte todos los usuarios a json

        return Response(users_serializer.data, status=status.HTTP_200_OK)

    # create un nuevo objeto
    elif request.method=='POST':
        users_serializer= UserSerializer(data= request.data) # lo que hace aca es deserializar el json y lo convierte en un objeto para compararlo con el modelo
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data, status=status.HTTP_201_CREATED)
        return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
    # consulta que trae el objeto user perteneciente a la pk que le pasamos
    user = User.objects.filter(id=pk).first()

    if user:

        if request.method=='GET':
            user_serializer=UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        elif request.method=='PUT':
            user_serializer=UserSerializer(user, data=request.data) # actualiza la instancia user que le pasamos con la nueva informacion que le pasamos en el request.data

            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)

            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method=='DELETE':
            user.delete()
            return Response({'message': 'Usuario eliminado correctamente'}, status=status.HTTP_200_OK)
    return Response({'message': 'No se ha encontrado un usuario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
