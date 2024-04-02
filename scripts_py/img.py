from transformers import pipeline

def summarize_text(article, max_length=1000, min_length=30, do_sample=False):
    summarizer = pipeline("summarization", model="Falconsai/text_summarization")
    # Generate the summarized text
    summerized_text = summarizer(ARTICLE, max_length=1000, min_length=30, do_sample=False)
    summerized_text=summerized_text[0]['summary_text']
    return summerized_text

# Example usage:
ARTICLE = """ 
Limitations Specialized Task Fine-Tuning: While the model excels at text summarization, its performance may vary when applied to other natural language processing tasks. Users interested in employing this model for different tasks should explore fine-tuned versions available in the model hub for optimal results. Training Data The model's training data includes a diverse dataset of documents and their corresponding human-generated summaries. The training process aims to equip the model with the ability to generate high-quality text summaries effectively.
"""
summary = summarize_text(ARTICLE)
print("Summary:", summary)