from locust import User, between, task, SequentialTaskSet, TaskSet, HttpUser, events


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
        with self.client.get("/>", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get all cart items, StatusCode: " + str(response.status_code))
            else:
                if "Why Us?" in response.text:
                    response.success()
                else:
                    response.failure("Could not verirfy that this is the correct page" + response.text)
                
    @task
    def exit_navigation(self):
        self.interrupt()
    
    @task    
    def search_cart_item(self):
        print("Searching items in cart")
        
    @task
    def exit_task_execution(self): # duplicated code from line 12
        self.interrupt()
        
        
class MyUser(HttpUser):
    wait_time = between(1, 2)
    tasks = [ViewCart]        
   
    
    # def on_start(self):
    #     print("MyUser : Hatching New User ..")
        
    # def on_stop(self):
    #     print("MyUser : Destroying User ..")
        