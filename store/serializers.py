from rest_framework import serializers
from store.models import Filter, Filter_option, Review
from users.models import User, Order
from ImageStorage.models import Image


class FilterSerializer(serializers.ModelSerializer): #Filter모델 시리얼라이즈
    class Meta:
        model = Filter
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer): #구매옵션설정페이지 댓글부분 시리얼라이즈
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Review
        fields = ('review_image','content','user', 'updated_at', 'created_at')


class ReviewCreateSerializer(serializers.ModelSerializer): #구매옵션설정페이지 리뷰생성 시리얼라이즈
    class Meta:
        model = Review
        fields = ("content",)

class OrderCreateSerializer(serializers.ModelSerializer): #구매페이지 order생성 시리얼라이즈
    class Meta:
        model = Order
        fields = "__all__"


class ImageStorageSerializer(serializers.ModelSerializer): #인풋인미지와 아웃풋이미지 담는 시리얼라이즈
    input_img = serializers.FileField(required=False)
    class Meta:
        model = Image
        fields = ("pk", "input_img", "output_img")

class FilterOptionPriceSerializer(serializers.ModelSerializer): #filter_option에서 price만 가져오는 시리얼라이즈
    filter_set = FilterSerializer(many=True)
    class Meta:
        model = Filter_option
        fields = ("price",)

class FilterOptionSerializer(serializers.ModelSerializer): # filter_option에 대한 시리얼라이저
     class Meta:
        model = Filter_option
        fields = "__all__"

class OptionReviewSerializer(serializers.ModelSerializer): # 구매옵션설정페이지 옵션+리뷰 데이터 시리얼라이즈
    review_set = ReviewSerializer(many=True)
    filter_option_set = FilterOptionSerializer(many=True)
    class Meta:
        model = Filter
        fields = "__all__"

class FilterDetailUserSerializer(serializers.ModelSerializer):  #구매페이지에 user정보 넘기기 위한 시리얼라이즈
    class Meta:
        model = User
        fields = "__all__"

class FilterDetailImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("output_img",)

class FilterDetailPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter_option
        fields = "__all__"
class FilterDetailPageGetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)
        
class FilterDetailPageSerializer(serializers.ModelSerializer):
    # user = FilterDetailPageGetUserSerializer(many=True)
    # image = FilterDetailImageSerializer(many=True)
    # filter_option = FilterDetailPriceSerializer(many=True)
    # filter = FilterSerializer(many=True)
    class Meta:
        model = Order
        fields = ("id", )
        
class ReviewAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"



class FilterDetailPageGetSerializer(serializers.ModelSerializer):
    filter_user = FilterDetailUserSerializer(many=True)
    review_set = ReviewAllSerializer(many=True)
    image_set = FilterDetailImageSerializer(many=True)
    filter_option_set = FilterDetailPriceSerializer(many=True)
    class Meta:
        model = Filter
        fields = "__all__"