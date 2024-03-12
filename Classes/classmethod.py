class User:
    users_registry = []  # Class variable to hold the registry of users

    def __init__(self, name, email):
        self.name = name
        self.email = email
        # Directly add the newly created user instance to the registry
        User.register_user(self)

    @classmethod
    def register_user(cls, user_instance):
        """Class method to add a user to the registry."""
        cls.users_registry.append(user_instance)

    @classmethod
    def display_registered_users(cls):
        """Class method to print out all registered users."""
        print("Registered Users:")
        for user in cls.users_registry:
            print(f"Name: {user.name}, Email: {user.email}")

# Creating user instances
user1 = User("Alice", "alice@example.com")
user2 = User("Bob", "bob@example.com")
user3 = User("wali", "wali@example.com")
user4 = User("azam", "azam@example.com")

# Displaying all registered users using a class method
User.display_registered_users()
class CurrencyConverter:
    @staticmethod
    def convert(amount, from_currency, to_currency):
        conversion_rates = {
            ('USD', 'EUR'): 0.93,
            ('EUR', 'USD'): 1.07,
            ('USD', 'GBP'): 0.82,
            ('GBP', 'USD'): 1.22,
            # Add more conversion rates as needed
        }

        # Construct the key for the conversion rates dictionary
        conversion_key = (from_currency, to_currency)

        # Check if the conversion rate exists
        if conversion_key in conversion_rates:
            return amount * conversion_rates[conversion_key]
        else:
            raise ValueError("Conversion rate not found.")

