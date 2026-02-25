class ProductivityTracker:
    def __init__(self):
        self.sessions = []
    
    def add_sessions(self,subject, hours):
        self.sessions.append({"subject:",subject})
    
    def view_sessions(self):
        print("\n Study Sessions")
        for session in self.sessions:
            print(f"{session['subject']} - {session['hours']} hours")
    
    def total_hours(self):
        total = sum(session["hours"] for session in self.sessions)
        print(f"\n Total study Hours: {total}")

tracker = ProductivityTracker()
while True:
    print("\n1. Add session")
    print("2. view session")
    print("3. total session")
    print("4. Exit session")

    choice = input("Enter Choice:")

    if choice == "1":
        subject = input("Enter subjects: ")
        hours = float(input("Enter hours studied"))
        tracker.add_sessions(subject, hours)
    elif choice == "2":
        tracker.view_sessions()
    
    elif choice == "3":
        tracker.total_hours()
    
    elif choice == "4":
        break
    else:
        print("Invalid choice1")