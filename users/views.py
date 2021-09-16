from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import UserProfile ,TopicTag , Member
from .serializers import (MemberSerializer, TopicTagSerializer, UserProfileSerializer, UserSerializer,
                          UserSerializerWithToken, CurrentUserSerializer)


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def post(self, request):
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        messages = {'errors':[]}
        if username == None:
            messages['errors'].append('username can\'t be empty')
        if email == None:
            messages['errors'].append('Email can\'t be empty')
        if password == None:
            messages['errors'].append('Password can\'t be empty')
        if User.objects.filter(email=email).exists():
            messages['errors'].append("Account already exists with this email id.")    
        if User.objects.filter(username__iexact=username).exists():
            messages['errors'].append("Account already exists with this username.") 
        if len(messages['errors']) > 0:
            return Response({"detail":messages['errors']},status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.create(
                username=username,
                email=email,
                password=make_password(password)
            )
            serializer = UserSerializerWithToken(user, many=False)
        except Exception as e:
            print(e)
            return Response({'detail':f'{e}'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # token['userProfile'] = user.userprofile
        token['email'] = user.email
        token['username'] = user.username
        token['name'] = user.userprofile.name
        token['profile_pic'] = 'static' + user.userprofile.profile_pic.url
        token['is_staff'] = user.is_staff
        token['id'] = user.id
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




@api_view(['GET'])
def user(request, username):
    user = User.objects.get(username=username)

    if(request.user.username == username):
        serializer = CurrentUserSerializer(user, many=False)
        return Response(serializer.data)

    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def profile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


# class UserProfileUpdate(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserProfileSerializer


#     def patch(self, *args, **kwargs):
#         profile = self.request.user.userprofile
#         serializer = self.serializer_class(
#             profile, data=self.request.data, partial=True)
#         if serializer.is_valid():
#             user = serializer.save().user
            
#             response = {'success': True, 'message': 'successfully updated your info',
#                         'user': UserSerializer(user).data}
#             new_email = self.request.data.get('email')
#             user = self.request.user
#             if new_email is not None:
#                 user.email = new_email
#                 user.save()
#                 profile.save()
#             return Response(response, status=200)
#         else:
#             response = serializer.errors
#             return Response(response, status=401)

@api_view(['PATCH'])
@permission_classes((IsAuthenticated,))
def UserProfileUpdate(request):
    profile= request.user.userprofile
    data= request.data["data"]
    if request.data["id"] != "":
        try:
            member = Member.objects.get(id = request.data["id"])
            member.name = data["name"]
            member.character = data["character"]
            member.lastName = data["lastName"]
            member.gender = data["gender"]
            member.city = data["city"]
            member.birth_day_date = data["birth_day_date"]
            member.phoneNumber = data["phoneNumber"]
            member.save()
            serializer = MemberSerializer(member , many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"details": f"{e}"})
    else:
        try:
            profile.name = data["name"]
            profile.character = data["character"]
            profile.lastName = data["lastName"]
            profile.gender = data["gender"]
            profile.city = data["city"]
            profile.birth_day_date = data["birth_day_date"]
            profile.phoneNumber = data["phoneNumber"]
            profile.save()
            serializer = UserProfileSerializer(profile , many=True)  
            return Response(serializer.data)
        except Exception as e:
            return Response({"details": f"{e}"})


class ProfilePictureUpdate(APIView):
    permission_classes=[IsAuthenticated]
    serializer_class=UserProfileSerializer
    parser_class=(FileUploadParser,)
    def patch(self, *args, **kwargs):
        profile_pic=self.request.FILES.get('profile_pic')
        setattr(self.request.user.userprofile, 'profile_pic', profile_pic)
        serializer=self.serializer_class(
            self.request.user.userprofile, data={}, partial=True)
        if serializer.is_valid():
            user=serializer.save().user
            response={'type': 'Success', 'message': 'successfully updated your info',
                        'user': UserSerializer(user).data}
        else:
            response=serializer.errors
        return Response(response)

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def ProfilePictureDelete(request):
    user = request.user.userprofile
    user.profile_pic.url = 'default.png'
    return Response({'detail':'Profile picture deleted '})


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def delete_user(request):
    user = request.user
    user.delete()
    return Response({'detail':'Account deleted successfully'},status=status.HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes((IsAuthenticated,))
def update_interests(request): 
    user_profile = request.user.userprofile
    interests = request.data.get("name")
    if request.data.get("id") != "":
        member_id = request.data.get("id")
        member= Member.objects.get(id = member_id)
        member.interests.set(
            TopicTag.objects.get(name=interest) for interest in interests
        )
        member.save()
        serializer = MemberSerializer(member, many=False)
        return Response(serializer.data)
    else:
        user_profile.interests.set(
                TopicTag.objects.get(name=interest) for interest in interests
        )
        user_profile.save()
        serializer = UserProfileSerializer(user_profile, many=False)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getIntrests(request):
    intrests = TopicTag.objects.all()
    serializer = TopicTagSerializer(intrests,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def createMember(request):
    data = request.data
    user = request.user
    try:
        member= Member.objects.create(
            parent=user,
            username=data["username"],
            character= data["character"],
            name=data["name"],
            lastName=data["lastName"],
            gender= data["gender"],
            city=data["city"],
            birth_day_date= data["birth_day_date"],
        )
        serializer = MemberSerializer(member, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response({"details": f"{e}"})

@api_view(['PATCH'])
@permission_classes((IsAuthenticated,))
def updateMemberInterest(request, id):
    user= request.user
    interests = request.data.get("name")
    member = Member.objects.get(id=id)

    try:
        if user == member.parent:
            member.interests.set(
                TopicTag.objects.get(name=interest) for interest in interests
            )
            return Response({"details": "member updated"})
        else:
            return Response({"details": "unAuthorized"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({"details": f"{e}"})