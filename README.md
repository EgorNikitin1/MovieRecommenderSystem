# Movie Recommender System
This service helps users find interesting movies based on their preferences. The CountVectorizer algorithm from the scikit-learn library is used as the basis for recommendations. The data for model development is obtained from an extensive dataset on the [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata). The user interface is based on the FastAPI web framework.
## Tech
 * Python
 * NumPy
 * Pandas
 * MatPlotLib
 * Seaborn
 * Scipy
 * Scikit-learn
 * FastAPI
## How to run
Build docker container:
```shell
docker build -t movie_recommendation_system .
```
Run docekr container:
```shell
docker run -p 80:80 movie_recommendation_system
```
Enter: localhost:80
