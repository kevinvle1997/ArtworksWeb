# ArtworksWeb


![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

ArtworksWeb is a website written in python, HTML, CSS and utilizes the PostgreSQL to store art related data.


# New Features!

  - updated graphics on the website


And of course ArtworksWeb itself is open source with a public repository
 on GitHub.

### Installation

ArtworksWeb requires Flask, SQLAlchemy, and PostGreSQL to run!

### Background

Front-end work is primarily done by Jenny, Saideep, and Brendan. We focused on a sleek black and white design with few accents and an easy to read font. The design emphasizes easy navigation and is subtle on the eyes. We attempt to intrigue users by cycling through images of museums in the collection on the splash page. Javascript, a client-side scripting language, was used to implement front-end functionality. CSS was used throughout the design process both internally and externally, primarily to adjust the size and color of images and other items on the webpages. Bootstrap, an open-source CSS framework, was used extensively to implement design features such as the navigation bar at the top of every page, buttons, the carousel of images on the splash page, and the tables for displaying data.

The back-end work is primarily done by Sungho and Kevin. Python was used to implement the logic of the code, including data processing. The microframework Flask was used alongside python to design this project alongside various python packages. Files are read in by an imported python library CSV and converted into a workable format. As shown in Figure 2, each component has several important attributes, such as title, date, museum_ID, etc. Most notably, a big change that we had to make was clean up the artwork data. Since an artist can supply artwork to multiple museums, the artwork needed a way to convey which museum it belongs to. To solve this issue, we added museum_ID to the end of the Artwork_ID in the data. So, in the tables shown when the user enters the artworks page, they will be able to see which museum the artwork was from. In the second stage of the project, We scraped the information we needed from the online repos that the Museums posted and stored them inside a dictionary for later usage. We then parsed the information from the dictionary into Models and sent them into SQL databases to then use for our website. One of the biggest challenges we faced was to make the information scraped from the different repo's into one uniform model, as there is a multitude of differences from each data source. In short, since the data from the three museums is coming from different sources, they are formatted differently and thus, needs to be cleaned and organized. Hosting The website will be hosted through the Google Cloud Platform through the app engine. Google Cloud Platform is a suite of cloud computing services and App Engine is a platform for developing and hosting web applications. We can build applications using popular and familiar languages (Python, in this case) and focus on the coding aspect of our project while App Engine manages the infrastructure aspect. In order to set up the Google Cloud Platform to deploy the website, we will have to first create a project on App Engine. We need to make sure that we have an app.yaml file within our folder and then navigate to the Google Cloud Shell to clone our repo with our application files. $gcloud app deploy will be used to deploy the website. After a successful deployment, we will receive a link to navigate to our application.