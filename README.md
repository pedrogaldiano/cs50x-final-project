
# Workout Generator

#### Video Demo: [Video link here](https://youtu.be/MyY3GI8R1aI)
#### Description: 
Workout  an application capable of Generate a workout program by  
choosing "randomly" the exercises for each muscle group defined by some filters.

[image1](/workout-creator/"print-home.png")
[image2](/workout-creator/"print-workout-predefined.png")
[image3](/workout-creator/"print-workout-personalized.png")

------------------------
### IMPORTANT:
At first, I tried to get the data web scrapping the ExRx.net (they have a huge database, with more than 1800 exercises).  
But they prohibit any type of copying or scrapping of their content. So I decided to use the [open source project in git hub from davejt](https://github.com/davejt/exercise).  
I choose to not use the API since the most crucial part of the data I can get from a CSV file.  


## Development process:

#### 1° Get the data from an open source
* Get the [exercise database](https://github.com/davejt/exercise) in CSV ==== [OK]  
* Create a SQLite relatioal database with the data from the CSV file ==== [OK]  
I'm not that this data set so small really needed a relational database, but was nice to do it...  

#### 2° Choose the exercises based on something simple
* Create the python program to pick the exercises ==== [OK]  
* You can generate a unique set of exercises within one of thoose routines: Full Body, Push/Pull, and Push/Pull/Legs ==== [OK]  

#### 3° Create a web application (so you can actually show everything)
* Use Flask to run the web application ==== [OK]  
* Create the index.html ==== [OK]  
* Create a style.css  ==== [OK]  
* Make it mobile-friendly ==== [OK]  

#### 4° Create the page where you show the exercises
* Create the workout.html ==== [OK]  
* Create a dinamic table ==== [OK]  
* Make every exercise name a link  ==== [OK]  

#### 5° Add new features and solve bugs
* Bugs in the index.html ==== [OK]  
* Make the html files be more dynamic and less hardcoded ==== [OK]  
* Allow the user to use checkboxes rather than radio inputs to choose the predfined routines ==== [OK]  
* Allow the user to select the muscles he or she want to workout and how many exercises for each muscles ==== [OK]  
* Fix bugs in the helpers ==== [OK]  
* Fix some more bugs... ==== [OK]   
  