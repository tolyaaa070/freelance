from django.shortcuts import render
from rest_framework import viewsets, generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .permission import CheckOffer, CheckRole, CheckOwner ,CheckRoleReview


from .models import (UserProfile,SocialLink,Skill,Review,Category,Project,Offer)
from .serializers import (SkillSerializers,CategoriesSerializers,CategoryDetailSerializers,
                          UserProfileSerializers,OtherUserProfileSerializers ,SocialLinkSerializers,
                          ProjectListAPISerializers,ProjectDetailSerializers,LoginSerializer,
                          ReviewsSerializers,UserSerializer,OfferMySerializers,OfferSerializers,OfferListAPISerializers)
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        from rest_framework.response import Response
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
class MyProfileViewSet(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class EditMyProfileViewSet(generics.RetrieveUpdateDestroyAPIView ):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

class OthersProfileViewSet(generics.RetrieveAPIView ):
    queryset = UserProfile.objects.all()
    serializer_class = OtherUserProfileSerializers

class SkillViewSet(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializers

class ProjectListAPIViewSet(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListAPISerializers

class ProjectDetailViewSet(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializers
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title', 'description','category','status']
    ordering_fields = ['budget', 'created_at', 'deadline']
    permission_classes = [CheckOwner]

class MyProjectView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListAPISerializers

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

class ProjectCreateViewSet(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializers
    # permission_classes = [CheckRole]

class ProjectEditViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializers

class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializers

class CategoriesViewSet(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializers

class CategoryDetailViewSet(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializers

class OfferCreateViewSet(generics.CreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializers
    permission_classes = [permissions.IsAuthenticated, CheckOffer]

class OfferListAPIViewSet(generics.ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferListAPISerializers

class OfferEditViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializers

class MyOfferViewSet(generics.ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferMySerializers
    def get_queryset(self):
        return Offer.objects.filter(freelancer=self.request.user)



class ReviewsViewSet(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckRoleReview]

