# Books Sales and Ratings

So, I choose this dataset on book sales and ratings which I found on Kaggle.
I will be exploring how book ratings, genres, prices and publices relate to sales using Python, Pandas and Matplotlib in a Juptyer notebook.

## Dataset

[Books Sales and Ratings on Kaggle](https://www.kaggle.com/datasets/thedevastator/books-sales-and-ratings), shared by thedevastator.

The dataset has **1,070 rows and 15 columns**. I looked it to many datasets, including movie sales, anxiety and wellbeing and others but I chose to go with this dataset.

## Questions

- (1) How are book ratings distributed?
- (2) Which genres have higher typical sales?
- (3) Is there a relationship between ratings and sales?
- (4) How do prices vary by genre?
- (5) How do sales compare across publishers?

## Files

- `notebooks/01_books_exploration.ipynb` — Notebook with markdowns so you can understand what I wrote. 
- `docs/cleaning_log.md` — data issues, a log of the cleaning
- `docs/project_plan.md` — analysis questions and chart ideas (may change)
- `scripts/download_data.py` —  dataset download

## Running the notebook

Open the project folder in PyCharm, select `.venv/bin/python` as the interpreter, then open the notebook.

To set it up after cloning:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-lock.txt
python scripts/download_data.py
python -m jupyter lab
```

The CSV is downloaded into `data/raw/`. It isn't included in the repo; the download details are in that folder.
