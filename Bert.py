#
# Referencias:
#   1. Sentiment Analysis: https://www.youtube.com/watch?v=szczpgOEdXs
#   2. Cómo resolví el problema de error con el clasificador: https://stackoverflow.com/questions/69065131/oserror-when-loading-tokenizer-for-huggingface-model
#
#   Creé el clasificador completo y lo corrí con las líneas 17 y 18 sin comentar.
#   Esto descargó el modelo y el tokenizer de Sentiment Analysis en la carpeta nlptown.
#   A partir de ahi, ya con el modelo y tokenizer en local, el resto del módulo funcionó.
#    
#
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL = f"nlptown/bert-base-multilingual-uncased-sentiment"

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

##tokenizer.save_pretrained(MODEL)
##model.save_pretrained(MODEL)

def analyze(txt):
    tokens = tokenizer.encode(txt,return_tensors='pt')
    result = model(tokens)
    resultado = int(torch.argmax(result.logits))+1
    return resultado


if __name__ == '__main__':
    resultado = analyze("ok")
    print(resultado)