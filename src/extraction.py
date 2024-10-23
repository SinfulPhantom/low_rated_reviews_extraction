import os
import pandas as pd


class Extraction:
    def __init__(self, file):
        self.file = file
        self.extraction_file = "low_rated_reviews.csv"

    def extract(self):
        try:
            df = pd.read_csv(self.file)

            # Filter reviews for date, rating and review with low ratings
            low_ratings = df[df['rating'].isin([1,2,3])]
            low_rated_reviews_filtered = low_ratings[['date', 'rating', 'review']]
            sorted_reviews = low_rated_reviews_filtered.sort_values(by='rating', ascending=True)

            # Remove old file if it exists
            if os.path.exists(self.extraction_file):
                os.remove(self.extraction_file)

            # Save to a new CSV file
            sorted_reviews.to_csv(self.extraction_file, index=False)
            print("App Store Ratings Extraction completed!\n")

        except Exception as e:
            print(f"An error has occurred: {e}")
