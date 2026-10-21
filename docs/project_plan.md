# Analysis approach

The main question is how ratings, genres, prices and publishers relate to the sales figures in this dataset.

| Question | Pandas calculation | Matplotlib chart |
| --- | --- | --- |
| How are ratings distributed? | Summary statistics and median | Histogram |
| Which genres have higher typical sales? | Grouped medians, means and counts; matching-record sensitivity check | Grouped horizontal bar chart |
| Is there a relationship between ratings and sales? | Pearson correlation and correlation of ranks for Spearman | Scatter plot with a log sales axis |
| How do prices vary by genre? | Grouped medians, quartiles and ranges | Box plot |
| How do sales compare across publishers? | Median, total and book count; minimum 20 records for the chart | Horizontal bar chart |
| How consistent are the sales fields? | Gross sales against price × units, tolerance 0.01 | Horizontal bar chart |

## Choices

- Use medians for typical sales because large values can affect means.
- Show group counts because categories have different sample sizes.
- Keep source categories separate unless there is evidence to merge them.
- Keep uncertain values and flag them rather than invent replacements.
- Use all records for the main analysis, with a matching-record sensitivity check. The subset is not assumed to be a verified correct sample.
- Don't infer annual sales trends from publishing years.
- Don't assume a currency, sales period or representative market sample.

All six charts, calculations and interpretations are in the notebook. The final recommendations are in `reports/findings.md`.
