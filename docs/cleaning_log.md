# Cleaning log

The original CSV has 1,070 rows and 15 columns. The cleaned copy has 1,070 rows and 20 columns. No records were removed.

| Check or change | What I did | Result and reason |
| --- | --- | --- |
| Column names | Removed spaces at the ends, changed names to lowercase and used underscores | Makes column selection consistent. `Publisher ` becomes `publisher`. |
| Source index | Renamed `index` to `source_row` | Keeps the original row reference; not used as a sales measure. All identifiers are unique. |
| Text spacing | Removed leading/trailing spaces and reduced repeated spaces to one | Changed 33 book names, 19 author entries and 600 publisher entries. |
| Duplicates | Checked exact duplicates, then content without the source index, before and after tidying | 0 duplicates; 0 rows removed. Titles alone were not used to identify duplicates. |
| Missing book names | Kept all 23 missing | The sales, genre, rating and publisher fields can still be compared. No names were guessed. |
| Missing language | Kept 53 missing original codes; used Unknown only in the new language group | Avoids inventing a language while allowing grouped summaries. |
| Language groups | Grouped eng, en-US, en-GB and en-CA as English in a separate field | Original codes are retained. French, Spanish, Arabic and Dutch are also mapped. |
| Numeric conversion | Used `pd.to_numeric`; whole-number fields use nullable `Int64` | 0 new missing values from conversion. The 1 missing publishing year stays missing. |
| Range checks | Checked ratings, non-negative prices/sales/counts, positive sales ranks and future years | No invalid values were found under these rules. Checks stop the notebook if unexpected values appear later. |
| Negative years | Retained and flagged 6 years below zero | Could refer to ancient works. They were not treated as modern dates or used as sales dates. |
| Garbled titles | Flagged 20 possible encoding issues using a text pattern | Heuristic review flag only; names were not rewritten by guessing. |
| Genre labels | Kept fiction and genre fiction separate | The source does not clearly explain the difference. |
| Author rating | Kept as a text category | The actual values are labels, despite the source calling the field numeric. |
| Publisher labels | Tidied spaces; kept similar names separate | No evidence that similarly named entries can safely be merged. |
| Sales consistency | Compared gross sales with price × units sold using an absolute tolerance of 0.01 | 444 match; 626 do not. Recorded figures were retained and flagged, not recalculated as replacements. |
| Publisher revenue | Kept 372 zero values | All are labelled Amazon Digital Services, Inc. Their meaning needs checking with the source. |

The five added fields are `language_group`, `publishing_year_bce`, `possible_encoding_issue`, `revenue_gap` and `sales_values_match`.

The sales comparisons use the full sample, with a separate matching-record check for sensitivity. Matching records are not assumed to be a verified correct sample. Medians and book counts are reported together. The publisher chart requires at least 20 records, leaving the two groups of four out of the ranking but keeping them in the summary table.

The cleaning code and before/after counts are in the notebook. The raw and cleaned CSV files stay local; the repo includes the download script, summary tables and charts.
