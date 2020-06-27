from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import json
import numpy as np
import random
import tensorflow as tf
import keras
import pickle
import os
from engine import get_recommendations
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

app = Flask(__name__)


# Config MySQL
mysql = MySQL()
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'botto'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize the app for use with this MySQL class
mysql.init_app(app)


# Chat
with open('intents.json') as json_data:
    intents = json.load(json_data)

data = pickle.load( open( "data.pickle", "rb" ) )
words = data['words']
classes = data['classes']

def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                
    return(np.array(bag))
   

model = keras.models.load_model("model.pkl")

# Bargain 

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def top(self):
         return self.items[len(self.items)-1]
     def prev(self):
         return self.items[len(self.items)-2]    
     def next(self):
         return self.items[len(self.items)-3]     

     def size(self):
         return len(self.items)
userStack =Stack()
botStack= Stack()



@app.route('/')
def fn():
    return render_template('landingpage.html')

@app.route('/allproducts')
def index():
    
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    cur.execute("SELECT * FROM products ORDER BY id DESC ")
    allproduct = cur.fetchall()
    
    # Close Connection
    cur.close()
    return render_template('allproducts.html', allproducts=allproduct)

@app.route('/<name>', methods=['GET', 'POST'])
def cars(name):
    global flag
    flag=0
    for j in range(0,userStack.size()):
        userStack.pop()
    for k in range(0,botStack.size()):
        botStack.pop()

    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    values = name
    cur.execute("SELECT * FROM products WHERE brand=%s ORDER BY id ASC", (values,))
    products = cur.fetchall()
    # Close Connection
    cur.close()

    if 'view' in request.args:
        product_id = request.args['view']
        curso = mysql.connection.cursor()
        curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
        q = curso.fetchall()
        for row in q:
            global p_name
            p_name=row['pName']
            global price
            price=row['price']
            global mini
            mini=row['mini']
        userStack.push(price) 
        global quantity
        quantity=0
        return render_template('view_product.html',  details=q)
        
    else:
        return render_template('products.html', toys=products, values=name)


