from src.scraping import Scraping
from src.extraction import Extraction

if __name__ == '__main__':
    print("Starting App Review Extraction for To The Trenches...\n")
    
    review_file = Scraping().run()
    Extraction(file=review_file).extract()

    print("Extraction complete!\nApp Reviews can be found in low_rated_reviews.csv")
