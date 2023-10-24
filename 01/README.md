# 01 PJT - 파이썬을 활용한 API 데이터 수집

<br>

## [ 도전 과제 ] 금융 상품 데이터 수집

* **정기 예금 API raw data**

    <img title="" src="file:///C:/Users/v0041/AppData/Roaming/marktext/images/2023-07-22-18-20-59-image.png" alt="" width="425">

                ... (중략)

    <img title="" src="file:///C:/Users/v0041/AppData/Roaming/marktext/images/2023-07-22-18-21-33-image.png" alt="" width="271">

<br>

<br>

### A. 데이터 추출 - Key값 출력하기

- **과제**
  
  > **전체 정기 예금의 응답을 JSON 형태로 변환 후 Key값만 출력하도록 구성하기**
  
  <br>

- **코드**
  
  - import, API 정보, pprint 코드 생략
  
  ```python
  def get_deposit_products():
  
    # 응답을 JSON 형태로 변환 후 Key값만 출력
    result = requests.get(url, params=params).json()
    return result['result'].keys()
  ```

<br>

* **학습 내용**
  
  * `.json` 
    ▷  JSON 응답을 JavaScript 객체 리터럴 혹은 배열로 자동 구문분석하는 메서드
  
  * `.keys()`
    
    ▷ 해당 딕셔너리의 key값만 모아 list화 하여 dict_keys 객체를 반환하는 메서드
    
    <br>

* **실행 결과**
  
  ![](C:\Users\v0041\AppData\Roaming\marktext\images\2023-07-22-19-17-24-image.png)
  
  <br>

* **API 확인**
  
  <img title="" src="file:///C:/Users/v0041/AppData/Roaming/marktext/images/2023-07-22-19-40-28-image.png" alt="" width="163">
  
  <img title="" src="file:///C:/Users/v0041/AppData/Roaming/marktext/images/2023-07-22-19-41-45-image.png" alt="" width="130">
  
  <br>
  
  <br>

### B. 데이터 추출 - 전체 정기 예금 상품 리스트 출력하기

* **과제**
  
  > **응답 중 정기예금 상품 리스트 정보만 출력하도록 구성합니다.**  
  
  <br>

* **코드**
  
  ```python
  def get_deposit_products():
  
    # 정기예금 상품 리스트 정보만 출력
    result = requests.get(url, params=params).json()
    key_result = result['result']
    return key_result['baseList']
  ```

<br>

* **실행 결과**
  
  ![](C:\Users\v0041\AppData\Roaming\marktext\images\2023-07-22-20-26-05-image.png)
  
  <br>

* **API 확인**
  
  <img title="" src="file:///C:/Users/v0041/AppData/Roaming/marktext/images/2023-07-22-20-31-02-image.png" alt="" width="503">
  
  <br>
  
  <br>

### C. 데이터 가공 - 전체 정기예금 옵션 리스트

* **과제**
  
  > **응답 중 정기예금 상품들의 옵션 리스트를 출력하도록 구성한다**
  
  <br>

* **코드**
  
  ```python
  def get_deposit_products():
  
    # 응답 중 key값이 result인 데이터 내에서 key값이 optionList인 데이터를 저
    result = requests.get(url, params=params).json()
    key_result = result['result']
    Option = key_result['optionList']
  
    # 정기예금 상품들의 옵션 리스트를 출력하도록 구성
    want_data_list = []
  
    for i in range(len(Option)):
        want_data = {}
        want_data['금융상품 코드'] = Option[i]['fin_prdt_cd']
        want_data['저축 금리'] = Option[i]['intr_rate']
        want_data['저축 기간'] = Option[i]['save_trm']
        want_data['저축 금리 유형'] = Option[i]['intr_rate_type']
        want_data['저축 금리 유형명'] = Option[i]['intr_rate_type_nm']
        want_data['최고 우대 금리'] = Option[i]['intr_rate2']
  
        want_data_list.append(want_data)
    return want_data_list
  ```

        → Option은 `result['result']['optionList']` 의 value값을 모아둔 
            List이므로 index를 가짐. 

<br>

