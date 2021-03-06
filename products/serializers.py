from rest_framework import serializers
from products.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    categorized_in = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "categorized_in",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )

    def get_categorized_in(self, obj):
        return obj.category.name


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products"
        )
