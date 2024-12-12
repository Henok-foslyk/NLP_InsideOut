# NLP_InsideOut

## Various Models Used for Testing

  -  Neural Network - baseline.ipynb (baseline given by sem_eval)

  -  Sklearn binary classificaion models (Binary Relevance and Classifier Chain) - binarymodels.ipynb 

  -  Improvements on baseline neural network - DL.ipynb

## Transformer models:
   - deberta.ipynb (Deberta final implementation)
   - sam-distilbert-tuning.ipynb (Distilbert final implementation)
   - sam-distilbert-eval.ipynb (Distilbert final evaluations)
   - experiment-transformers.ipynb (initial DistilBert experiments)
   - neuralnetnotebook.ipynb (inital DeBERTa experiments)

## Data:
We worked on the sem_eval dataset:

 - We trained on the english dataset given:
     
   - eng_train.csv
          
 - We tested on both english and translated amharic dataset:
     
   - amharic_translated_ordered.csv (from sem_eval dataset and has more rows)
   - eng_dev.csv (submitted to sem_eval website)
   - xed_fixed.csv ( form Helsinki dataset after dropping extra labels)

file_translate.py  -- translation script used for amharic -- works with google cloud API
      


