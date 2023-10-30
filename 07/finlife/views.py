from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.db.models import Max
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .serializers import DepositOptionsSerializer, DepositProductsSerializer
from .models import DepositOptions, DepositProducts

# Create your views here.
@api_view(['GET'])
def save_deposit_products(request):
    API_KEY = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'

    response = requests.get(url).json()

    products_lst = response.get('result').get('baseList')

    for prdt in products_lst:
        prdt_data = {
            'fin_prdt_cd': prdt.get('fin_prdt_cd'),
            'kor_co_nm': prdt.get('kor_co_nm'),
            'fin_prdt_nm': prdt.get('fin_prdt_nm'),
            'etc_note': prdt.get('etc_note'),
            'join_deny': prdt.get('join_deny'),
            'join_member': prdt.get('join_member'),
            'join_way': prdt.get('join_way'),
            'spcl_cnd': prdt.get('spcl_cnd'),
        }

        serializer = DepositProductsSerializer(data=prdt_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    options_lst = response.get('result').get('optionList')

    for optn in options_lst:
        optn_data = {
            'fin_prdt_cd': optn.get('fin_prdt_cd'),
            'intr_rate_type_nm': optn.get('intr_rate_type_nm'),
            'intr_rate': optn.get('intr_rate') if optn.get('intr_rate') else -1 ,
            'intr_rate2': optn.get('intr_rate2') if optn.get('intr_rate2') else -1,
            'save_trm': optn.get('save_trm'),
        }

        serializer = DepositOptionsSerializer(data=optn_data)
        if serializer.is_valid(raise_exception=True):
            prdt = DepositProducts.objects.get(fin_prdt_cd=optn.get('fin_prdt_cd'))
            serializer.save(product=prdt)

    return JsonResponse({'message': 'okay'})


@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response({'message': '이미 있는 데이터이거나, 잘못 입력되었습니다.'})


@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    # DepositProduct 테이블의 데이터 중 fin_prdt_cd(=field name)가 fin_prdt_cd(=variable routing)인 데이터 조회
    product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    # 위에서 조회한 상품에 대한 모든 옵션 조회 
    options = product.depositoptions_set.all()
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def top_rate(request):
    # DepositOptions 테이블에서 intr_rate2가 max인 데이터를 찾고, 그 중에서 최대 금리의 값만 가져오는 것
    max_rate = DepositOptions.objects.aggregate(intr_rate2=Max('intr_rate')).get('intr_rate2')
    # intr_rate2가 최대 금리의 값인 옵션의 데이터 얻기
    max_option = DepositOptions.objects.get(intr_rate2=max_rate)
    # 최대 금리 옵션의 외래키를 참조하여 최대 금리 옵션을 가지는 상품 조회 (by serializer)
    serializer_prdt = DepositProductsSerializer(max_option.product)

    # 최대 금리 옵션을 가지는 상품에 대한 모든 옵션 정보를 조회 (by 역참조) 
    options = max_option.product.depositoptions_set.all()
    serializer_optn = DepositOptionsSerializer(options, many=True)

    info = {
        'top_rate_product': serializer_prdt.data,
        'options': serializer_optn.data,
    }
    
    return Response(info)
    # intr_rate2
