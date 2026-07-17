# Analysis of Gender stereotyping language in capital trials
This project analyzes transcript text files given a set of keywords and computes bootstrap-based word and n-gram metrics.

## Project Description
- Reads transcript files and keyword lists from a local input folder
- Preproccesses transcripts
- Builds word and n-gram features
- Identify keywords from MAX_QDA annotations
- Runs bootstrap sampling
- Outputs summary statistics to CSV
- Produces visualizations of results

## Requirements
- Python 3.10+ recommended
- `numpy`
- `pandas`
- `scipy`
- `nltk`
- `gensim`
- `matplotlib`
- `seaborn`
- `scikit-learn`

## Setup
Install dependencies with:

```bash
pip install numpy pandas scipy nltk gensim matplotlib seaborn scikit-learn
```


## Data
- transcripts should be in .txt form
- create transcript folder seperated with subfolders for men and women
- if using chunked data run chunk.ipynb to chunk transcript files and create upload to chunked transcript forlder with subfolders for men and women
- create metadata file for transcripts
- create matched groups of metadata with men and women transcript metadata files using exact_matching_groups.ipynb
- save outputs of matched group metadata files
- create csv of keywords and themes of keywords
- include metadata of men and women


## How to Run
- Use MaxQDA_Term_Extraction.ipynb and files in key_term_supporting folder to construct keyword list, or use provided key term list
- normalize and one hot encode metadata of men and women with propensity_metadata.ipynb
- preprocess and bootstrap keyword metrics with bootstrap_result.ipynb (formerly reimplementation.ipynb)
- visualize results for matched groups with Result_visualizations.ipynb
