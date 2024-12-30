#
# Tarea Modulo Linea de Comandos
# Alumno: Ernesto Cantu Valle
# Fecha: Diciembre 2024
#
import json
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from Bert import analyze
import matplotlib.pyplot as plt

from Review import Review as UserReview


#nltk.download('stopwords')
#nltk.download('punkt')


def read_file(file_path):
    '''
        Method that read a given file and converts it into a list of json objects
    '''
    reviews = []
    with open(file_path,'r') as file:
        for line in file:
            review = json.loads(line.strip())  # Eliminar el salto de línea
            ur = UserReview()
            ur.init_from_json(review)
            reviews.append(ur)  # Almacenar el valor de "text" en la lista
    return reviews


def normalize_text(txt):
    txt = txt.lower()
    txt = txt.translate(str.maketrans('', '', string.punctuation + '¡¿'))
    txt = re.sub(r'\d+', '', txt)
    txt = re.sub(r'\s+', ' ', txt).strip()
    return txt

def rem_token_and_stop_words(txt):
    tokens = word_tokenize(txt)
    stop_words = set(stopwords.words('english'))
    tokens_filtrados = [word for word in tokens if word.lower() not in stop_words]
    return ' '.join( t for t in tokens_filtrados)

def process_reviews(reviews):
    for review in reviews:
        text = review.comment
        # Step 1 - Normalize
        text = normalize_text(text)
        # Step 2 - Stop Words and Tokens
        tokens = rem_token_and_stop_words(text)
        # Step 3 - Generate Sentiment Analisys.
        resultado = analyze(tokens)
        review.bert_grade = resultado
    return

if __name__ == '__main__':
    '''
        Main entry point of the project.

        It is important to note that, since I've developed this project using an upper folder,
        I had to manage from other folder than "Code". 

        That's why I used the "./Resources/Gift_Cards_reviews.json" route.
    '''
    reviews = read_file("./Code/Resources/Gift_Cards_reviews.json")
    #for user_review in reviews:
    #    print(user_review)
    process_reviews(reviews)
    
    #Preparo las clasificaciones para hacer la construir la gráfica
    tags = ['insatisfecho','neutral','satisfecho']
    bert_values = [0,0,0]
    rating_values = [0,0,0]
    for review in reviews:
        if review.bert_grade < 3:
            bert_values[0] += 1
        elif review.bert_grade == 3:
            bert_values[1] +=1
        else:
            bert_values[2] +=1

        if review.rating < 3:
            rating_values[0] += 1
        elif review.rating == 3:
            rating_values[1] +=1
        else:
            rating_values[2] +=1

    ## Análisis por Bert
    plt.bar(tags, bert_values)
    plt.title('Análisis de reseñas amazon por Bert')
    plt.xlabel('Etiqueta')
    plt.ylabel('Cantidad')
    plt.show()
    

    # Analisis por Rating
    plt.bar(tags, rating_values)
    plt.title('Análisis de reseñas amazon por Bert')
    plt.xlabel('Etiqueta')
    plt.ylabel('Cantidad')
    plt.show()