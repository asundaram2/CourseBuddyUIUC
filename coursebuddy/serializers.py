from rest_framework import serializers
from .models import *

class ProfessorUserRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfessorRatingsFromUser
        fields = "__all__"

class ProfessorWebsiteRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfessorRatingsFromWebsites
        fields = "__all__"

class RMPSerializer(serializers.Serializer):
    professor = serializers.CharField(max_length=45)
    professor_ratings = serializers.FloatField(required=False)

class StudyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Studygroup
        fields = "__all__"

class RegistrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registrations
        fields = "__all__"

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=45)
    major = serializers.CharField(max_length=45)
    email = serializers.CharField(max_length=45)
    year = serializers.CharField(max_length=45)
    crn = serializers.IntegerField()
    subject = serializers.CharField(max_length=45, required=False)
    course = serializers.IntegerField(required=False)


class TestSerializer(serializers.ModelSerializer):
    crn = serializers.IntegerField()  # Field name made lowercase.
    professor = serializers.CharField()  # Field name made lowercase.
    averagegpa = serializers.FloatField()  # Field name made lowercase.
    professor_ratings = serializers.FloatField()  # Field name made lowercase.
    difficulty = serializers.FloatField()

    class Meta:
        model = Test
        fields = "__all__"

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields = "__all__"

class Spring19GradesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sp19
        fields = "__all__"
