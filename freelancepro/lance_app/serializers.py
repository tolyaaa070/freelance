from .models import (Skill,UserProfile,SocialLink,
                     Category,Project,Offer,Review)
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                 'role', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class SkillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill_name']
class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name']

class CategoryDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']

class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['last_name','username','role','bio','avatar','skills']

class OtherUserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['last_name','role']

class SocialLinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ['social_links','social_name']
class ProjectListAPISerializers(serializers.ModelSerializer):
    category = CategoriesSerializers()
    class Meta:
        model = Project
        fields = ['id','title','category','client']

class ProjectDetailSerializers(serializers.ModelSerializer):
    skills_required = SkillSerializers(read_only=True, many=True)
    class Meta:
        model = Project
        fields = ['description','title','budget','deadline','status','category','skills_required','created_at','client']

class OfferListAPISerializers(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'project', 'freelancer']
class OfferMySerializers(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['project','freelancer','message','proposed_budget','proposed_deadline','created_at']

class OfferSerializers(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['project','freelancer','message','proposed_budget','proposed_deadline','created_at']

class ReviewsSerializers(serializers.ModelSerializer):
    reviewer_user = OtherUserProfileSerializers(read_only=True)
    target_user = OtherUserProfileSerializers(read_only=True)
    class Meta:
        model =Review
        fields = ['project','reviewer_user','target_user','rating','comment','created_at']