* **코드 2** - 반복문에서 list의 인덱스를 사용하지 않고 데이터 가공하기
  
  ```python
  def get_deposit_products():
  
    # 응답 중 key값이 result인 데이터 내에서 key값이 optionList인 데이터를 저
    result = requests.get(url, params=params).json()
    key_result = result['result']
    Option = key_result['optionList']
  
    # 정기예금 상품들의 옵션 리스트를 출력하도록 구성
    want_data_list = []
  
    for want in Option :
        want_data = {
            '금융상품 코드' : want['fin_prdt_cd'],
            '저축 금리' : want['intr_rate'],
            '저축 기간' : want['save_trm'],
            '저축 금리 유형' : want['intr_rate_type'],
            '저축 금리 유형명' : want['intr_rate_type_nm'],
            '최고 우대 금리' : want['intr_rate2'],
       }
  
        want_data_list.append(want_data)
  
    return want_data_list
  ```

        → 변수를 인덱스 값이 아닌 List의 요소로 사용하는 것도 가능하므로 `want` 에는
            `Option` 의 요소가 차례로 할당되고 반복한다.

<br>

* **실행 결과**
  
  <img title="" src="file:///C:/Users/v0041/AppData/Roaming/marktext/images/2023-07-22-21-02-15-image.png" alt="" width="534">
  
  <br>
  
  <br>

### D. 데이터 가공 - 새로운 값을 만들어 반환하기

* **과제**
  
  > **상품과 옵션 정보들을 담고 있는 새로운 값을 만들어 Dict 형태로 반환하기**
  
  > **다음의 정보만 추출하여 포함하기**
  > 
  > * 금융 상품
  >   
  >   * 금융 회사명
  >   
  >   * 금융 상품명'
  >   
  >   * 금리 정보 
  >     
  >     : 해당 금융 상품의 금리 정보(옵션) - 여러 개 가질 수 있음
  >     
  >     * 저축금리 유형
  >     
  >     * 저축금리 유형명
  >     
  >     * 저축 기간
  >     
  >     * 저축 금리
  >     
  >     * 최고 우대 금리
  
  <br>

* **코드**
  
  ```python
  def get_deposit_products():
  
      result = requests.get(url, params=params).json()
  
      key_result = result['result']
      Base = key_result['baseList']
      Option = key_result['optinList']
  
      Base_list = []
      base_data = {}
  
      for info_base in Base:
  
          base_data[info_base['fin_prdt_cd']] = {
              '금융회사명' : info_base['kor_co_nm'],
              '금융상품명' : info_base['fin_prdt_nm'],
              '금리정보' : []
          }
  
      for info_option in Option:
  
          option_data = {
              '저축 기간' : info_option['save_trm'],
              '저축 금리' : info_option['intr_rate'],
              '저축 금리 유형' : info_option['intr_rate_type'],
              '저축 금리 유형명' : info_option['intr_rate_type_nm'],
              '최고 우대 금리' : info_option['intr_rate2'],
          }
  
          base_data[info_option['fin_prdt_cd']]['금리정보'].append(option_data)
          Base_list.append(base_data[info_base['fin_prdt_cd']])
  
      return Base_list
  ```

<br>

* **코드 설명**
1. 최종적으로 정리된 금융 상품에 대한 정보들을 모아 담을 list인 `Base_list`를 선언한다.
   
   <br>

2. `Base_list`의 요소가 될 dict `base_data`를 선언한다.
   
   <br>

3. `base_data`는 '금융회사명', '금융상품명', '금리정보'를 출력해야하고, '금리정보'에는 금융 상품 코드가 동일한 상품에 대한 복수의 옵션 정보들이 각각 list의 요소로써 저장되어야 한다.
   
   <br>

4. 따라서 `Base`의 각 요소 dict마다 '금융회사명', '금융상품명', '금리정보'만 추출하여 `base_data`에 담는 것을 반복해야한다.
   
   - `Base`의 각 요소 dict는 반복문 내에서 `info_base`에 할당되므로 `info_base['key 이름']`을 통해 원하는 상품 정보를 추출하여 `base_data`의 value로 할당할 수 있다.
     
     <br>

5. 이 때, 동일한 금융 상품에 대해 다른 금리 정보를 가지는 옵션들을 모아서 `base_data`의 '금리정보'에 할당해주어야 한다.
   
   - 따라서 '금리정보'의 value값은 list로 선언한다.
     
     <br>

6. `base_data` 내에서 금융 상품 정보에 대한 dict를 value값으로 가질 key는 `info_base`의 `fin_prdt_cd`로 설정한다.
   
   - 이는 옵션 정보를 확인하여 `base_data`의 요소 중 해당 옵션의 `fin_prdt_cd`를 key로 가지는 요소에 접근할 수 있도록 한다.
     
     <br>

7. 반복문을 통해 `Option`리스트의 각 요소(`info_option`)에 대해 원하는 정보만을 포함한 `option_data` dict를 선언한다. 동일 상품이지만, 다른 금리를 가지는 상품들의 정보를 가공하여 `option_data` dict에 할당한다.
   
   <br>

