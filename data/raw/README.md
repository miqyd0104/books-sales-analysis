# Dataset

[Books Sales and Ratings on Kaggle](https://www.kaggle.com/datasets/thedevastator/books-sales-and-ratings), shared by thedevastator. The source description credits [Josh Murrey](https://data.world/josh-nbu).

File: `Books_Data_Clean.csv` — 1,070 rows and 15 columns. Dataset version 2, last updated 6 December 2023. Downloaded on 21 October 2026. The checksum in `manifest.json` records the exact CSV used.

Run `python scripts/download_data.py` from the project folder to download it. The script verifies the checksum and will not overwrite a different file.

The source describes gross sales as book sales revenue, sale price as the price per copy, and units sold as the number of copies sold. It does not clearly specify currency, sales period, sampling method, book format or why the sales measures may not reconcile. The author rating field is categorical in the CSV even though the description calls it numeric.

Kaggle lists the licence as “Other (specified in description)”. The raw and cleaned CSVs are kept locally; see the source page for reuse terms. No additional licence is claimed over the source data.
