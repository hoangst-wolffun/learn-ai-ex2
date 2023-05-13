import pandas as pd
import string

# Read the text file
with open('story.txt', 'r') as file:
    text = file.read()

# Remove punctuation characters
translator = str.maketrans('', '', string.punctuation)
cleaned_text = text.translate(translator)

# Create a DataFrame from the cleaned data
data = pd.DataFrame({'text': cleaned_text.split()})

# # Display general information about the DataFrame
# print(data.head())
# print(data.shape)
# print(data.describe())

# Perform value count on 'column_name'
count_data = data.value_counts()
# Sort the counts in descending order
sorted_data = count_data.sort_values(ascending=False)

# Display the top 5 rows
top_5 = sorted_data.head(100)
print(top_5)