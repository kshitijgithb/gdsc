from flask import Flask, render_template, request
import pickle
import numpy as np
import support as waterpd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

yes = "https://fitpage.in/wp-content/uploads/2021/02/Article_Banner-1-10.jpg"
yes1 = "Water is safe and Drinkable💧"
noo = "https://v3.cdnpk.net/videvo_files/video/premium/partners0067/thumbnails/BB_2d1fd848-635c-4ef1-b07f-9db6fc7ed10a_large.jpg"
noo1 = "Water is Not safe for Drinking🚱"


@app.route('/')
def hello_world():
    return render_template("index.html", val1="https://watercureusa.com/wp-content/uploads/image-free-water-testing.png")

@app.route('/', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
      int_features=[x for x in request.form.values()]
      finalarray=[np.array(int_features)]
      # print(finalarray)
      finalarray = waterpd.input(finalarray)
      prediction = model.predict(finalarray)
      res = prediction[0]
      ans = noo
      ans1 = noo1
      if res == 1:
        ans = yes
        ans1 = yes1
      return render_template('index.html',pred=ans1, val1=ans)

    else:
        return render_template("index.html", val1="https://watercureusa.com/wp-content/uploads/image-free-water-testing.png")


if __name__ == "__main__" :
    app.run(debug=True)