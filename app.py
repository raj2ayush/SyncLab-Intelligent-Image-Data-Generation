from flask import Flask, render_template, request
from flask_socketio import SocketIO
from flask import Flask, render_template, request
from flask_socketio import SocketIO
from web_crawler import WebCrawler
from dataset_builder import DatasetBuilder
from validator import validatee
from postprocessing import postProcessing
from synonyms import get_synonyms_for_phrase

###VALIDATE###
from validator import validatee

from validator1 import validatee1
###############

from scraper import scrape
app = Flask(__name__)
app.config['DEBUG'] = True
socketio = SocketIO(app)

api_keys = {'google': ('AIzaSyBNzhW3VdaVUckanfETdnTWe20f_ljEQ4o','05e004413ea124cc4'),
            'flickr': ('6c606c90653aa17d5b9b179a922c6b8b', 'd97111c6529166c9')}
# # number of images to fetch
# images_nbr = 4
download_folder = "./data" # folder in which the images will be stored

# Initialize the WebCrawler and DatasetBuilder instances
crawler = WebCrawler(api_keys)
dataset_builder = DatasetBuilder()


@app.route('/validate')
def validate():
    validatee()
    return render_template("index.html")

@app.route('/validate1')
def validate1():
    validatee1()
    return render_template("index.html")


@app.route('/postProcess')
def postProcess():
    postProcessing()
    return render_template("index.html")


@app.route("/crawl_and_download",methods=['POST'])
def crawl_and_download():
        keywords = request.form.get('query')
        images_nbr = int(request.form.get('count'))
        download_folder = "./data"
        print(get_synonyms_for_phrase(keywords))

        # Crawl and download images
        crawler.collect_links_from_web(keywords, images_nbr, remove_duplicated_links=True)
        crawler.save_urls(download_folder + "/links.txt")
        crawler.download_images(target_folder=download_folder)

        # Build the dataset
        source_folder = download_folder
        target_folder = download_folder + "_merged"
        dataset_builder.merge_folders(source_folder, target_folder, extensions=('.jpg', '.jpeg', '.png', '.gif'))

        return "Crawling and downloading completed successfully!"

        return render_template("index.html")

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return crawl_and_download()
    return render_template("index.html")

if __name__ == '__main__':
    socketio.run(app, debug=True)

   