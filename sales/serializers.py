from rest_framework import serializers
from sales.models import ProductCategory
from sales.models import Product
from sales.models import Receipt
from sales.models import Sales

class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
	products = serializers.HyperlinkedRelatedField(
		many=True,
		read_only=True,
		view_name='product-detail')

	class Meta:
		model = ProductCategory
		fields = fields = (
		'url',
		'pk',
		'name',
		'products')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
	product_category = serializers.SlugRelatedField(queryset = ProductCategory.objects.all(), slug_field='name')

	class Meta:
		model = Product
		fields = fields = (
		'url',
		'name',
		'product_category',
		'production_date',
		'price')

class ReceiptSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Receipt
		fields = fields = (
		'url',
		'pk',
		'no_resi',
		'receipt_date',
		'total')

class SalesSerializer(serializers.ModelSerializer):
	product = serializers.SlugRelatedField(queryset = Product.objects.all(), slug_field='name')
	receipt = serializers.SlugRelatedField(queryset = Receipt.objects.all(), slug_field='no_resi')

	class Meta:
		model = Sales
		fields = fields = (
		'url',
		'pk',
		'quantity',
		'sub_total',
		'product',
		'receipt'
		)