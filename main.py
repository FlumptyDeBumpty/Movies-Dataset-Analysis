#import libraries
import streamlit as st
import pandas as pd
from PIL import Image
import warnings

warnings.filterwarnings("ignore")

st.title("Movies Dataset Analysis")

st.write(
  "Isaac: 14 years old and going into 8th grade, learned Scratch in 6th and learned Python in 7th, and has recreated Five Nights at Freddy's in Scratch."
)
st.write(
  "Caleb: Going to my last year of school in 12th grade at 16 years old. I don't know much about coding, but I know everything that has to do with drawing and other hands on art."
)
st.write(
  'John Stanley: Going into 8th grade this year, has used Python and Scratch before, has some knowledge on how to use Python prior to this class.'
)
st.write(
  "Philip: going to 5th grade has learned abit about coding in 4th and 3rd and is still learning mor how to code tried to make a roblox game failed and lost the account."
)
st.write(
  "Devon: Going in to 8th grade knows small bits of how to use scratch and has made 3 or 4 roblox games. "
)
st.write(
  "John D: Going into 8th grade, experienced with scratch and enjoys coding in python."
)

st.header("Context - Written by Isaac")

st.write(
  "This is where we will analyze a dataset full of information about popular movies, as well as creating graphs and other plots in order to display information, as well as possible correlations between particular types of data."
)

st.header("Exploratory Data Analysis")

image = Image.open('Top 10 Actors.png')

st.image(
  image,
  caption=
  'The Top 10 actors based on how many Movies they have starred in. (Taken by Isaac)'
)

st.write(
  "This graph shows us that movies that Robert De Niro, Mel Gibson, and Tom Hanks star in have a tendency to score high score. "
)

image = Image.open('Top 10 Directors.png')

st.image(
  image,
  caption=
  'The Top 10 directors based on how many movies they have directed. (Taken by Isaac)'
)

st.write(
  "This graph shows us that movies that Woody Allen, Clint Eastwood, and Barry Levinson have directed tend to have a high score."
)

image = Image.open('Top 25 Movies.png')

st.image(image,
         caption='The top 25 movies based on their score. (Taken by Isaac)')

st.write(
  "This graph shows us that The Shawshank Redemption, Pulp Fiction, and Schindler's List are the best scored movies."
)

image = Image.open('Top 25 Movies Gross.png')

st.image(
  image,
  caption='The top 25 movies based on their gross income. (Taken by Isaac)')

st.write(
  "This graph shows us that Titanic, The Lion King, and Jurassic Park brought in the largest amount of money."
)

image = Image.open(
  'Web capture_13-7-2023_11641_colab.research.google.com.jpeg')

st.image(image, caption='Top 10 Movies Based on Budget. (By Caleb)')

image = Image.open('Top 25 Movies.png')
st.write(
  image,
  caption=
  'top 25 movies based on their buget scores starring monsters inc. as the lowest score spy game as 3rd lowest and titanic as highest score. '
)
image = Image.open('Project.png')

st.image(image, caption='Top 25 Movies Based on Mean Score')

st.write(
  "This graph shows us that history movies were the most popular based on their mean score."
)
st.write(
  "Titanic took the most amount of money for their movie which was about 200m. And the lowest was monsters inc. which was at leat 120m "
)

image = Image.open('project 2.png')

st.image(image, caption='Top 25 Movies Sorted by Score')

st.write(
  "This graph shows that The Shawnshank Redemption was the highest scored movie in the top")

  

st.header("Conclusion - By Isaac")

st.write(
  "In conclusion, there are many popular movies, actors, and directors, but some do manage to stand out, and manage to be better than the rest. For example, Robert De Niro's movies score very high ratings, most likely because of his great acting skills. As well, movies that Woody Allen directs also score very high ratings, as he must be very talented in his field of work. This data is capable of showing directors what the average viewer will likely want to see next, allowing them to accurately guess the next big hit."
)
