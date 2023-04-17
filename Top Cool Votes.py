# Find the review_text that received the highest number of  'cool' votes.
# Output the business name along with the review text with the highest numbef of 'cool' votes.

# Import your libraries
import pandas as pd

# Start writing code
df = pd.DataFrame(yelp_reviews)
copy = df[['business_name','review_text','cool']]
max_cool = copy['cool'].max()
max_cool_row = copy.loc[copy['cool'] == max_cool]
