from rest_framework import serializers
from app1.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
		model=Snippet
		fields='id','name','address','dob',

