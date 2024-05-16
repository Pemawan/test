from queue import LifoQueue
backward_history=LifoQueue()
forward_history=LifoQueue()
current_page=None
#Visit Function
NoOfVisists= int(input("Enter the number of url history: "))
print("Enter URLs to visit:")
for i in range(NoOfVisists): 
    url= input("UAL:")
    print("Visiting {url}")
    backward_history.put(current_page)
    current_page =url
#Display current page
print("Current page: (current page)") 
#G0 back
while input("Do you want to go back? (yes/no): ").lower()=='yes':
     if not backward_history.empty():
        forward_history.put(current_page)
        current_page=backward_history.get()
        print(f"Going back to {current_page}")
else:
     print("No previous page available")
#G0 forward
while input("Do you want to go forward? (yes/no): ").lower()=='yes':
     if not forward_history.empty():
        forward_history.put(current_page)
        current_page=backward_history.get()
        print(f"Going forward to {current_page}")
else:
    print("No forward page available")
