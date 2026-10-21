# Project plan

Submission deadline: close of business Wednesday 21 October 2026, as specified in the brief.

## Five analytical questions

| Question | Pandas approach | Planned Matplotlib chart | Interpretation to develop |
| --- | --- | --- | --- |
| 1. How are average book ratings distributed? | describe, value counts/bins | Histogram | Are ratings concentrated in a narrow range? |
| 2. Which genres have higher typical units sold? | groupby, median, size | Horizontal bar chart | Compare medians alongside group sample sizes. |
| 3. Are average ratings associated with units sold? | complete pairs, Spearman correlation | Scatter plot | Assess association and unusual observations; do not claim causation. |
| 4. How do sale prices vary by genre? | groupby, describe | Box plot | Compare typical prices and spread; verify currency first. |
| 5. Which publishers have the highest median gross sales per book? | groupby, agg, minimum group size | Horizontal bar chart | Compare median, total and book count to avoid ranking by catalogue size alone. |

## Suggested workflow

1. Inspect the source definitions and audit the CSV.
2. Document cleaning choices before implementing them.
3. Use a separate cleaned copy and record row counts before/after.
4. Answer one question at a time: table → chart → interpretation → commit.
5. Add final recommendations only when evidence supports them.

Each final chart needs a meaningful title, labelled axes, readable formatting and a written interpretation. Include at least three charts; aim for all five above. The initial histogram is an exploration aid and should be revisited after cleaning.
