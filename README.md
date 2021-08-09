# Recipe Ingredient Classifier

This is my [Udacity Machine Learning Engineer Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t) Capstone Project.

I implemented a Named-Entity Recognition (NER) machine learning model to identify different parts in the
description of an ingredient, in other words: when given "100 g flour", the model should recognize
100 as quantity, g as unit of measurement and flour as ingredient name and label them as such.

In the **docs** folder you'll find two documents:

- **project-report**: A project report addressing the five major project development stages and detailed 
  information about the implementation.
- **proposal.pdf**: A project proposal addressing seven key points before starting developing of the project.

## Prerequisites

- Python 3.6

Note: I used above version of python to develop this classifier. You can probably use a newer version, but I cannot
guarantee that the code will work in that case.

## Installation

In order to get the code to run locally you need to follow these steps:

- Download the code
- Create a python virtual environment, in order to install the dependencies for this particular project
- Install jupyterlab, in order to be able to run the jupyter notebooks.
- Run Jupyter Lab

```bash
git clone https://github.com/y-garcia/recipe-ingredient-classifier
cd recipe-ingredient-classifier
python -m venv venv
venv\Scripts\activate.bat
pip install jupyterlab
jupyter lab
```

Alternatively you can create a new AWS Sagemaker notebook instance and enter the repository address in the setup.
This is how I developed the code, so try that if you want to avoid the hustle of setting it all up locally.
Take into consideration that it may incur some costs running the notebooks.
If you go this route **DON'T FORGET TO STOP THE NOTEBOOK INSTANCE AFTER YOU ARE DONE**, otherwise it will run forever
and you will get an unpleasant surprise in the bank account at the end of the month.

## Usage

There are 3 main notebooks:

- 01_data_exploration: here I take you through the data.
- 02_benchmark: here we use an existing model to compare our implementation with.
- 03_implementation: here is the actual implementation of the model.

Steps:

1. Open the first notebook: **01_data_exploration**. 
    - Go to menu **Run** > **Run All Cells**. This shouldn’t take long.
    - You can then go through the notebook to learn more about the data we are building our model on.
    

2. Open the second notebook: **02_benchmark**.
    - Go to menu **Run** > **Run All Cells**. This should take about **5 minutes**,
      since we are not training the model but loading the trained model from disk.
    - You can then go through the notebook which will guide you through the benchmark. 
      **Note**: Comments prefixed with “**Author**” are the original comments from the article.
      Comments prefixed with “**Yeray**” are my own.


3. Open the third notebook: **03_implementation**.
    - Go to menu **Run** > **Run All Cells**. This will take about **10-15 minutes**,
      since it will train the model from scratch, so take that into consideration.
    - You can then go through the notebook which will guide you through the implementation details.
    
## Contributing

This project is for learning purposes, so contributing is not desired at the moment.
You may fork this project and build upon it on your profile if you wish.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available,
see the [tags on this repository](https://github.com/y-garcia/recipe-ingredient-classifier/tags).

See the [CHANGELOG.md](CHANGELOG.md) file for details. 

## Authors

* **Yeray García Quintana** | [y-garcia](https://github.com/y-garcia)

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
See the [LICENSE.md](LICENSE.md) file for details.
