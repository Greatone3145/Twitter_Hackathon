# Twitter_Hackathon

## Inspiration
We wanted to challenge our knowledge of Python, AI and databases -We wanted to find a way to determine how successful people on twitter are at predicting stock price changes

## What it does
Scrapes Twitter for tweets predicting the movement of specific stocks -The raw data of each tweet and stock movement is sorted through and uploaded to a database -An AI model receives some of the filtered data and learns how to predict whether a tweet's prediction will be correct -The AI test results are visualized on a graph

## How we built it
All code in the project was done in Python -Twitter API (tweepy and Yahoo Finance) to obtain the raw data -PostGreSQL to create the database and filter the data we obtained -Python Libraries (numpy, sci-kit learn) to create the AI classifier and then train and test the AI -We used a Naive Bayes AI model due to its common use in classification and data filtering. Also, it works well with large data sets -MatPlotLib to graph the results from the AI's predictions regarding what percentage of tweets have a successful prediction

## Challenges we ran into
Yahoo Finance API broke after 7 PM because the markets close
This caused an issue where the data stored for every stock resets
Our program could not function with empty data
The database gave issues when importing the data

## Accomplishments that we're proud of
Using 2 APIs that we had no prior knowledge of
Developing a database from scratch, with little knowledge
Developing an AI
Developing a graph in Python

## What we learned
Teamwork is essential to get a big project done
Communication is also key to succeeding

Try it out
