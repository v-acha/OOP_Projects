'''Class to manages bidding strategy''' 
class Bidder:
    '''Class to represent a bidder in an online second-price ad auction''' 

    def __init__(self, num_users, num_rounds):
        """
        Initializes a new Bidder instance.

        :param num_users: Number of user objects in the game
        :param num_rounds: Total number of rounds to be played
        """
        self.num_users = num_users
        self.num_rounds = num_rounds
        self.balance = 0.0  # Initial balance
        self.bid_history = []
        self.current_round = 0

    def __repr__(self):
        '''Return a Bidder object with balance.'''
        return f'Bidder(balance={self.balance})'

    def __str__(self):
        '''Return a Bidder object with balance.'''
        return f'Bidder with balance: {self.balance}'

    def bid(self, user_id):
        """
        Places a bid for a user based on the user_id.

        :param user_id: The ID of the user to place a bid for
        :return: A non-negative amount of money, rounded to three decimal places
        """
         # Increase the bid amount as the auction progresses, encouraging a more aggressive approach
        # in the later stages of the game when more is known about the clicking behavior.
        bid_increment = 0.05  # Increment the bid slightly each round
        max_bid = 0.2  # Maximum bid limit
        # Simple strategy: bid a fixed increment more each round, not exceeding max_bid
        bid_amount = min(0.05 + (self.current_round * bid_increment), max_bid)
        # Update the current round for the next bid
        self.current_round += 1
        return round(bid_amount, 3)

    def notify(self, auction_winner, price, clicked):
        ''' Receives notification about the auction outcome.
            Actual balance updates are handled in the Auction class.
            :param auction_winner: A boolean indicating whether this bidder won the auction.
            :param price: The price of the second-highest bid, which the winner pays.
            :param clicked: if user clicked on bidder ad returns True or false.'''
         # Adjust virtual balance based on auction outcomes to inform future bids
        # Increment balance by 1 if the ad was clicked, reflecting successful ad placement
        if auction_winner:
            self.balance -= price # Deduct the price from the balance if this bidder won
            if clicked:
                self.balance += 1  # Increasing the balance if the ad was clicked