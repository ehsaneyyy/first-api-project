from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from users.models import User
from customer.models import Category,Product
from .serializers import CategorySerializer,ProductSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    email=request.data.get("email")
    password=request.data.get("password")

    user=authenticate(request,email=email,password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        
        response_data={
            "status_code":201,
            "status":"success",
            'refresh': str(refresh),
            'access': str(refresh.access_token),

            "message":"login successful"
            
        }
        return Response(response_data)
    else:
        response_data={
            "status_code":400,
            "status":"error",
            "message":"login is not found"
        }
        return Response(response_data)


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    first_name=request.data.get("first_name")
    last_name=request.data.get("last_name")
    email=request.data.get("email")
    password=request.data.get("password")

    if User.objects.filter(email=email).exists():
     response_data={
         "status_code":400,
         "status":"error",
         "message":"user with this email already exists"

     }
     return Response(response_data)
    
    else:
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        response_data={
         "status_code":201,
         "status":"success",
         "message":"user registered succusfully"
     }
        return Response(response_data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def categories(request):
    categories=Category.objects.all()
    context={
        "request":request
    }
    serializer=CategorySerializer(categories,many=True,context=context)

    response_data={
        "status_code":200,
        "data":serializer.data,
        "message":"successfull"
    }
    return Response(response_data)



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_category(request):
    user =request.user
    name=request.data.get("name")

    category=Category.objects.create(
        name=name,
        user=user
    )
    serializer=CategorySerializer(
       category,context={"request":request}
   )
    response_data={
        "status_code":200,
        "status":"success",
        "message":"succesfull",
        "data":serializer.data
    }
    return Response(response_data)
    

@api_view(["PUT","PATCH"])
@permission_classes([IsAuthenticated])
def edit_category(request, id):
    user=request.user
    name=request.data.get("name")
    category=Category.objects.get(id=id,user=user)

    if name:
        category.name = name
    category.save()

    serializer=CategorySerializer(
        category,context={"request":request}
    )
    response_data={
        "status_code":200,
        "status":"success",
        "message":"succcessfull",
        "data":serializer.data,
    }
    return Response(response_data)


    

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_category(request, id):
    category=Category.objects.get(id=id,user=request.user)
    category.delete()
    response_data={
        "status_code":200,
        "status":"success",
        "message":"succcessfull",
    }
    return Response(response_data)


    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def products(request):
    products=Product.objects.filter(user=request.user)
    context={
        "request":request
    }
    serializer=ProductSerializer(products,many=True,context=context)
    response_data={
         "status_code":200,
         "data":serializer.data,
         "message":"successfull"
     }
    return Response(response_data)
    



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_product(request):
    user=request.user
    serializer=ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=user)
        return Response({
        "status_code":200,
        "data":serializer.data,
        "message":"successfull"
        })
    
    return Response(serializer.errors,status=400)

@api_view(["PUT","PATCH"])
@permission_classes([IsAuthenticated])
def edit_product(request, id):
    user=request.user
    products=Product.objects.get(id=id,user=request.user)
    serializer=ProductSerializer(products,data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({
        "status_code":200,
        "data":serializer.data,
        "message":"successfull"
        })
    return Response(serializer.errors,status=400)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_product(request, id):
    products=Product.objects.get(id=id,user=request.user)
    products.delete()
    response_data={
        "status_code":200,
        "status":"success",
        "message":"successfull"
    }
    return Response(response_data)
    
    