## Project Overview
![](https://lh4.googleusercontent.com/gcISeGs08PS0Eh3TG4K_nye0fFzX0bSyIf7Oe8IJLpZr5B4FXrd4S_OH8lmXISs7tnQVVOynYx_jNm0LVFuEhcmkeYFU3KRRD1n1SeWDxgOkhD4zhnOhPVzmHS7DKwnLfmqv7t4VUYIKuskX)
This code simulates an online second-price ad auction involving users and bidders. Here's a summary of what it does:
1.  **User Class:** This class represents a user with a secret probability of clicking on an ad. Upon initialization, the probability is generated uniformly between 0 and 1.
2.	**Bidder Class:** Each class represents a bidder in the auction. Each bidder has an initial balance and can place bids on users. Bidders adjust their bidding strategy based on the outcome of previous auctions.
3.	**Auction Class:** Manages the auction process. It initializes with lists of users and bidders. It executes rounds of the auction, during which:
      - A random user is selected.
      - Bidders place bids on the selected user.
      - The winning bid and the second-highest bid are determined.
      - Bidders are notified of the auction outcome and update their balances accordingly.
      - Bidders with balances below a certain threshold are disqualified from future rounds.
      - The balance history of each bidder is recorded.
4.	**Plotting Function:** Provides a visual representation of each bidder's balance history during the auction.

Overall, this code simulates an auction environment where bidders compete to display ads to users, with their bidding strategies evolving based on feedback from previous auctions.
