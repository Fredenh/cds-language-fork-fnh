# load packages 
import spacy 
# initialize spacy
nlp = spacy.load("en_core_web_lg")

# virtual environment only contains a version of Python but no packages. 
# you can install any packages you need in your virtual environment
# this is useful because it doesnt interfere with other local or global environments with packages installed
# python3 -m venv spacy_env
# source ./spacy_env/bin/activate
# deactivate leaves the virtual environment

# setup script
# python3 -m venv spacy_env
# source ./spacy_env/bin/activate
# python3 pip install --upgrade pip
# python3 -m pip install -r requirements.txt
# python3 src/script.py
# python3 -m spacy download en_core_web_md
# deactivate

def main():
    text = "This is a string"
    doc = nlp(text)
    for token in doc:
        print(token.text)

if __name__=="__main__":
    main()