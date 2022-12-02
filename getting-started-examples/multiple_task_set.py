from locust import User, between, task, SequentialTaskSet, TaskSet

class SearchProduct(SequentialTaskSet):
    @task
    def search_adult_products(self):
        print("Searching for adult products")
        
    def search_kids_products(self):
        print("Searching for kids products")
        

class ViewCart(SequentialTaskSet):
    @task
    def get_cart_items(self):
        print("Get all cart items")
        
    def search_cart_item(self):
        print("Searching items in cart")
        
        
class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct, ViewCart]
    