8. 만들어진 dict는 `base_data` 중 `fin_prdt_cd`가 동일한 요소의 '금리정보' list로 할당되어야 한다.
   
   따라서 `base_data[info_option['fin_prdt_cd']]['금리정보']`를 통해 접근한 후, `option_data`를 `append()` 메소드를 통해 할당한다.
   
   <br>

9. 최종적으로 정리된 금융정보를 담은 `base_data[info_option['fin_prdt_cd]]`dict들을 하나의 리스트에 모아야 하므로 `Base_list`에 `append()`메소드를 통해 할당한다.
   
   <br>

10. `get_deposit_product()`함수를 통해 얻을 값은 `Base_list`이므로 이를 반환하며 함수를 끝낸다.
    
    <br>
* **어려웠던 점**
  
  * '금리정보'가 같은 금융 상품들을 하나로 모으기 위해서, 금리 정보를 담은 Option list 내의 dict 요소 중 `fin_prdt_list`의 value값을 새로운 리스트 `prdt_list`에 담았음. 이후, 해당 리스트에 `list(set())`을 적용하여 상품들의 코드만 중복 없이 추출함.
  
  * 이후 해당 요소들끼리 반복문을 통해 1:1 비교한 후, `fin_prdt_cd`가 같은 요소만 list화 하려고 했으나, 구현이 쉽지 않았음.
  
  ```python
  def get_deposit_products(): 
  
        result = requests.get(url, params=params).json() 
        key_result = result['result']
        Base = key_result['baseList']
        Option = key_result['optinList'] 
  
        Option_list = []
        product_code = [] 
  
        for i in range(len(Option)):
             option_data = {}
             option_data['저축 금리'] = Option[i]['intr_rate']
             option_data['저축 기간'] = Option[i]['save_trm']
             option_data['저축 금리 유형'] = Option[i]['intr_rate_type']
             option_data['저축 금리 유형명'] = Option[i]['intr_rate_type_nm']
             option_data['최고 우대 금리'] = Option[i]['intr_rate2']
             option_data['금융상품명'] = Option[i]['fin_prdt_cd'] 
  
             Option_list.append(option_data)
             product_code.append(Option[i]['fin_prdt_cd'])
  
    # fin_prdt_cd들을 set()으로 받음 (중복제거를 위해)
  
    # 그리고, Option[i][fin_prdt_cd]를 list(set()) 요소들과 1:1 비교하여(by for)
  
    # 같은 코드를 가진 친구들끼리 list화 해서 base_data['금리정보']에 할당
  
      Pdcd_list = list(set(product_code)) 
  
      for i in range(len(Base)):
           base_data = {}
           base_data['금융회사명'] = Base[i]['kor_co_nm']
           base_data['금융상품명'] = Base[i]['fin_prdt_nm']
  
           # if Option_list
           #   base_data['금리정보'] = Option_list 
  
    # if문을 통해 fin_prdt_cd 동일 여부 판별코드를 작성하던 중 막힘.
  
    # 동일 여부 판별을 위해 처음에는 dict 생성 역시 index를 이용
  
          Base_list.append(base_data) 
  
      return Base_list
      ```
  ```

<br>

* **해결 방안**
  
  * `fin_prdt_cd`가 같은 요소끼리 묶어야하므로 이를 key로 가지는 dict를 생성함.
  
  * value로 금융 상품의 정보를 할당하고, 그 중 '금리정보'의 요소로 동일한 코드를 가지는 옵션들을 할당함.

<br>

<br>

### [ 느낀 점 ]

* `for 반복문`
  
    for문에 대한 이해는 완전하게 됐다고 생각했으나, index를 사용하는 것이 습관이 되어 효율적이지 못한 코드를 짜고 있음을 알게 됨. 이는 문자열이나 list 순회에 대한 이해도가 range 순회에 비해 상대적으로 낮기 때문이라고 생각됨. 따라서 for문을 좀 더 깊게 공부해봐야겠다고 생각함.

* `dictionary 자료형`
  
    수업때부터 dict 자료형이 많이 헷갈렸는데, 특히 이번 문제는 중첩된 dict가 많아 더욱 어렵게 느껴짐. 또한 key를 통해 공통된 자료를 묶을 수 있는 방법을 생각해내기 어려웠음. 결국 반 친구의 힌트를 통해 코딩을 마무리할 수 있었음. dictionary 자료형을 자유자재로 이용할 수 있도록 공부하고 익숙해질 때까지 연습해야겠다고 생각함. 
