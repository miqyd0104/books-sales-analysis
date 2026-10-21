# Data checks

These are the issues found during the first checks. The original CSV has been kept unchanged.

| Issue | Notes |
| --- | --- |
| `Publisher ` has a space at the end | Column names need tidying. |
| `index` appears to be a row number | Check it before leaving it out of the analysis. |
| 23 missing book names | These rows may still be useful for sales and ratings comparisons. |
| 53 missing language codes | There isn't enough information to fill them in. |
| 1 missing publishing year | Leave it missing unless a reliable value is available. |
| Earliest publishing year is -560 | This could refer to an ancient work, so it needs checking. |
| Both fiction and genre fiction appear | Keep them separate unless the source explains the difference. |

The notebook also checks for duplicates, including duplicates without the index column. Cleaning changes will be recorded here when they are applied.

Publishing year is different from the year a sale happened. The sales period and currency also need checking before drawing conclusions.
