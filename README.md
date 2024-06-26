# cs132-ph-electric-shortages

## Data Gathering

This sections provides an overview of the scrapers used and how to use them.

### Meralco Scraper

1. Install Python. For consistency, make sure it's at least Python 3.10

2. Move your directory towards `data-gathering` and install the requirements using `pip`. You can make a virtual environment if you want.

```bash
cd data-gathering
pip install -r requirements.txt
```

3. Prepare environmental file. The environment file should be named `.env` and should contain the following fields.

```sh
FACEBOOK_USER=(your facebook username)
FACEBOOK_PASS=(your facebook password)
```

Do not share this file.

4. Run the scraper using:

```bash
cd data-gathering
python meralco_scraper.py {number of days to scrape} {start date in Y-M-D format}
```

## Exploratory Data Analysis

This section/folder contains all the data (cleaned) and the colab notebook for processing the data. The colab noteboot also produces the nutshell plot and the necessary plots for the web portfolio.

## Machine Learning

This section contains the colab notebook for machine learning.
