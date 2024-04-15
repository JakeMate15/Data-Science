import stanza

# Descargar e instalar el modelo de inglés si es la primera vez que lo usas
stanza.download('en')  

# Inicializar el pipeline de procesamiento de inglés
nlp = stanza.Pipeline('en')

# Procesar un texto
doc = nlp("Stanford University is located in California. It is a great place for studying AI.")

# Iterar sobre las oraciones y sus dependencias
for sentence in doc.sentences:
    for word in sentence.words:
        print(f"word: {word.text}\tparent: {word.head}\tdependency relation: {word.deprel}")
