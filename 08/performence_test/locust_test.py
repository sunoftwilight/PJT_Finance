from locust import HttpUser, task, between

class SampleUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        print('test start')

    @task
    def chk_algorithm(self):
        self.client.get("test/algorithm/")

    @task
    def jiwhan(self):
        self.client.get("test/jiwhan/")

    @task
    def inwha(self):
        self.client.get("test/inwha/")

    # @task
    # def normal_sort(self):
    #     self.client.get("test/normal_sort/")

    # @task
    # def priority_queue(self):
    #     self.client.get("test/priority_queue/")

    # @task
    # def bubble_sort(self):
    #     self.client.get("test/bubble_sort/")


