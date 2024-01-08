from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer

import jwt,datetime

class GetPerson(APIView):
    def get(self,request):
        people=Person.objects.all()
        seri=PersonSerializer(people,many=True)
        return Response(seri.data)
    
    def post(self,request):
        try:
            data=request.data
            seri=PersonSerializer(data=data)
            if seri.is_valid():
                seri.save()
                return Response(seri.data)
            else:
                return Response({"message":"user  exists"})
        except:
            return Response({"message":"check your passed data"})
        

class LoginUser(APIView):
    def post(self,request):
        try:
            phone=request.data["phone"]
            password=request.data["password"]
            person=Person.objects.filter(phone=phone).first()
            if phone is None:
                return Response({"message":"no such user found"})
            if person.password == password:
                payload={
                    'id':person.id,
                    'iat':datetime.datetime.utcnow(),
                    'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=10)
                }
                token=jwt.encode(payload,'secret',algorithm='HS256')
                return Response({"message":"successful login","token":token})
            return Response({"message":"wrong password"})
        except:
            return Response("check your data")
        


class Deleteuser(APIView):
    def post(self,request):
        try:
            phone=request.data["phone"]
            person=Person.objects.filter(phone=phone).first()
            if not person is None:
                person.delete()
                return Response({'message':'user deleted'})
            else:
                return Response({"message":"no such user"})
        except:
            return Response({"message":"check your data"})
        


class UpdateUser(APIView):
    def put(self,request):
        try:
            phone=request.data["phone"]
            person=Person.objects.filter(phone=phone).first()
            if not person is None:
                seri=PersonSerializer(person,data=request.data)
                if seri.is_valid():
                    seri.save()
                    return Response({"message":"updated"})
            
                return Response({'message':'check data passed'})
            else:
                return Response({"message":"no such user"})
        except:
           return Response({'message':'check data passed'})
