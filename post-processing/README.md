# cs132-ph-electric-shortages

## Post-Processing

This directory contains the scripts used to post-process all scraped data. Each script is named identically to the data file it processes. All outputs will be stored in the `out` folder in this directory, with the same file name as its script.


The list of sample data to help in creating the post-processors can be found [here](https://drive.google.com/drive/folders/1YIvqTxgiY1DS0fBB8v0yPlLavl3oAjDn?usp=sharing).

### Format

The format of the post-processors must be consistent. Hence, the output of each script should follow these guidelines:

- The script should be in Python.
- The script should take all input (that is until end-of-file).

#### PHASE 1

The script should output a **list of strings** where each string should be a valid electric shortage post. 