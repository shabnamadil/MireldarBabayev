from rest_framework import serializers
from ..models import Blog, Category, Comment, Tag


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class CommentListSerializer(serializers.ModelSerializer):
    author_full_name = serializers.SerializerMethodField()
    author_photo = serializers.SerializerMethodField()
    is_author = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'author_full_name', 'author_photo', 'is_author', 'created_date')

    def get_author_full_name(self, obj):
        return obj.author.get_full_name() if obj.author and obj.author.get_full_name() else 'Admin User'
    
    def get_author_photo(self, obj):
        return obj.author.image.url if obj.author and obj.author.image else '/static/images/user.png'
    
    def get_is_author(self, obj):
        request = self.context.get('request', None)
        return request.user == obj.author if request else False


class CommentPostSerializer(serializers.ModelSerializer):
    author_full_name = serializers.SerializerMethodField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    created_date = serializers.ReadOnlyField()
    author_photo = serializers.SerializerMethodField()
    is_author = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'content',
            'author',
            'author_full_name',
            'blog',
            'created_date',
            'author_photo', 'is_author',
        )

    def validate(self, attrs):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            raise serializers.ValidationError('You have to log in')
        attrs['author'] = request.user
        return attrs

    def get_author_full_name(self, obj):
        return obj.author.get_full_name() if obj.author.get_full_name() else 'Admin User'
    
    def get_author_photo(self, obj):
        return obj.author.image.url if obj.author and obj.author.image else '/static/images/user.png'
    
    def get_is_author(self, obj):
        request = self.context.get('request', None)
        return request.user == obj.author if request else False

    

class CommentUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'content'
        )



class BlogListSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    tag = serializers.SerializerMethodField()
    author = serializers.CharField(source='author.get_full_name', default='Admin User')
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    comments = CommentListSerializer(many=True, read_only=True)
    has_next = serializers.BooleanField(default=True)

    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'short_description',
            'content',
            'image',
            'category',
            'tag',
            'author',
            'comment_count',
            'view_count',
            'slug',
            'comments',
            'published_date',
            'has_next'
        )

    def get_category(self, obj):
        return [category.name for category in obj.category.all()]
    
    def get_tag(self, obj):
        return [tag.name for tag in obj.tag.all()]
    
    def get_has_next(self, obj):
        return True
