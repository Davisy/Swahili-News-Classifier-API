import requests as r

# sample news article
news = "Mshambuliaji wa Chelsea Romelu Lukaku amehusishwa na kurejea katika klabu yake ya zamani Inter Milan lakini mchezaji huyo wa kimataifa wa Ubelgiji mwenye umri wa miaka 28 anataka kusalia na kupigania nafasi yake Stamford Bridge. (Mirror)"


# make prediction
keys = {"news": news}
prediction = r.get(
    "https://limitless-forest-00896.herokuapp.com/news-prediction/", params=keys
)

# collect and print the result
results = prediction.json()
print(results["prediction"])
print(results["Probability"])

