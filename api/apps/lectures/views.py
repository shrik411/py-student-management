from rest_framework import serializers, viewsets
from .models import Lecture

# Create your views here.

class LectureSerializer(serializers.serializer):
    class Meta:
        model = Lecture
        fields = ('id', 'title', 'description',
                  'lecturer_name', 'date', 'duration',
                  'slides_url', 'level', 'required')


class LeactureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer