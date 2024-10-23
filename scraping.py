from app_store_scraper import AppStore
import pandas as pd
import numpy as np


class Scraping:
    def __init__(self):
        self.review_file = "app_store_reviews.csv"

    def run(self):
        ttt = AppStore(country='us', app_name='to-the-trenches', app_id='6443956171')
        ttt.review(how_many=200)

        # Convert the data into a DataFrame
        df = pd.DataFrame(np.array(ttt.reviews), columns=['review'])
        df_list = df.join(pd.DataFrame(df.pop('review').tolist()))
        df_list.head()

        # Save the DataFrame to a CSV file
        df_list.to_csv(self.review_file, index=False)

        print(f"{self.review_file} file with reviews saved.\n")
        return self.review_file