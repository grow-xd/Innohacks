from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM, Seq2SeqTrainingArguments, Seq2SeqTrainer
import torch
import sys
checkpoint = "Jayveersinh-Raj/hindi-summarizer-small"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
# Input paragraph for summarization
input = "मुझे याद है, बचपन में जब कोई मुझसे पूछा करता था कि तुम बड़े हो कर क्या बनना चाहते हो, तो मेरा एक ही जवाब होता था, कि मैं बड़ा हो कर policeman बनना चाहता हूँ. उनकी वर्दी, और निडरता मुझे हमेशा ही आकर्षित करती थी. लेकिन जैसे जैसे मैं बड़ा हुआ, मेरी सोच में बदलाव आया, और उसी के साथ बदलाव आया मेरे career goals में. बचपन के बजाय, मेरे goals अब बेहतर तरीके से सोचे और सुलझे हुए थे. लेकिन इतना सोचने के बाद भी मैंने कई ऐसी jobs की, जिनमे मुझे बिलकुल भी interest नहीं आया. काफी समय बाद मैं अपने passion को समझ पाया. मुझे यकीन है कि आप में से भी कई लोग इस दौर से गुज़र रहे होंगे. लेकिन आपको घबराने की बिलकुल भी ज़रुरत नहीं है. अक्सर अपनी dream job को पहचानना थोड़ा मुश्किल हो जाता है, लेकिन एक बार आपने जान लिया, कि आप अपनी ज़िन्दगी में क्या करना चाहते हैं तो कोई आपको नहीं रोक सकता।"
def hin_sum(input):
    # Tokenize the input sentence
    input_ids = tokenizer.encode(input, return_tensors="pt")
    # Generate predictions
    with torch.no_grad():
        output_ids = model.generate(input_ids, max_new_tokens=200)
    # Decode the generated output
    output_sentence = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return output_sentence
print(hin_sum(input).encode('utf-8').decode(sys.stdout.encoding, 'ignore'))




