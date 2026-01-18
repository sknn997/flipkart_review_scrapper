import logging
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs
from flask import Flask ,request,render_template,jsonify
logging.basicConfig(filename='scrapper.log',level=logging.INFO)
import pymongo
import csv

headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/140.0.0.0 Safari/537.36"
    }

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def homepage():
    return render_template('index.html')
    
    
@app.route('/review',methods=['POST','GET'])
def index():
    if request.method=='POST':
        try:
            searchString=request.form['content'].replace(' ','-')
            url='https://www.flipkart.com/search?q='+searchString
            page_details=uReq(url).read()
            beauty_page=bs(page_details,'html.parser')
            boxes=beauty_page.findAll('div',{'class':'lvJbLV col-12-12'})
            del boxes[0:2]
            page_url='https://www.flipkart.com'+boxes[0].div.div.div.a['href']
            page_html=requests.get(page_url)
            page_html.encoding='utf-8'
            b_page_url=bs(page_html.text,'html.parser')
            comments=b_page_url.find_all('div',{'class':'col MDzIYy'})
            review_link=comments[0].a['href']
            all_reviews_link='https://www.flipkart.com'+review_link
            all_reviews_html=requests.get(all_reviews_link)
            all_reviews_html.encoding='utf-8'
            b_reviews_url=bs(all_reviews_html.text,'html.parser')
            overall_html=b_reviews_url.find_all('div',{'class':'CFqdv6'}) 
            overall_link=overall_html[0].a['href']
            final_link='https://www.flipkart.com'+overall_link
            final_html=requests.get(final_link)
            final_html.encoding='utf-8'
            b_final_url=bs(final_html.text,'html.parser')
            final_call=b_final_url.find_all('div',{'class':'lvJbLV col-12-12'})
            del final_call[0:4]

            reviews=[]

            for review in final_call:
                name_tag = review.find("div", class_="row f6dnIR")
                spans = name_tag.find_all("span") if name_tag else []
                reviews.append({
                    'Product':searchString,
                    "Name": name_tag.p.text.strip() if name_tag and name_tag.p else None,
                    
                    "Location": spans[1].text.strip()[2:] if len(spans) > 1 else None,
                    
                    "Rating": review.find("div", class_="MKiFS6").text.strip()
                              if review.find("div", class_="MKiFS6") else None,
                    
                    "Comment": next(
                         (d.text.strip() for d in review.find_all("div")
                          if d.get("class") == [] and d.text.strip()),
                         None       
                        )
                })

            
            filename = searchString + ".csv"
            with open(filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Product", "Name", "Location", "Rating", "Comment"])
                for r in reviews:
                    writer.writerow([
                        r["Product"],
                        r["Name"],
                        r["Location"],
                        r["Rating"],
                        r["Comment"]
                        ])
        
            
            client=pymongo.MongoClient('mongodb+srv://sknn98885:sknn98885@cluster0.nlozl.mongodb.net/?appName=Cluster0')
            db=client['flipkart_reviews']
            review_col=db['flipkart_reviews']
            review_col.insert_many(reviews)
        
        except Exception as e:
            logging.info(e)
    
            
                
    return render_template('result.html',reviews=reviews[0:(len(reviews)-1)])
        


if __name__=='__main__':
    app.run(host='0.0.0.0')