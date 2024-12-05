from google.cloud import translate_v2 as translate
import csv
import sys
import os

def translate_to_english(text):
    """
    Translates the input text to English using Google Cloud Translation API.
    """
    client = translate.Client()
    result = client.translate(text, target_language="en")
    return result['translatedText']

def process_csv(input_file, output_file):
    """
    Reads a CSV file, translates sentences in the second column, and writes to a new CSV file.
    """
    try:
        with open(input_file, mode='r', encoding='utf-8') as infile, \
             open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
            
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            # Write the header row
            header = next(reader)
            writer.writerow(header)

            # Translate each row
            for row in reader:
                row_id = row[0]          # The ID column (first column)
                sentence = row[1]       # The sentence to be translated (second column)
                labels = row[2:]        # Remaining columns are labels (unchanged)
                try:
                    translated_sentence = translate_to_english(sentence)
                except Exception as e:
                    print(f"Error translating sentence '{sentence}': {e}")
                    translated_sentence = sentence  # Fallback: use original sentence
                
                writer.writerow([row_id, translated_sentence] + labels)
        
        print(f"Translation complete. Output saved to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ensure proper usage
    if len(sys.argv) != 2:
        print("Usage: python translate.py <input_csv_file>")
        sys.exit(1)
    
    input_csv = sys.argv[1]
    output_csv = os.path.splitext(input_csv)[0] + "_translated.csv"

    process_csv(input_csv, output_csv)
