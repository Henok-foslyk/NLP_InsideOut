# NLP_InsideOut

Baseline from sem_eval - baseline.ipynb

Sklearn model trials - binarymodels.ipynb (Binary Relevance and Classifier Chain)

Improvements on baseline model - DL.ipynb

## Transformer models:
   - experiment-transformers.ipynb (DistilBert)
   - neuralnetnotebook.ipynb (DeBERTa)

## Data:
We worked on the sem_eval dataset:

     - We trained on the english dataset given:
     
          - eng_train.csv
          
     - We tested on both english and translated amharic dataset:
     
          - amharic_translated_ordered.csv (from sem_eval dataset)
          - eng_dev.csv
          - xed_fixed.csv ( form Helsinki dataset after dropping extra labels)

file_translate.py  -- translation script used for amharic -- works with google cloud API
      