@app.route("/get")
def chat():
    userText = request.args.get('msg')
    res=0
    global mini
    global quantity
    global flag
    global discount
    global price
    global p_name
    global accepedPrice
  
    while True:
        for i in userText.split():
            if i.isdigit():
             res = i

        for i in userText.split():
            if i=="accept":
                return "congrats on your deal. I will email you the link to purchase. "
            elif i=="reject":
                randomresponse1 = ["I understand. What do you offer, then?","What could make it work, then?","Fair enough, what's your counter offer","Ok, what’s your counter offer?","Hit me with your best shot!","Make me an offer I can’t refuse!" ]
                return random.choice(randomresponse1)

        if res == 0:
            input_data = pd.DataFrame([bow(userText, words)], dtype=float, index=['input'])
            results = model.predict([input_data])[0]
            results_index = np.argmax(results)
            tag = classes[results_index]

            if results[results_index] > 0.5:
  
                for tg in intents["intents"]:
                    if tg['tag'] == tag:
                        responses = tg['responses']
              
                responce= random.choice(responses)
                return responce
            else:
                return("i didn't understand. try something else. ")

        elif quantity==0:
            if int(res) < 10 and int(res)>0:
                quantity=int(res)
                if quantity <= 1:
                    discount = 7
                elif quantity==2:
                     discount = 9
                else:
                    discount = 10
                nextOffer = price-(price * (discount/100))
                botStack.push(nextOffer)    

                return "How much are you willing to offer per unit ?" 
            else:
                return "Please enter a quantity "
            
        else:
            hisOffer = int(res)
            if(flag == 0):
                

                if(hisOffer<mini):
                    rejectResponse=["Im here to make deals and not to give out items just like that ! Please make a higher offer ","I'd be at loss if i accept that price. Please make a higher offer","That's less than the price we got it for. Please make a higher offer"]
                    return random.choice(rejectResponse)

                if((botStack.size()<4) & (hisOffer<botStack.top())):
                    if((userStack.size()>1) & (hisOffer<userStack.top())):
                        rejectResponse=["That's less that what you previously offered... Here's my offer ","Hey now, I can play silly games too, here’s my offer ","That’s a worse offer than the one you have made earlier… here’s my offer: "]
                        discount = discount-4
                        botStack.push(price-(price * (discount/100)))
                        counterOffer=  random.choice(rejectResponse) + str(botStack.top()) + "?" 
                        somehtml='<div style="z-index:100;display:flex" ><input class="btn" style="background-color:#4CAF50;" id="accept" type="submit" placeholder="accept" value="accept" onclick="return getAccepted();"> <input class="btn" id="reject" style="background-color:#f44336;" type="submit" placeholder="reject" value="reject" onclick="return getRejected();"> </div>'
                        return '{} {}'.format(counterOffer, somehtml)

                    else:    
                        userStack.push(hisOffer)
                        rejectResponse= ["Thats too less. I can do ", "Nope. Won't do. How about ","My boss said we can’t do it, however we can do ","I can't except that deal, how about "]
                        discount= discount+3
                        counterOffer = random.choice(rejectResponse) + str(botStack.top()) + "?" 
                        botStack.push(price-(price * (discount/100))) 
                        somehtml='<div style="z-index:100;display:flex" ><input class="btn" style="background-color:#4CAF50;" id="accept" type="submit" placeholder="accept" value="accept" onclick="return getAccepted();"> <input class="btn" id="reject" style="background-color:#f44336;" type="submit" placeholder="reject" value="reject" onclick="return getRejected();"> </div>'
                        return '{} {}'.format(counterOffer, somehtml)

                elif(hisOffer>botStack.top()):
                    userStack.push(hisOffer)
                    accepedPrice= hisOffer
                    return "Congrats! We have a deal. I will email you the link to purchase. "

                else:
                    userStack.push(hisOffer)
                    discount = discount + 3
                    botStack.push(price-(price * (discount/100)))
                    if(hisOffer>botStack.top()):
                        return "Congrats! We have a deal. I will email you the link to purchase. "
                    flag=1
                    counterOffer="Sorry, I can’t accept that deal. We’ve been bargaining for a while and I can see that you are a tough negotiator. So here's my final offer of " + str(botStack.top()) +""
                    somehtml='<div style="z-index:100;display:flex;" ><input class="btn" style="background-color:#4CAF50;" id="accept" type="submit" placeholder="accept" value="accept" onclick="return getAccepted();"> <input class="btn" id="reject" style="background-color:#f44336;" type="submit" placeholder="reject" value="reject" onclick="return getRejected();"> </div>'
                    return '{} {}'.format(counterOffer, somehtml)


            elif(flag==1):
                if(hisOffer>botStack.top()):
                    return "Congrats! We have a deal. I will email you the link to purchase. "
                #email()
                result_final = get_recommendations(p_name)
                names = []
                pictures = []
                ids = []
                brands=[]
                prices = []
                for i in range(len(result_final)):
                    if result_final.iloc[i][4] <price:
                        names.append(result_final.iloc[i][0])
                        pictures.append(result_final.iloc[i][1])
                        ids.append(result_final.iloc[i][2])
                        brands.append(result_final.iloc[i][3])
                        prices.append(result_final.iloc[i][4])
                if not names:
                    return "That was my last offer, however i will check with my boss and get back to you on email"
                else:
                    cards=''        
                    for m in range(len(names)):
                        card= '<div class="card mb-4"> <a href="/'+brands[m] +'?view='+str(ids[m]) +'">'+'<div class="card-img-top" ><img style="width:15vw; height: 10vw;" src="static/image/product/' +brands[m] +'/' +pictures[m] +' "> </img> </div></a><div class="card-body"><a class="card-title" href="/'+brands[m] +'?view='+str(ids[m])+'">'+names[m] +'</a> <p> Rs '+str(prices[m])  +' </p></div></div>'
                        cards+=card     
                    someHtml='<div style="z-index:100;display:flex;width:min-content" >'+cards  +'</div>'
                    resp="That was my last offer, however you could check out these similar products in your budget"
                        
                return '{} {}'.format(resp, someHtml)       

'''                
def email():
    message = Mail(
        from_email='Botto@toycars.com',
        to_emails='julianathayil@gmail.com',
        subject='Heres my final offer',
        html_content='<center> <h1>Still thinking about it? </h1> <h4> Here is my final offer</h4></center><br> <span><img width="400px" height="200px" src="https://drive.google.com/uc?id=1WpN-8dJ7iomFT4znizFvkMSqEWjgvpLL"> </img> <h3>Subaru Impreza 22B STi </h3> <h3>Offer price = Rs 513 </h3> </span>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(str(e))
'''
    
if __name__ == "__main__":
    app.run()
    global flag
    global discount
    global p_name
    global quantity
    global price
    global accepedPrice
    global mini