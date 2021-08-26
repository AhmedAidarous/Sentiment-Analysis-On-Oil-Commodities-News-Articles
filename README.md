# Sentiment-Analysis-On-Oil-Commodity-News-Articles
A script which web scrapes crude oil news articles, and performs sentiment analysis on these articles to see whether these articles are projecting either (Good things, bad things, or neural things) on the oil commodity market, and could be used as a potential indicator of oil prices for any commodity investors out there.

The algorithm returns the three outputs:
<br>• The Overall Sentiment Rating 
<br>• The most negative news article w URL
<br>• The most positive news article w URL

## What is Sentiment-Analysis
Sentiment analysis, also referred to as opinion mining, or polarity detection, refers to the set of algorithms and techniques used to extract the polarity of a given document, meaning whether the document conveys a positive, negative, or neutral.
So, if you can think about it, NLP tries to figure out the human language, while sentiment analysis tries to decode the language and understand the “sentiment” of the message.

This is a growing field, and is gaining popularity by the day, as it’s now widely used for:
<br>•	Advertisement Campaigns 
<br>•	Political Campaigns 
<br>•	Stock Analysis 
<br>•	Product Review Mining 
<br>•	Etc. 

## The Process
The following shows the program performing sentiment analysis on all articles it scrapes:
![image](https://user-images.githubusercontent.com/47617364/131044479-43803c16-8bbb-4ce9-87c1-26daca979b34.png)

<br><br>
From the data collected in the image above, the final result would look as follows:



## Relevant Libraries
The most prominent library used was **VADER** (**V**alence **A**ware **D**ictionary and s**E**ntiment **R**easoner), which performs the sentiment analysis on news articles related to oil, other dependencies include:
<br>• requests
<br>• BeautifulSoup
<br>• pandas 

