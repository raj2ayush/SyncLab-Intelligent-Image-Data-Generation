#Import libraries
import os
import concurrent.futures
from GoogleImageScraper import GoogleImageScraper
from patch import webdriver_executable


webdriver_path = os.path.normpath(os.path.join(
    os.getcwd(), 'webdriver', webdriver_executable()))
image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))


def scrape(query,num,width,height,extension):

    def worker_thread(search_key):
        image_scraper = GoogleImageScraper(
            webdriver_path, image_path, search_key, number_of_images, headless, min_resolution, max_resolution,max_missed)
        image_urls = image_scraper.find_image_urls()
        image_scraper.save_images(image_urls, keep_filenames,extension)
        #Release resources 
        del image_scraper
    
    #Defining file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))
    # keyword = input("Enter the keyword - ")
    keyword = query
    # number_of_images = int(num)
    
    if num is not None:
        number_of_images = int(num)
    if width is not None:
        width = int(width)
    if height is not None:
        height = int(height)
    
    search_keys = list()
    search_keys.append(keyword)

    #Parameters
    # number_of_images = int(input("Enter the number of images - "))
    headless = True                     
    min_resolution = (0, 0)            
    max_resolution = (width, height)       
    max_missed = 10                   
    number_of_workers = 1               
    keep_filenames = False              

    #Runs each searchkey in a separate thread
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_workers) as executor:
        executor.map(worker_thread, search_keys)
