from django.shortcuts import render

# Create your views here.

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'is_student')
        extra_kwargs = { 'password': {'write_only': True, 'min_length': 8} }

    def create(self, validated_data):
        is_student = validated_data.pop('is_student')
        user = get_user_model().objects.create_user(**validated_data)
        user.is_student = is_student
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
                queryset=get_user_model().objects.all())

    class Meta:
        model = UserProfile
        fields = ('__all__')


class CreateUserSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
                queryset=get_user_model().objects.all())

    class Meta:
        model = UserProfile
        fields = ('__all__')
