from locust import HttpUser, TaskSet, task, between


class BrowseCatalog(TaskSet):
    @task(3)
    def get_product(self):
        self.client.get("/product/123")

    @task(2)
    def get_category(self):
        self.client.get("/category/456")


class BrowseBucket(TaskSet):
    @task
    def get_product(self):
        self.client.get("/bucket")


class ShopUser(HttpUser):
    host = "https://api.example.com"

    tasks = {
        BrowseCatalog: 3,
        BrowseBucket: 7
    }

    wait_time = between(1, 3)
