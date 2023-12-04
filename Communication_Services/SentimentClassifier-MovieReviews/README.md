# Sprint Project 05
> Sentiment Analysis on Movies Reviews

## The Business problem

This project is related to NLP. As you may already know, the most important and hardest part of an NLP project is pre-processing, which is why we are going to focus on that.

Basically this is a basic sentiment analysis problem, as in this case, consists of a classification problem, where the possible output labels are: `positive` and `negative`. Which indicates, if the review of a movie speaks positively or negatively. In our case it is a binary problem, but one could have many more "feelings" tagged and thus allow a more granular analysis.

## About the data

In this project, we will work exclusively with two files: `movies_review_train_aai.csv` and `movies_review_test_aai.csv`.

You don't have to worry about downloading the data, it will be automatically downloaded from the `AnyoneAI - Sprint Project 05.ipynb` notebook in `Section 1. Get the data`.

This is a dataset for **binary sentiment classification**.

## Technical aspects

To develop this Machine Learning model you will have to primary interact with the Jupyter notebook provided, called `AnyoneAI - Sprint Project 05.ipynb`. This notebook will guide you through all the steps you have to follow and the code you have to complete in the different parts of the project, also marked with a `TODO` comment.

## Install

A `requirements.txt` file is provided with all the needed Python libraries for running this project. For installing the dependencies just run:

```console
$ pip install -r requirements.txt
```

*Note:* We encourage you to install those inside a virtual environment.

## Run Project

It doesn't matter if you are inside or outside a Docker container, in order to execute the project you need to launch a Jupyter notebook server running:

```bash
$ cd project
$ jupyter notebook
```

Then, inside the file `AnyoneAI - Sprint Project 05.ipynb`, you can see the project statement, description and also which parts of the code you must complete in order to solve it.

## Code Style

Following a style guide keeps the code's aesthetics clean and improves readability, making contributions and code reviews easier. Automated Python code formatters make sure your codebase stays in a consistent style without any manual work on your end. If adhering to a specific style of coding is important to you, employing an automated to do that job is the obvious thing to do. This avoids bike-shedding on nitpicks during code reviews, saving you an enormous amount of time overall.

We use [Black](https://black.readthedocs.io/) for automated code formatting in this project, you can run it with:

```console
$ black --line-length=88 .
```

Wanna read more about Python code style and good practices? Please see:
- [The Hitchhiker’s Guide to Python: Code Style](https://docs.python-guide.org/writing/style/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

## Tests

We've added some basic tests to `AnyoneAI - Sprint Project 05.ipynb` that you must be able to run without errors in order to approve the project. If you encounter some issues in the path, make sure to be following these requirements in your code:

- Every time you need to run a tokenizer on your sentences, use `nltk.tokenize.toktok.ToktokTokenizer`.
- When removing stopwords, always use `nltk.corpus.stopwords.words('english')`.
- For Stemming, use `nltk.porter.PorterStemmer`.
- For Lematizer, use `Spacy` pre-trained model `en_core_web_sm`.

We provide unit tests along with the project that you can run and check from your side the code meets the minimum requirements of correctness needed to approve. To run just execute:

```console
$ pytest tests/
```

If you want to learn more about testing Python code, please read:
- [Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/)
- [The Hitchhiker’s Guide to Python: Testing Your Code](https://docs.python-guide.org/writing/tests/)
