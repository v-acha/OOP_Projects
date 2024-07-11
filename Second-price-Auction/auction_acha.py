"""Module to randomize secret probability"""
import random
#import matplotlib.pyplot as plt

class User:
    '''Class to represent a user with a secret probability of clicking an ad.'''

    def __init__(self):
        '''Generating a probability between 0 and 1 from a uniform distribution'''
        self.__probability = random.uniform(0, 1)  # Secret probability of clicking an ad

    def __repr__(self):
        '''User object with secret probability'''
        return f'User(probability={self.__probability:.2f})'

    def __str__(self):
        '''Return User object with a secret likelihood of clicking on an ad'''  
        return f'User object with secret likelihood of clicking on an ad: {self.__probability:.2%}'

    def show_ad(self):
        '''Returns True to represent the user clicking on an ad or False otherwise'''
        return random.random() <= self.__probability


# Class representing the Auction
class Auction:
    """ Class to represent an online second-price ad auction """

    def __init__(self, users, bidders):
        """
        Initializes the Auction with lists of User and Bidder objects.

        :param users: A list of User objects participating in the auction.
        :param bidders: A list of Bidder objects participating in the auction.
        :self.balances: dictionary to store balances for each bidder in the auction
        """
        self.users = users
        self.bidders = bidders
        self.balances = {bidder: 0 for bidder in bidders}

    def __repr__(self):
        '''Return auction object with users and qualified bidders'''
        return f'Auction(users={len(self.users)}, qualified_bidders={len(self.bidders)})'

    def __str__(self):
        '''Return auction object with users and qualified bidders'''
        return f'Auction with {len(self.users)} users and {len(self.bidders)} qualified bidders'

    def execute_round(self):
        """ Executes a single round of the auction."""
        #Step 1: Randomly select a user
        user = random.choice(self.users)
        user_id = self.users.index(user)

        #Step 2: Generate bids for the selected user from each bidder
        bids = {bidder: bidder.bid(user_id) for bidder in self.bidders}
        if not bids:
            return  # Exit if no bids were made

        #Step 3&4: Determine the winning bid and second highest bidder
        # Determine the winning bid and the second-highest bid
        sorted_bids = sorted(bids.items(), key=lambda x: x[1], reverse=True)
        winner, winning_bid = sorted_bids[0]
        second_highest_bid = sorted_bids[1][1] if len(sorted_bids) > 1 else winning_bid

        #Step 5: Determine if the user clicked on the ad
        clicked = user.show_ad()

        #Step 6 & 7: Notify bidders about the auction results and update balances
        for bidder in self.bidders:
            auction_winner = bidder == winner
            # Deduct the second-highest bid from the winning bidder's balance
            if auction_winner:
                self.balances[bidder] -= second_highest_bid
                if auction_winner and clicked:
                    # Increment the winner's balance if the ad was clicked
                    self.balances[bidder] += 1
            bidder.notify(auction_winner, second_highest_bid, clicked if auction_winner else None)

            # Check if any bidder's balance falls below -1000
            # check and remove disqualified bidders.
            if self.balances[bidder] < -1000:
                self.bidders.remove(bidder)
                print(f"{bidder} balance below -1000. Balance:{self.balances[bidder]:.2f}")


    '''def plot_history(self):
        #Creates a visual representation of how the auction has proceeded.
        plt.figure(figsize=(10, 6)) 
        # Each bidder's balance history will be a separate line in the plot
        for bidder in self.bidders:
            plt.plot(self.balances[bidder], label=str(bidder))

        # Set the title and labels for the plot
        plt.title('Auction Balance History')
        plt.xlabel('Round')
        plt.ylabel('Balance')
        plt.legend()  # Show legend with bidder labels
        plt.grid(True)  # Add a grid for easier readability
        plt.show()  # Display the plot'''