# AI Assistant for 2nd Edition AD&D

This project aims to create an AI Assistant specializing in 2nd Edition Advanced Dungeons & Dragons. The assistant will be trained on core rulebooks and other relevant materials to provide accurate and helpful information to players and Dungeon Masters alike. 

## Project Goals:

* **Faithful to 2e:** The primary focus is to ensure the AI Assistant is specifically knowledgeable about 2nd Edition AD&D rules, avoiding information bleed from later editions.
* **Comprehensive Knowledge Base:** Train the assistant on a wide range of 2e materials to cover character creation, spells, monsters, magic items, and more. 
* **Helpful Features:**  Potentially include features such as:
    * Answering rules questions 
    * Generating character stats
    * Providing encounter ideas
    * Offering summaries of spells or items
* **Open Source & Educational:**  The project will be open-source to serve as a learning resource for others interested in AI, natural language processing, and game development. 

## Project Structure:

* **data/raw:**  Contains the raw text files of the AD&D 2nd Edition rulebooks.
* **data/processed:** Will contain the processed and cleaned data ready for training. 
* **src:** Contains the source code for data preprocessing, model training, and the assistant's functionality.
* **tests:**  Includes unit tests to ensure the correctness of the code.

## Getting Started:

1. Clone the repository.
2. Install the required dependencies listed in `requirements.txt`.
3. Add your raw 2nd Edition AD&D text files to the `data/raw` directory.
4. Run `python src/training.py` to preprocess the data and begin training the AI model. 

**Note:** This README will be updated as the project progresses. 
