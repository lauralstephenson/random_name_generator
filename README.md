App Use
Before getting into the process of making this app, I want to explain how to use the GUI. Run main.py, and press the button to get eight random names.
There are both first and last names. Feel free to pick and choose what sounds good for you from the list.  
These can be used for stories, games, and the like. These are all human names. Drop or add letters to make them scifi.

Process
First, I downloaded the publicly available database for all first names for the USA 1880-2022, which contain both female and male names.
Why the USA and why from so far back? People in the USA speak 350 languages and come from every country in the world, so this is a fair represenatation
of worldwide names. Also, names fall in and out of favor, and any name might be interesting to an author. Also, this way I came up with over one million names.

Why surnames from 2010? This is a mix of names from all over the USA, including First Nations names. Surnames do change over time, but not that much. 
I also wanted information from when immigration wasn't as curtailed. New groups with new surnames come to the USA over the centuries. 

Using a Jupyter notebook, I used pandas and numpy to merge the yearly files, delete duplicates, remove extraneous information, 
and separate them into male and female files. 

Then I went to Wikipedia and found lists of agendered names, plus I am a writer and have seen many names and nicknames. I added quite a few to this 
database and claened it up. As a novelist, I need a mix of male, female, and "cool" names for my characters, especially when writing strong characters.

Then I moved to main.py and used Tkinter to make a GUI for a person to press a button to get three female, three male, and two "cool" names. 

I hope that you find this app useful.

Retrieved some data from https://en.wikipedia.org/wiki/Unisex_name
Retrieved first name census data from https://www.archives.gov/research/census/online-resources. I only went back to 1880.
Retrieved last name census data from 2010 from https://www.census.gov/topics/population/genealogy/data/2010_surnames.html.
