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

3. Run the scraper using:

```bash
cd data-gathering
python meralco_scraper.py
```