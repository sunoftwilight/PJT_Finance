from locust import HttpUser, task, between

class SampleUser(HttpUser):
    # wait_time = 1~3초마다 작업을 하게 될 것
    wait_time = between(1, 3)

    def on_start(self):
        # 유저가 생길 때마다 print 찍기
        print('test start')

    # 유저 생성 + 1~3초마다 아래 요청을 서버로 보낸다
    @task
    def normal_sort(self):
        # 아래 주소가 앞에 붙어서 실행됨
        # http://localhost:8000/
        # 이 주소로 get 요청을 보내는 것
        self.client.get("test/normal_sort/")

    # @task
    # def priority_queue(self):
    #     self.client.get("test/priority_queue/")

    # @task
    # def bubble_sort(self):
    #     self.client.get("test/bubble_sort/")


