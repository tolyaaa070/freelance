from .views import (OthersProfileViewSet,EditMyProfileViewSet,MyProfileViewSet,SkillViewSet,
                    ProjectListAPIViewSet,ProjectEditViewSet,ProjectCreateViewSet,CustomLoginView,LogoutView,
                    OfferEditViewSet,OfferCreateViewSet,OfferListAPIViewSet,MyOfferViewSet,ReviewsViewSet,ProjectDetailViewSet,MyProjectView,CategoriesViewSet,CategoryDetailViewSet,SocialLinkViewSet,RegisterView)
from rest_framework import routers
from django.urls import path,include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


router = routers.SimpleRouter()
router.register(r'sociallink', SocialLinkViewSet, basename='sociallink')

urlpatterns=[
    path('', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/me', MyProfileViewSet.as_view(), name='my_profile'),
    path('user/<int:pk>/', OthersProfileViewSet.as_view(), name='users'),
    path('user/edit', EditMyProfileViewSet.as_view(), name='edit'),
    path('project/', ProjectListAPIViewSet.as_view(), name='project'),
    path('project/<int:pk>/', ProjectDetailViewSet.as_view(), name='project_detail'),
    path('project/<int:pk>/edit', ProjectEditViewSet.as_view(), name='project_edit'),
    path('project/create', ProjectCreateViewSet.as_view(), name='project_create'),
    path('project/my/', MyProjectView.as_view(), name='my_project'),
    path('skills/', SkillViewSet.as_view(), name='skills'),
    path('categories/', CategoriesViewSet.as_view(), name = 'categories'),
    path('category/<int:pk>/', CategoryDetailViewSet.as_view(), name='category_det'),
    path('offer/', OfferListAPIViewSet.as_view(), name='offer'),
    path('offer/<int:pk>/edit/', OfferEditViewSet.as_view(), name='offer_edit'),
    path('offer/my', MyOfferViewSet.as_view(), name='my_offer'),
    path('offer/create', OfferCreateViewSet.as_view(), name='offer_create'),
    path('reviews/', ReviewsViewSet.as_view(), name='reviews'),
]