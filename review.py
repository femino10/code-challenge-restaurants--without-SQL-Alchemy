class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        restaurant.reviews.append(self)
        customer.reviews.append(self)
        Review.all_reviews.append(self)

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    def rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews