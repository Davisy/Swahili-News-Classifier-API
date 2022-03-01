# import packages

from os.path import dirname, join, realpath
import joblib
import uvicorn
from fastapi import FastAPI

app = FastAPI()

# load the model and count_vectorizer

with open(
    join(dirname(realpath(__file__)), "model/news_classification_model.pkl"), "rb"
) as f:
    model = joblib.load(f)

with open(
    join(dirname(realpath(__file__)), "preprocessing/count_vectorizer.pkl"), "rb"
) as f:
    vectorizer = joblib.load(f)

topics = {0: "Kitaifa", 1: "michezo", 2: "Biashara", 3: "Kimataifa", 4: "Burudani"}


@app.get("/")
def home():
    return {"A simple API to predict news topics in swahili Language"}


@app.get("/news-prediction/")
def predict_topic(news: str):
    """
	A simple function that receive a news content and predict the topic of the content.
	:param news:
	:return: prediction, probabilities
	"""

    # transform the input
    transformed_news = vectorizer.transform([news])

    # perform prediction
    prediction = model.predict(transformed_news)
    output = int(prediction[0])
    probas = model.predict_proba(transformed_news)
    output_probability = "{:.2f}".format(float(probas[:, output]))

    return {"prediction": topics[output], "Probability": output_probability}


# run the app
uvicorn.run(app, host="127.0.0.1", port=8000, debug=True)

