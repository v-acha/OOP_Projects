
## Project Overview:
![](https://cdn.pixabay.com/photo/2024/01/18/10/37/letter-tiles-8516698_1280.jpg)

The provided code consists of three functions related to Scrabble gameplay. The `score_word` function calculates the Scrabble score for a given word, considering wildcard characters. It iterates through each letter in the word, calculates its score based on a predefined scoring dictionary, and adjusts the score by subtracting the scores of wildcard characters if present. The `load_valid_words` function loads valid words from a specified file and stores them in a set. Finally, the `run_scrabble` function takes a Scrabble rack as input, generates valid English words that can be constructed from the rack, calculates their scores, and sorts them by score and then alphabetically. It also performs error validation for the input rack and returns the list of valid words and the total number of valid words.
