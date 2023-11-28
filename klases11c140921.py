class Subscription:
    def __init__(self, p):
        self.price = p

    def monthly(self, month_count):
        return self.price * month_count

spotify = Subscription(6.99)
print(spotify.monthly(13))

netflix = Subscription(11.99)
print(netflix.monthly(12))