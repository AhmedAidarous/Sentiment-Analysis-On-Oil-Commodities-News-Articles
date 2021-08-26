# Web scraping crude oil news and using VADER for sentiment analysis

import requests
from bs4 import BeautifulSoup
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Create lists to store scrapped news urls, headlines and text.
urlList = []
dateTime = []
newsText = []
headlines = []

# The counter is the number of pages we would like to scape, and creates the urls to be accessed
# Iterates through the
#           <div>
#               <categoryArticle>
#            </div>

for page in range(1,3):
    # Get the list of unique URLS in the page
    url = "https://oilprice.com/Energy/Crude-Oil/Page-{}.html" .format(page)
    request = requests.get(url)

    # Parses the HTML to scrape the important elements
    soup = BeautifulSoup(request.text , "html.parser")

    for links in soup.find_all('div', {'class': 'categoryArticle'}):
        for info in links.find_all('a'):
            if info.get('href') not in urlList:
                urlList.append(info.get('href'))


# Accessing each URL scraped
for www in urlList:
    # Extract the headline and remove the dash delimiter to fit our sentiment Analysis algorithm
    headlines.append(www.split("/")[-1].replace('-',' '))

    request = requests.get(www)
    soup = BeautifulSoup(request.text , "html.parser")

    # Store the dates and time of publications of each article
    for dates in soup.find_all('span', {'class':'article_byline'}):
        dateTime.append(dates.text.split('-')[-1])

    # Store the news article text by extracting the <p> element
    text = []
    for news in soup.find_all('p'):
        text.append(news.text)


    # Identify the last line of the news article
    for lastSentence in reversed(text):
        if lastSentence.split(" ")[0] == "By" and lastSentence.split(" ")[-1] == "Oilprice.com":
            break
        elif lastSentence.split(" ")[0] == "By":
            break


    joinedText = ' '.join(text[text.index("More Info") + 1 : text.index(lastSentence)])
    newsText.append(joinedText)


# Saves the news text with the news headline in a pandas dataframe
newsDataFrame = pd.DataFrame({'Date' : dateTime,
                              'Headline' : headlines,
                              'News' : newsText
                              })



# Initializing the Sentiment Analysis Algorithm
sentimentAnalysisModel = SentimentIntensityAnalyzer()

def compoundScore(text):
    return sentimentAnalysisModel.polarity_scores(text)["compound"]

newsDataFrame["sentiment"] = newsDataFrame["News"].apply(compoundScore)

# Calculating overall sentiment
sentimentSum = newsDataFrame["sentiment"].sum()

# Gets both the highest and lowest sentiment values
highestSentiment , lowestSentiment = newsDataFrame["sentiment"].max() , newsDataFrame["sentiment"].min()

# Get the highest and lowest sentiment news articles
positiveHeadline = (newsDataFrame.loc[newsDataFrame["sentiment"] == highestSentiment])["Headline"]
negativeHeadline = (newsDataFrame.loc[newsDataFrame["sentiment"] == lowestSentiment])["Headline"]

positiveHeadline = positiveHeadline.iloc[0]
negativeHeadline = negativeHeadline.iloc[0]


sentimentClass = ""
# Returns the classified result
if (sentimentSum > 0.05):
    sentimentClass = "Looking Good!"

elif (sentimentSum < 0.05 and sentimentSum >= -0.05):
    sentimentClass = "Neutral"

else:
    sentimentClass = "Not Looking Good!"



# The results
print("""

Overall Sentiment Analysis

* OverallCompoundScore : %s (%s)

* Most Positive News Headline: 
    "%s"

* Most Negative News Headline: 
    "%s"

""" % (round(sentimentSum , 3) , sentimentClass, positiveHeadline[:len(positiveHeadline) - 5] ,negativeHeadline[:len(negativeHeadline) - 5]))
