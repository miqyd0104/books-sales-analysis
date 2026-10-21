# Books Sales and Ratings

I'm exploring how book ratings, genres, prices and publishers relate to sales using Python, Pandas and Matplotlib in a Jupyter notebook.

## Dataset

[Books Sales and Ratings on Kaggle](https://www.kaggle.com/datasets/thedevastator/books-sales-and-ratings), shared by thedevastator.

The dataset has **1,070 rows and 15 columns**. I chose it because it has a mix of ratings, sales figures and book details to compare.

## Questions

- How are book ratings distributed?
- Which genres have higher typical sales?
- Is there a relationship between ratings and sales?
- How do prices vary by genre?
- How do sales compare across publishers?

## Files

- `notebooks/01_books_exploration.ipynb` — initial checks and a ratings chart
- `docs/cleaning_log.md` — data issues found so far
- `docs/project_plan.md` — analysis questions and chart ideas
- `scripts/download_data.py` — downloads the dataset

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
