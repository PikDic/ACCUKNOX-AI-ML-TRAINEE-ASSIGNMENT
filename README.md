# AccuKnox AI/ML Assignment

This repository contains solutions for the AccuKnox AI/ML assignment.

#Pratik Kishor Nayak
#mail: kishorpratik023@gmail.com
#resume: https://drive.google.com/file/d/1m5xhwXanI_dnRq_ZOYTCa52K5N6O-axb/view?usp=drive_link

--------------------------------------------------------------

### Task 1.1 – API Data Retrieval and Storage
- Fetches book data from a public REST API
- Stores data in a local SQLite database
- Displays stored records
  
  fetch_books.py → API fetch
  db_connection.py → SQLite connection
  book_repository.py → DB operations
  main.py → Orchestration

📁 Code location: Problem Statement 1/src/

---

### Task 1.2 – Data Processing and Visualization
- Implemented in Google Colab
- Uses a dataset to calculate averages and visualize results
- Used kaggle dataset -> (https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
  
📁 Notebook: Problem-statement-1/Task 1.2_.ipynb

---

### Task 1.3 – CSV Data Import to Database
- Uses a real CSV file
- Imports user data into SQLite using a Python script

📁 Script Location: Problem-statement-1/scripts/import_csv_to_db.py
📁 CSV Location: Problem-statement-1/data/

---
  


## How to Run Tasks 1.1 and 1.3

1. Navigate to the folder:
   cd "Problem-statement-1"

2. Install dependencies:
   python -m pip install -r requirements.txt

3. Run Task 1.1:
   python src/main.py

4. Run Task 1.3:
   python scripts/import_csv_to_db.py
