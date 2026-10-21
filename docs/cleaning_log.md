# Cleaning decisions and observations

Status: initial audit only. No rows or values have been corrected or removed yet.

| Issue / observation | Decision for the next stage | Reason / evidence |
| --- | --- | --- |
| `Publisher ` has a trailing space | Strip column names and standardise them on a copy | Avoid errors when selecting columns. |
| `index` looks like an exported row identifier | Check uniqueness and sequence before excluding it from analytical measures | It may identify source rows; preserve the original CSV. |
| 23 missing book names | Keep records initially; decide per question | Other numerical measures may still be usable. |
| 53 missing language codes | Leave missing initially; consider an explicit Unknown group for language summaries | Do not invent a language. |
| 1 missing publishing year | Leave missing initially | No evidence for a replacement year. |
| Earliest year is -560 | Investigate BCE dates and edition/publication semantics | Negative years are not automatically bad data; do not convert directly to modern dates. |
| Genres include fiction and genre fiction | Keep source categories until definitions justify merging | Similar labels may encode different categories. |
| Duplicate records | Audit full rows and analytical columns without `index` | A distinct exported index can conceal duplicate content; title alone is not a safe identifier. |
| Sales, currency and period definitions | Check source documentation | Do not interpret publishing-year groups as annual sales trends. |

For every applied change, record: issue, Python rule, justification, affected rows, and before/after counts. Do not silently fill missing ratings or sales with zero or delete high-sales outliers.
