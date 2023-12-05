class Customer:
    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name

    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    # Class variable to store all customer instances
    all_customers = []

    def save(self):
        # Save the current instance to the class variable
        Customer.all_customers.append(self)

    def restaurants(self):
        return list({review.restaurant for review in self.reviews})

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)  

    @classmethod
    def all(cls):
        # Return all customer instances
        return cls.all_customers

    def num_reviews(self):
        return len(self.reviews)  

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name().lower() == name.lower():
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.all_customers if customer.given_name.lower() == name.lower()]

# Rest of the Review class and other code

# Create customer instances
customer1 = Customer("Felix", "Ndirangu")
customer2 = Customer("John", "Adams")

# Change names
customer1._given_name = "Lennox"
customer2._family_name = "Warugu"

# Save customer instances
customer1.save()
customer2.save()

# Retrieve all customer instances
all_customers = Customer.all()

# Display information
for customer in all_customers:
    print(customer.full_name())
