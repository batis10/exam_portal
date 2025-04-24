from rest_framework import serializers
from .models import Question, Option, QuestionTag, QuestionTagMap

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'question', 'option_text', 'is_correct']


class QuestionTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionTag
        fields = ['id', 'name']


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, source='option_set', read_only=True)
    tags = serializers.SerializerMethodField()

class QuestionTagMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionTagMap
        fields = '__all__'  # or specify the fields you need    

    class Meta:
        model = Question
        fields = [
            'id', 'exam', 'question_text', 'question_type',
            'difficulty', 'media_url', 'marks', 'options', 'tags'
        ]

    def get_tags(self, obj):
        return [tag_map.tag.name for tag_map in obj.questiontagmap_set.select_related('tag')]
