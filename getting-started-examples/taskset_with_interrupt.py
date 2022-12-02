from locust import User, between, task, SequentialTaskSet, TaskSet

class SearchProduct(SequentialTaskSet):
    @task
    def search_adult_products(self):
        print("Searching for adult products")
    
    @task    
    def search_kids_products(self):
        print("Searching for kids products")
    
    @task
    def exit_task_execution(self):
        self.interrupt()

class ViewCart(SequentialTaskSet):
    @task
    def get_cart_items(self):
        print("Get all cart items")
    
    @task    
    def search_cart_item(self):
        print("Searching items in cart")
        
    @task
    def exit_task_execution(self): # duplicated code from line 12
        self.interrupt()
        
        
class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct, ViewCart]
    