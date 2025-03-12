# train-by-book is a NLP project using pipeline from transfers to train the model using a pdf. In this case a randomly generate story is being trained. Qustions can asked to the model and 80% of accuracy can be expected. 

# dependencies
pip install pdfplumber transformers accelerate datasets torch sentencepiece


# Sample questions to ask the model for wonderland-story:
Here are 10 questions and answers based on the story:
Q1: What did Alice and Jack find in the attic of Alice's family home?
A1: An old, mysterious-looking door.
Q2: Where did the door lead them?
A2: To a long, dark corridor that descended deep into the earth.
Q3: What did they find at the end of the corridor?
A3: A beautiful garden filled with towering flowers and sparkling fountains.
Q4: Who welcomed them to Wonderland?
A4: The Cheshire Cat.
Q5: What event did they attend in Wonderland?
A5: The mad tea party.
Q6: Who were the hosts of the tea party?
A6: The March Hare and the Hatter.
Q7: What realization did Jack come to during the tea party?
A7: He was falling in love with Alice.
Q8: How did Alice feel about Jack?
A8: She had feelings for him too.
Q9: What happened as the night wore on?
A9: Alice and Jack found themselves lost in each other's eyes.
Q10: What did Alice and Jack share as they left Wonderland?
A10: Their first kiss.

# to run python3 train_by_book.py