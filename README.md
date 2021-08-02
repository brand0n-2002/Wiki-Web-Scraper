# Wiki-Web-Scraper
## Introduction
Hello, Representative of the Virtual Student Federal Service Internship Program or anyone else who is interested in the code behind a Wiki-Web-Scraper. Though the original intent behind this code was to display my coding skill for VSFS, I hope it is helpful to anyone else who may be looking at it. A brief overview of what will be talked about is the "Task", the "Solution", possible "Future Improvements", and "Helpful Resources" to help code a similar script.

### Task
The task that was given was to write a python script that "*takes in a Wikipedia link and for each section, prints out the title of the section, prints out the most frequent words in the section that are not considered “stop words”, and lists every hyperlink in the section*".

## Solution
1. I first imported the "requests" library to retrieve data from the URL, I next imported the "BeautifulSoup" library to obtain methods to webscrape and parse the URL, and then imported the "nltk.corpus" and "nltk.tokenize" packages to filter and count the words taken from URL.

2. I then entered the Wikipedia Link to be parsed and saved it to the variable "wikilink". Next, I sent a get request to "wikilink" and saved it to variable "results". Following this, using BeautifulSoup, "results" HTML is parsed and saved to the variable "soup". I then initialized the variable "WikiText" as an Empty String.

3. Following this I did a nested for loop which would first print the heading of the respective Wikipedia section and then enter another loop which ran through all of the text of the section saving it to the "WikiText" variable, and also print out all of the links in each section and the name of the link within the page. If the link was a reference or a Wikipedia link the code would go through an additional if elif statement which would fix the link to its correct format. This part is important if we want the links to be accessible.

4. After this I ran a for loop through "WikiText" to purge it of any punctuation and following this broke down "WikiText" into tokens and saved it to the "W_Token" variable. I then saved the stop words to the "S_Words" variable. Next, I checked the "W_Token" and "S_Words" against each other and put them into the "Filter_One" variable if "W_Token" was not in "S_Words".

5. I then made sure that all of the words in "Filter_One" had turned lowercase and saved it to the "Filter_Two" variable. Next, I used the Counter Method to count all of the words in "Filter_Two" and saved it to the "Counter_Filter" variable. Following this, I used the ".most_common(5)" method on "Counter_Filter" to print the top five most mentioned words from most to least and saved it to the "Occurence_Filter" variable.

6. Finally I printed "Occurence_Filter" and reset "WikiText" to an empty string before continuing through the loop printing out the headings, links, and most used words.

Output:
![Screenshot 2021-08-02 173221](https://user-images.githubusercontent.com/88068824/127926558-9e918f09-e34e-4648-9d5b-cc363a7b272e.png)

![Screenshot 2021-08-02 173101](https://user-images.githubusercontent.com/88068824/127926602-222a4ef0-0f4d-4536-93f8-51565b495e47.png)

## Future Improvements
Some future improvements that can be done to the code is a more thorough scraping of the HTML. The way the code orignally works is that it only reads text from lists and paragraphs, so there is a possibility that the code will not find all of the words which could be hidden under other tags. Another improvement could be a more organized manner in printing the links, by splitting the links into the three catagories of Wikipedia links, reference links, and normal links, rather than just printing them in order.

## Helpful Resources
1. Beautiful Soup Documentation - https://www.crummy.com/software/BeautifulSoup/bs4/doc/

2. NLTK Stop Words - https://pythonspot.com/nltk-stop-words/
