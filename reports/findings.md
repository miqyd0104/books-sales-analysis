# Books Sales and Ratings: findings

Source: [Kaggle](https://www.kaggle.com/datasets/thedevastator/books-sales-and-ratings), shared by thedevastator and credited to Josh Murrey. Analysed on 21 October 2026.

## Data

The original file has 1,070 rows and 15 columns. All 1,070 records were retained after cleaning. Missing titles and years were not guessed. The cleaned copy has 20 columns, including language and quality flags.

## Main results

- Mean book rating: 4.01; median: 4.015.
- Children's books have the highest full-sample median units sold (5,265), but only 15 records. The ranking changes in the matching subset.
- Ratings and units sold show little association: Pearson -0.0085, Spearman 0.0005.
- Median prices: children 6.15, nonfiction 4.99, fiction and genre fiction 3.99. Currency is not specified.
- Penguin Group (USA) LLC leads median recorded gross sales among publishers with at least 20 books: 1,381.30.
- 626 records (58.5%) do not reconcile across price, units and gross sales. 372 records have zero publisher revenue.

## Recommendations

1. Verify sales definitions, periods, currency and zero values with the data owner before using the figures for spending decisions.
2. Collect more data before choosing a genre, especially children's books.
3. Don't use average rating alone to forecast sales.
4. Compare publisher medians alongside totals and catalogue size.
5. Check currency, format and market before recommending prices.

## Limits

These are descriptive results from this sample. Coverage and sales timing are unclear, sales fields are inconsistent, and association does not prove causation. Matching records are a sensitivity check, not a verified correct sample. Publishing year is not the year of sale.

Full calculations, six charts and explanations are in `notebooks/01_books_exploration.ipynb`.
