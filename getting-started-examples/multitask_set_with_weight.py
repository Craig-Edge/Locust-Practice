from locust import User, between, task, SequentialTaskSet, TaskSet


@events.test_start.add_listener
def on_test_start(**kwargs):
    print("............ Initiating Load Test ......... ON_TEST_START")
    
    
@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print("........ Load Test Completed .......... ON_TEST_END")
    

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
    tasks = {
        SearchProduct: 4, 
        ViewCart: 1
    }    