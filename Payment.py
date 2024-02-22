class PaymentGateway:
    def __init__(self):
        self.users = {'user1': 1000, 'user2': 500, 'user3': 200}

    def check_balance(self, user):
        return self.users.get(user, 0)

    def process_payment(self, user, amount):
        if user in self.users and self.users[user] >= amount:
            self.users[user] -= amount
            return True
        return False

if __name__ == "__main__":
    gateway = PaymentGateway()

    while True:
        print("\nPayment Gateway Menu:\n1. Check Balance\n2. Make Payment\n3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            user = input("Enter your username: ")
            print(f"Your balance: ${gateway.check_balance(user)}")

        elif choice == '2':
            user = input("Enter your username: ")
            amount = float(input("Enter the payment amount: $")) #code by Anshuman
            print("Payment successful!" if gateway.process_payment(user, amount) else "Payment failed Insufficient balance or invalid user.")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please select a valid option.")
