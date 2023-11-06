from django.http import JsonResponse
from rest_framework.decorators import api_view
# from locust import HttpUser, task, between
import random
# import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

array_length = 1000
random_range = 5000

csv_path = 'data/test_data.csv'

def csv_to_DF(request):
    # csv파일 로딩
    df = pd.read_csv(csv_path, encoding='cp949', usecols=['이름', '나이'])
    data = df.to_dict('records')
    
    return JsonResponse({ 'data': data })


def missing_value(request):
    df = pd.read_csv(csv_path, encoding='cp949', usecols=['이름', '나이'])
    # dataframe의 '나이'열이 빈 값인 곳은 문자열 'null'로 채워준다.
    df['나이'].fillna('null', inplace=True)
    data = df.to_dict('records')
    
    return JsonResponse({ 'data': data })


def algorithm(request):
    df = pd.read_csv(csv_path, encoding='cp949', usecols=['이름', '나이'])

    # dataframe의 '나이' 열의 값에 대한 평균값을 계산하여 avg_older 변수에 할당
    avg_older = df['나이'].mean()
    
    # dataframe에 '평균 나이와의 차' 열 추가 및 해당 열의 값 0으로 초기화
    df['평균 나이와의 차'] = 0

    # dataframe의 각 행에 대해 index와 row 전체를 받아오며 순회
    for idx, row in df.iterrows():
        # 탐색중인 행의 '나이' 열의 값을 this_older 변수에 할당
        this_older = row['나이']
        # '평균 나이와의 차' 열의 idx 행의 값으로 avg_older와 this_order의 절댓값을 할당
        df['평균 나이와의 차'][idx] = abs(avg_older - this_older)

    # '평균 나이와의 차' 열을 기준으로 dataframe을 오름차순 정렬한 뒤, 0~9번째 행까지만 받기
    sort_df = df.sort_values(by=['평균 나이와의 차']).iloc[:10]
    
    data = sort_df.to_dict('records')
    
    return JsonResponse({ 'data': data })


def jiwhan(request):
    df = pd.read_csv(csv_path, encoding='cp949', usecols=['이름', '나이'])

    age_avg = df['나이'].mean()
    new_col = []
    for age in df['나이']:
        new_col.append(abs(age - age_avg))
    df['나이편차'] = new_col
# 여기서 쓰입니다
    tgdf = df.sort_values(by=['나이편차']).head(10)
    data = tgdf.to_dict('records')
    return JsonResponse({'test': data})


def inwha(request):
    arr = np.loadtxt('data/test_data.CSV', delimiter=",", encoding='cp949', dtype=str)    
    columns = arr[0]
    arr = np.delete(arr, 0, 0)
    # arr[0]을 컬럼명으로 지정하고 arr의 0행 삭제
    df = pd.DataFrame(arr, columns=columns)
    # replace() 이용하여 결측치를 'NULL'이라는 문자열로 치환
    df_NULL = df.replace('', 'NULL')
    # 나이에 결측치가 없는 행만 모으기
    df_c = df_NULL.loc[df_NULL['나이'] != 'NULL']
    # 나이 자료형을 int로 변경
    df_c = df_c.astype({'나이':'int'})
    # 나이의 평균값 구하기
    mean_v = df_c['나이'].mean()
    # 평균과의 차이 열 diff 추가
    df_c['diff'] = abs(df_c['나이'] - mean_v)
    # diff를 기준으로 오름차순으로 정렬
    df_c = df_c.sort_values(by=['diff'])
    # 상단 10개의 행만 선택
    df_c = df_c.head(10)
    
    data = df_c.to_dict('records')
    return JsonResponse( {'dat': data} )

@api_view(['GET'])
def bubble_sort(request):
    df = pd.read_csv(csv_path, encoding='cp949')
    data = df.to_dict('records')
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0],
      'data': data,
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    df = pd.read_csv(csv_path)
    data = df.to_dict('records')

    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0],
        'data': data,
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    df = pd.read_csv(csv_path)
    data = df.to_dict('records')

    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get(),
        'data': data,
    }
    return JsonResponse(context)
