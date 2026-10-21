# Books Sales and Ratings Analysis

A starter Pandas and Jupyter project for the Sparta Global data analysis assignment.

**Status:** environment, dataset download and initial exploration prepared. Cleaning, analysis and final recommendations are still to be completed.

## Dataset and purpose

- **Dataset:** Books Sales and Ratings, shared by thedevastator on [Kaggle](https://www.kaggle.com/datasets/thedevastator/books-sales-and-ratings).
- **Downloaded:** 21 October 2026.
- **Initial size:** 1,070 rows and 15 columns, verified from the downloaded CSV.
- **Why this dataset:** it combines book ratings, rating counts, genres, prices and sales measures, giving us numerical and categorical variables for several kinds of analysis.
- **Main question:** which book characteristics are associated with stronger sales in this dataset?

Do not assume the sample represents the whole publishing market. Verify sales definitions, currency, coverage and collection methods before making business recommendations. A publishing year is not the year a sale took place.

## Open in PyCharm

1. Open this `books-sales-analysis` folder as a project.
2. Select the existing interpreter `.venv/bin/python` in **Settings → Python → Interpreter** (the wording may vary by version). Do not create a second environment.
3. Open `notebooks/01_books_exploration.ipynb`.
4. Use the project environment / **Books sales analysis** kernel and run cells from the top.

The `.venv` keeps this project's dependencies separate from other projects. It stays on your computer and is excluded from GitHub.

## Recreate the environment after cloning

Developed using Python 3.14.6. Exact installed package versions are recorded in `requirements-lock.txt`.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-lock.txt
python scripts/download_data.py
python -m jupyter lab
```

`requirements.txt` lists the main dependencies with compatible ranges; the lock file records the environment used here. The download script verifies the CSV against the recorded checksum. If Kaggle changes access requirements, download the CSV from the source page and put it in `data/raw/`.

## Project layout

```text
notebooks/01_books_exploration.ipynb  # Starter notebook and assignment roadmap
scripts/download_data.py             # Reproducible source download
data/raw/                           # Original local CSV and provenance
data/processed/                     # Future cleaned data
reports/figures/                    # Future chart exports
docs/cleaning_log.md                 # Decisions and evidence
docs/project_plan.md                 # Questions and planned charts
```

## Work still to do

- [x] Choose and cite the dataset.
- [x] Create the environment and initial exploration notebook.
- [ ] Apply and document evidence-based cleaning in Python.
- [ ] Answer at least five questions using Pandas.
- [ ] Produce five useful charts of more than one type, including Matplotlib.
- [ ] Write findings, limitations and recommendations backed by the results.
- [ ] Restart the notebook kernel and run all cells before submission.

## Keep committing as you work

Commit each meaningful stage after reviewing your changes, for example `Document missing-value decisions`, `Compare median sales across genres`, and `Add final findings and recommendations`. The initial commits are setup milestones, not a completed analysis.

## Data attribution and reuse

The Kaggle metadata reports **Other (specified in description)** for the dataset licence. The raw CSV is kept local rather than included in this public repository; the source, filename, checksum and download instructions are versioned. Consult the dataset page for reuse terms. No licence is asserted over the source data here.

PyCharm reference: [use an existing virtual environment](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html).
