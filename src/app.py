import random
import os
import requests
from flask import Flask, render_template, abort, request

from MemeGenerator.MemeEngine import MemeEngine
from QuoteEngine.Ingestor import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')

 
def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # quote_files variable
    quotes = []
    for file_path in quote_files:
        if Ingestor.is_file_compatible(file_path):
            quotes.extend(Ingestor.parse(file_path))

    images_path = "./_data/photos/dog/"

    # images within the images images_path directory
    imgs = []
    for file_name in os.listdir(images_path):
        imgs.append(os.path.join(images_path, file_name))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    try:
        img = random.choice(imgs)
        quote = random.choice(quotes)
        path = meme.make_meme(img, quote.body, quote.author)
        return render_template('meme.html', path=path)
    except:
        return render_template('error.html')


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    if not image_url:
        return render_template('error.html')
    try:
        tmp_file_path = f'tmp/{os.path.basename(image_url)}'
        rq_file = requests.get(image_url)
        with open(tmp_file_path, 'wb') as f:
            f.write(rq_file.content)

        path = meme.make_meme(tmp_file_path, body, author)

        os.remove(tmp_file_path)
        path = None

    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run()
