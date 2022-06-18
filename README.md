# Movies Recommender System

A recommender system for a movie dataset.

## About

This is a test on building a recommender systems, given a dataset of movies and their ratings. The project was inspired by [this video](https://www.youtube.com/watch?v=eyEabQRBMQA) from [Dataquest](https://www.youtube.com/c/Dataquestio), give him some love. ❤️

The project consists of the recommender system and an API for querying recommendations using Flask, the main way to interact with the recommender is querying the endpoint `/recs` with a movie title to query as an input. Example:

```sh
curl -X GET 'http://localhost:8081/recs?title=Batman'
```

This should output a JSON in the terminal with an array of object of the following schema:

```ts
type Recommendation = {
  id: number
  score: number
  title: string
  genres: string[]
}
```

The server is set to start on port 8081 by default, you can change the port to run on any other one by changing the `app.run(port=<port>)` call in the `main.py` file.

## Requirements

- [Movies dataset](https://files.grouplens.org/datasets/movielens/ml-25m.zip)
- Python >= 3.8
- PIP

## How to install

To be able to run the server, you'll have to install the dependencies first, in your terminal, type the following code to install them:

```sh
$ pip install -r requirements.txt
```

## How to run

To be able to run, first download the [dataset](https://files.grouplens.org/datasets/movielens/ml-25m.zip) and unzip it into the root folder, after that, you can just type:

```sh
python src/main.py
```

And the server will start. 😸

## Author

| ![Eder Lima](https://github.com/asynched.png?size=100) |
| ------------------------------------------------------ |
| [Eder Lima](https://github.com/asynched)               |

## Resources

- [Dataquest - Build a movie recommendation system with Jupyter and Pandas: Data Project](https://www.youtube.com/c/Dataquestio)
