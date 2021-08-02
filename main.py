#Imported "requests" module to retrieve data from URL
#Imported "BeautifulSoup" to webscrape and parse the URL
#Imported "stopwords" and "word_tokenize" to filter and count the words taken from URL
import requests
from bs4 import BeautifulSoup
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Entered the Wikipedia Link to be parsed and saved it to variable "wikilink"
#Sent a get request to "wikilink" and saved it to variable "results"
#Using BeautifulSoup, "results" html is parsed and saved to variable "soup"
#WikiText is initialized as an Empty String
wikilink = "https://en.wikipedia.org/wiki/Minecraft"
results = requests.get(wikilink)
soup = BeautifulSoup(results.content, "html.parser")
WikiText = ""

#For loop is used to run though the html and find lines with the tag "h2"
for heading in soup.findAll("h2"):

    #If statement is used to differentitate Wikipedia section headings (has "span" tag) from section sub-headings (doesn't have "span" tag)
    if heading.span:

        #Wikipedia Section Head is printed
        print("----------------------------------------------------------------")
        print("Headings:", heading.span.text)
        print("----------------------------------------------------------------")
        print("Links for", '"' + heading.span.text + '"', "section:")

        #For loop is used to run through the html in the respective section of the heading
        for part in heading.next_siblings:

            #If elif statment is used to determine that the data being scraped comes from "p" and "ul" tags (paragraph and lists) and breaks if it comes from an "h2" tag (heading)

            #If the tag is "p" or "ul" indicating a paragraph or list, the text is added to "WikiText" variable
            if part.name == "p" or part.name == "ul":
                WikiText += part.text

                #For loop is used to run through html in the respetive location of the respective section of the heading to find all html with "a" tag which is for links
                for text in part.find_all('a'):

                    #If elif statment is used to determine which links are Wikipedia links, Third-party links, or just references.

                    #Refereneces
                    if "cite" in text["href"]:

                        #Generic reference link is saved to "output" variable before proper modification
                        output = wikilink + text["href"]
                        print("Reference:", text.text)

                        #Generic reference link is modified to correct URL encoding

                        # Parenthesis adjustment
                        if "(" in text["href"]:
                            output = output.replace("(", "%28").replace(")", "%29")

                        # Apostrophe adjustment
                        if "'" in text["href"]:
                            output = output.replace("'", "%27")

                        # Quote adjustment
                        if '"' in text["href"]:
                            output = output.replace("'", "%22")

                        # En dash adjustment
                        if "–" in text["href"]:
                            output = output.replace("–", "%E2%80%93")

                        # Em dash adjustment
                        if "—" in text["href"]:
                            output = output.replace("—", "%E2%80%94")

                        # "output" (link) is printed
                        print(output)

                    #Wikipedia
                    elif "wiki" in text["href"]:

                        #Generic Wikipedia link is saved to "output" variable before proper modification
                        output = "https://en.wikipedia.org" + text["href"]
                        print(text.text)

                        #Generic Wikipedia link is modified to correct URL encoding

                        #Parenthesis adjustment
                        if "(" in text["href"]:
                            output = output.replace("(", "%28").replace(")", "%29")

                        #Apostrophe adjustment
                        if "'" in text["href"]:
                            output = output.replace("'","%27")

                        #Quote adjustment
                        if '"'in text["href"]:
                            output = output.replace("'","%22")

                        #En dash adjustment
                        if "–" in text["href"]:
                            output = output.replace("–","%E2%80%93")

                        #Em dash adjustment
                        if "—" in text["href"]:
                            output = output.replace("—","%E2%80%94")

                        #"output" (link) is printed
                        print(output)

                    #Third-party
                    else:
                        print(text["href"])

            #If tag is "h2" indicating a heading print a line of stars and break out of loop
            elif part.name == "h2":
                print("***************************************************************************************")
                break

            #"punc" variable contains multiple types of punctuation which will be filtered out of the "WikiText" variable
            punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

            #For loop runs through WikiText
            for word1 in WikiText:

                #If word1 is in "punc", it will be replaced with nothing and saved back to "WikiText"
                if word1 in punc:
                    WikiText = WikiText.replace(word1,"")


            #"WikiText" is broken down into tokens and saved to "W_Token" variable
            #Stop words are saved to "S_Words"
            #"W_Token" and "S_Words" are checked against each other and put into the "Filter_One" variable if "W_Token" is not in "S_Words"
            W_Token=word_tokenize(WikiText)
            S_Words=set(stopwords.words("english"))
            Filter_One = [w for w in W_Token if not w.lower() in S_Words]

            #"Filter_One" has all of its words turned lowercase and saved to "Filter_Two" variable
            #The Counter Method is than used which counts all of these words and saved to the "Counter_Filter" variable
            #.most_common(5) method is called on "Counter_Filter" which prints the top five most mentioned words from most to least and saves to "Occurence_Filter" Variable
            Filter_Two=map(lambda x:x.lower(), Filter_One)
            Counter_Filter = Counter(Filter_Two)
            Occurence_Filter = Counter_Filter.most_common(5)

        #"Occurence_Filter" is printed and so is a star line
        #WikiText is then reset to an empty string before continuing loop
        print('"'+heading.span.text+'"',"Most Used Words: ",Occurence_Filter)
        print("***************************************************************************************")
        WikiText=""