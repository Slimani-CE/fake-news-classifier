# Fake News Classifier

## About the Dataset
The dataset used in this project is from the Kaggle competition "Fake News." It contains news articles with the following attributes:
1. id: Unique id for a news article
2. title: The title of a news article
3. author: Author of the news article
4. text: The text of the article; could be incomplete
5. label: A label that marks whether the news article is real or fake (0 = Fake news, 1 = Real news)

[Link to dataset](https://www.kaggle.com/c/fake-news/data?select=train.csv)

## Libraries
  ![Numpy](https://img.shields.io/badge/Numpy-007396?style=for-the-badge&logo=numpy&logoColor=white)
  ![Pandas](https://img.shields.io/badge/Pandas-007396?style=for-the-badge&logo=pandas&logoColor=white)
  ![NLTK](https://img.shields.io/badge/NLTK-Natural%20Language%20Toolkit-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white)
  ![regex](https://img.shields.io/badge/RE-RegEx-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white)
  ![SKLEARN](https://img.shields.io/badge/sklearn-007396?style=for-the-badge&logo=scikit-learn&logoColor=white)

## Data Pre-processing
Data pre-processing steps are performed to clean and transform the dataset. Null values are replaced with empty strings, and the title, author, and text columns are merged into a single column called 'content'. The text is then processed using stemming and removing stopwords.

## The Model 
A Logistic Regression model is trained using the training set.

## Contributing
Contributions are always welcome! If you find any issues with the code or have suggestions for improvements, please feel free to submit a pull request.

Just remember, we are not responsible for any broken keyboards or late-night coding sessions that may result from your contributions! 😄

## Show Your Support
If you found this notebook helpful, please give it a ⭐️ to show your support!
