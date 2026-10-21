# Books Sales and Ratings

So, I chose this dataset on book sales and ratings which I found on Kaggle. I looked at a few options, including movie sales, anxiety and wellbeing, before choosing books.

I used Python, Pandas and Matplotlib in a Jupyter notebook to look at how ratings, genres, prices and publishers relate to sales.

## Dataset

[Books Sales and Ratings on Kaggle](https://www.kaggle.com/datasets/thedevastator/books-sales-and-ratings), shared by thedevastator and credited to [Josh Murrey](https://data.world/josh-nbu).

The original file has **1,070 rows and 15 columns**. All records were kept after cleaning. I tidied names and spaces, checked types and missing values, and added flags for issues that could not safely be corrected.

## Questions

1. How are book ratings distributed?
2. Which genres have higher typical sales?
3. Is there a relationship between ratings and sales?
4. How do prices vary by genre?
5. How do sales compare across publishers?
6. How consistent are the sales fields?

## Main findings

- Ratings are mostly close to four stars: the mean is **4.01** and the median is **4.015**.
- Ratings show almost no association with recorded units sold in this sample.
- Children's books have the highest median units sold in the full sample, but there are only **15 records**, and the ranking changes when the sales check is applied.
- Penguin has the highest median recorded gross sales among publishers with at least 20 records. Amazon has the largest total and the most records.
- **626 records (58.5%)** don't reconcile across price, units and gross sales. This is the main limitation of the sales comparisons.

My first recommendation is to check the sales definitions with the data owner before making spending decisions. Ratings alone also aren't a good basis for a sales forecast here. The notebook explains the other findings and limitations.

## Files

- [Notebook](notebooks/01_books_exploration.ipynb) — code, results, six charts and Markdown explanations
- [Cleaning log](docs/cleaning_log.md) — changes and reasons
- [Analysis approach](docs/project_plan.md) — questions and methods
- [Findings](reports/findings.md) — short summary and recommendations
- [Charts](reports/figures/) and [summary tables](reports/tables/)
- `scripts/download_data.py` — downloads and checks the dataset

## Running the notebook

Tested with Python **3.14.6**. The virtual environment is local and isn't included in GitHub downloads.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-lock.txt
python scripts/download_data.py
python -m ipykernel install --prefix .venv --name books-sales-analysis --display-name "Books sales analysis"
python -m jupyter lab
```

In PyCharm, choose `.venv/bin/python` as the interpreter and open `notebooks/01_books_exploration.ipynb`. Select the **Books sales analysis** kernel if asked, then run the cells from the top.

The notebook saves the cleaned CSV in `data/processed/` and recreates the charts, summary tables and findings report. Raw and cleaned CSVs stay local; the source and download details are in `data/raw/`.
