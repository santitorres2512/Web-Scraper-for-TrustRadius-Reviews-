#import bs4
#from urllib.request import urlopen as uReq
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import csv
import time
#myurl = 'https://www.trustradius.com/voip?f=0#products'
#uClient = uReq(myurl)
#page_html = uClient.read()

req = Request('https://www.trustradius.com/voip?f=0#products', headers={'User-Agent': 'Mozilla/5.0'})
req1 = Request('https://www.trustradius.com/voip?f=25#products', headers={'User-Agent': 'Mozilla/5.0'})
req2 = Request('https://www.trustradius.com/voip?f=50#products', headers={'User-Agent': 'Mozilla/5.0'})
req3 = Request('https://www.trustradius.com/voip?f=75#products', headers={'User-Agent': 'Mozilla/5.0'})
req4 = Request('https://www.trustradius.com/voip?f=100#products', headers={'User-Agent': 'Mozilla/5.0'})
req5 = Request('https://www.trustradius.com/voip?f=125#products', headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()
webpage1 = urlopen(req1).read()
webpage2 = urlopen(req2).read()
webpage3 = urlopen(req3).read()
webpage4 = urlopen(req4).read()
webpage5 = urlopen(req5).read()


#Parse the HTML web page
pagesoup = soup(webpage, "html.parser")
pagesoup1 = soup(webpage1, "html.parser")
pagesoup2 = soup(webpage2, "html.parser")
pagesoup3 = soup(webpage3, "html.parser")
pagesoup4 = soup(webpage4, "html.parser")
pagesoup5 = soup(webpage5, "html.parser")


#Grabs each provider
Providers = pagesoup.findAll("div",{"class":"CategoryProduct_category-product-card__3s4Nq Card_card__2TQFx"})
Providers1 = pagesoup1.findAll("div",{"class":"CategoryProduct_category-product-card__3s4Nq Card_card__2TQFx"})
Providers2 = pagesoup2.findAll("div",{"class":"CategoryProduct_category-product-card__3s4Nq Card_card__2TQFx"})
Providers3 = pagesoup3.findAll("div",{"class":"CategoryProduct_category-product-card__3s4Nq Card_card__2TQFx"})
Providers4 = pagesoup4.findAll("div",{"class":"CategoryProduct_category-product-card__3s4Nq Card_card__2TQFx"})
Providers5 = pagesoup5.findAll("div",{"class":"CategoryProduct_category-product-card__3s4Nq Card_card__2TQFx"})


#document.querySelector("#product_card_list > div:nth-child(1) > div > div.CategoryProduct_logo__gijLT > a > div > img")
Amountofproviders = len(Providers)
Amountofproviders1 = len(Providers1)
Amountofproviders2 = len(Providers2)
Amountofproviders3 = len(Providers3)
Amountofproviders4 = len(Providers4)
Amountofproviders5 = len(Providers5)
'''
Provider = Providers[0]
Imageclass = Provider.findAll("div",{"class":"CategoryProduct_rating-count__2hxFa"})
Image = Imageclass[1].text
#URLlink = 'https://www.trustradius.com/'+str(Image)
print(Image)
'''

###### 1st page parsing#############

rows =[['VoIP Provider', 'Description','URL','Image logo URL','Amount of ratings','Amount of reviews','Most rated review','Pro','Contra','Integrations','Free Trial?','Support rating','App Score']]
for i in range(Amountofproviders):
    
    Provider = Providers[i]
    Title = Provider.div.div.div["title"]
    
    Descclass = Provider.findAll("div",{"class":"CategoryProduct_content__2ML8S"})
    Description = Descclass[0].div.text
    
    Imageclass = Provider.findAll("div",{"class":"CategoryProduct_logo__gijLT"})
    Image = Imageclass[0].div.img["src"]
    
    URLclass = Provider.findAll("h3",{"class":"CategoryProduct_heading-text__1snnq"})
    URL = URLclass[0].a["href"]
    URLlink = 'https://www.trustradius.com'+str(URL)
    
    Ratingamountclass = Provider.findAll("div",{"class":"CategoryProduct_rating-count__2hxFa"})
    RatingsAmount = Ratingamountclass[0].text
    
    Reviewamountclass = Provider.findAll("div",{"class":"CategoryProduct_rating-count__2hxFa"})
    ReviewsAmount = Reviewamountclass[1].text
    
    internalreq = Request(URLlink, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage = urlopen(internalreq).read()
    internalpagesoup = soup(internalwebpage, "html.parser")
    try:
        Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Scoreclass = internalpagesoup.findAll("span",{"itemprop":"ratingValue"})
        Score = Scoreclass[0].text
    except:
        Score = "No Score Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    try:
        Comment = internalpagesoup.findAll("div",{"class":"review-questions"})
    
        Commentclass = internalpagesoup.findAll("div",{"class":"not-edited question-text"})
        Review = Commentclass[0].text
    except:
        Review = "No Reviews Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    try:
        Prossection = internalpagesoup.findAll("ul",{"class":"pros"})
    
        #Prosclass = internalpagesoup.findAll("div",{"class":"not-edited question-text"})
        Pros = Prossection[0].li.text
        
        
        
        
    except:
        Pros = "No Pros Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    try:
        Conssection = internalpagesoup.findAll("ul",{"class":"cons"})
    
        #Prosclass = internalpagesoup.findAll("div",{"class":"not-edited question-text"})
        Cons = Conssection[0].li.text
        
        
        
        
    except:
        Cons = "No Cons Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    
    internalreq = Request(URLlink, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage = urlopen(internalreq).read()
    internalpagesoup = soup(internalwebpage, "html.parser")
    try:
        Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Scoreclass = internalpagesoup.findAll("span",{"itemprop":"ratingValue"})
        Score = Scoreclass[0].text
    except:
        Score = "No Score Found"
    
    
    URLlink2 = URLlink+str('#1')
    
    
    
    
    internal2req = Request(URLlink2, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage2 = urlopen(internal2req).read()
    internalpagesoup2 = soup(internalwebpage2, "html.parser")
    try:
        #Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Trialclass = internalpagesoup2.findAll("span",{"class":"answer"})
        #Trial1 = soup(Trialclass, "html.parser")
        #Trial2 = internalpagesoup2.findAll("span",{"class":"sprite sprite-featureSupported"})
        Trial = Trialclass[0].text
        
    except:
        Trial = "No Info Available"
    
    
    try:
        #Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Integrationsclass = internalpagesoup2.findAll("section",{"id":"integrations"})
        #Trial1 = soup(Trialclass, "html.parser")
        #Trial2 = internalpagesoup2.findAll("span",{"class":"sprite sprite-featureSupported"})
        Integrations = Integrationsclass[0].div.text
        
    except:
        Integrations = "No Info Available"
    
    URLlink3 = URLlink+str('#3')
    
    
    
    
    internal3req = Request(URLlink3, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage3 = urlopen(internal3req).read()
    internalpagesoup3 = soup(internalwebpage3, "html.parser")
    try:
        #Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Supportclass = internalpagesoup3.findAll("div",{"class":"rating-summary-block"})
        #Trial1 = soup(Trialclass, "html.parser")
        #Trial2 = internalpagesoup2.findAll("span",{"class":"sprite sprite-featureSupported"})
        Support = Supportclass[0]
        Supportstring = str(Support)
        String1 = Supportstring.split('qs=support-rating">',1)[1] 
        String2 = String1.split('</a></div></div><div class="rating-facet',1)[0] 
        Supportrating=String2[-3:]
    except:
        Supportrating = "No Info Available"
    
    
    
    rows.append([Title,str(Description),URLlink,Image,RatingsAmount,ReviewsAmount,Review,Pros,Cons,Integrations,Trial,Supportrating,Score])
    
    
    
    
    
    print('---------------------------------')
    print(URLlink)
    print('---------------------------------')
    print(Title)
    print('---------------------------------')
    print(Description)
    print('---------------------------------')
    print(Image)
    print('---------------------------------')
    print(RatingsAmount)
    print('---------------------------------')
    print(ReviewsAmount)
    print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
    


############### 2nd page parsing

for i in range(Amountofproviders1):
    
    Provider = Providers1[i]
    Title = Provider.div.div.div["title"]
    
    Descclass = Provider.findAll("div",{"class":"CategoryProduct_content__2ML8S"})
    Description = Descclass[0].div.text
    
    Imageclass = Provider.findAll("div",{"class":"CategoryProduct_logo__gijLT"})
    Image = Imageclass[0].div.img["src"]
    
    URLclass = Provider.findAll("h3",{"class":"CategoryProduct_heading-text__1snnq"})
    URL = URLclass[0].a["href"]
    URLlink = 'https://www.trustradius.com'+str(URL)
    
    Ratingamountclass = Provider.findAll("div",{"class":"CategoryProduct_rating-count__2hxFa"})
    RatingsAmount = Ratingamountclass[0].text
    
    Reviewamountclass = Provider.findAll("div",{"class":"CategoryProduct_rating-count__2hxFa"})
    ReviewsAmount = Reviewamountclass[1].text
    
    internalreq = Request(URLlink, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage = urlopen(internalreq).read()
    internalpagesoup = soup(internalwebpage, "html.parser")
    try:
        Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Scoreclass = internalpagesoup.findAll("span",{"itemprop":"ratingValue"})
        Score = Scoreclass[0].text
    except:
        Score = "No Score Found"
        
    try:
        Comment = internalpagesoup.findAll("div",{"class":"review-questions"})
    
        Commentclass = internalpagesoup.findAll("div",{"class":"not-edited question-text"})
        Review = Commentclass[0].text
    except:
        Review = "No Reviews Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    
    
    try:
        Prossection = internalpagesoup.findAll("ul",{"class":"pros"})
    
        #Prosclass = internalpagesoup.findAll("div",{"class":"not-edited question-text"})
        Pros = Prossection[0].li.text
        
        
        
        
    except:
        Pros = "No Pros Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    
    try:
        Conssection = internalpagesoup.findAll("ul",{"class":"cons"})
    
        #Prosclass = internalpagesoup.findAll("div",{"class":"not-edited question-text"})
        Cons = Conssection[0].li.text
        
        
        
        
    except:
        Cons = "No Cons Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    
    internal2req = Request(URLlink2, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage2 = urlopen(internal2req).read()
    internalpagesoup2 = soup(internalwebpage2, "html.parser")
    try:
        #Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Trialclass = internalpagesoup2.findAll("span",{"class":"answer"})
        #Trial1 = soup(Trialclass, "html.parser")
        #Trial2 = internalpagesoup2.findAll("span",{"class":"sprite sprite-featureSupported"})
        Trial = Trialclass[0].text
    except:
        Trial = "No Info Available"
    
    
    try:
        #Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Integrationsclass = internalpagesoup2.findAll("section",{"id":"integrations"})
        #Trial1 = soup(Trialclass, "html.parser")
        #Trial2 = internalpagesoup2.findAll("span",{"class":"sprite sprite-featureSupported"})
        Integrations = Integrationsclass[0].div.text
        
    except:
        Integrations = "No Info Available"
    
    
    
    URLlink3 = URLlink+str('#3')
    
    
    
    
    internal3req = Request(URLlink3, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage3 = urlopen(internal3req).read()
    internalpagesoup3 = soup(internalwebpage3, "html.parser")
    try:
        #Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Supportclass = internalpagesoup3.findAll("div",{"class":"rating-summary-block"})
        #Trial1 = soup(Trialclass, "html.parser")
        #Trial2 = internalpagesoup2.findAll("span",{"class":"sprite sprite-featureSupported"})
        Support = Supportclass[0]
        Supportstring = str(Support)
        String1 = Supportstring.split('qs=support-rating">',1)[1] 
        String2 = String1.split('</a></div></div><div class="rating-facet" data-toggle="tooltip" title=" Click to view In-Person',1)[0] 
        Supportrating=String2[-3:]
    except:
        Supportrating = "No Info Available"
    
    
    
    rows.append([Title,str(Description),URLlink,Image,RatingsAmount,ReviewsAmount,Review,Pros,Cons,Integrations,Trial,Supportrating,Score])
    
    
    
    
    
    print('---------------------------------')
    print(URLlink)
    print('---------------------------------')
    print(Title)
    print('---------------------------------')
    print(Description)
    print('---------------------------------')
    print(Image)
    print('---------------------------------')
    print(RatingsAmount)
    print('---------------------------------')
    print(ReviewsAmount)
    print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
 
    
#############3rd page parsing    
    
for i in range(Amountofproviders2):
    
    Provider = Providers2[i]
    Title = Provider.div.div.div["title"]
    
    Descclass = Provider.findAll("div",{"class":"CategoryProduct_content__2ML8S"})
    Description = Descclass[0].div.text
    
    Imageclass = Provider.findAll("div",{"class":"CategoryProduct_logo__gijLT"})
    Image = Imageclass[0].div.img["src"]
    
    URLclass = Provider.findAll("h3",{"class":"CategoryProduct_heading-text__1snnq"})
    URL = URLclass[0].a["href"]
    URLlink = 'https://www.trustradius.com'+str(URL)
    try:
        Ratingamountclass = Provider.findAll("div",{"class":"CategoryProduct_rating-count__2hxFa"})
        RatingsAmount =S Ratingamountclass[0].text
    
        Reviewamountclass = Provider.findAll("div",{"class":"CategoryProduct_rating-count__2hxFa"})
        ReviewsAmount = Reviewamountclass[1].text
    except:
        RatingsAmount = '0 Ratings'
        ReviewsAmount = '0 Reviews'
    internalreq = Request(URLlink, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage = urlopen(internalreq).read()
    internalpagesoup = soup(internalwebpage, "html.parser")
    try:
        Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Scoreclass = internalpagesoup.findAll("span",{"itemprop":"ratingValue"})
        Score = Scoreclass[0].text
    except:
        Score = "No Score Found"
        
    try:
        Comment = internalpagesoup.findAll("div",{"class":"review-questions"})
    
        Commentclass = internalpagesoup.findAll("div",{"class":"not-edited question-text"})
        Review = Commentclass[0].text
    except:
        Review = "No Reviews Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    
    
    try:
        Prossection = internalpagesoup.findAll("ul",{"class":"pros"})
    
        #Prosclass = internalpagesoup.findAll("div",{"class":"not-edited question-text"})
        Pros = Prossection[0].li.text
        
        
        
        
    except:
        Pros = "No Pros Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    
    try:
        Conssection = internalpagesoup.findAll("ul",{"class":"cons"})
    
        #Prosclass = internalpagesoup.findAll("div",{"class":"not-edited question-text"})
        Cons = Conssection[0].li.text
        
        
        
        
    except:
        Cons = "No Cons Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    
    internal2req = Request(URLlink2, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage2 = urlopen(internal2req).read()
    internalpagesoup2 = soup(internalwebpage2, "html.parser")
    try:
        #Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Trialclass = internalpagesoup2.findAll("span",{"class":"answer"})
        #Trial1 = soup(Trialclass, "html.parser")
        #Trial2 = internalpagesoup2.findAll("span",{"class":"sprite sprite-featureSupported"})
        Trial = Trialclass[0].text
    except:
        Trial = "No Info Available"
    
    try:
        #Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Integrationsclass = internalpagesoup2.findAll("section",{"id":"integrations"})
        #Trial1 = soup(Trialclass, "html.parser")
        #Trial2 = internalpagesoup2.findAll("span",{"class":"sprite sprite-featureSupported"})
        Integrations = Integrationsclass[0].div.text
        
    except:
        Integrations = "No Info Available"
    
    
    
    URLlink3 = URLlink+str('#3')
    
    
    
    
    internal3req = Request(URLlink3, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage3 = urlopen(internal3req).read()
    internalpagesoup3 = soup(internalwebpage3, "html.parser")
    try:
        #Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Supportclass = internalpagesoup3.findAll("div",{"class":"rating-summary-block"})
        #Trial1 = soup(Trialclass, "html.parser")
        #Trial2 = internalpagesoup2.findAll("span",{"class":"sprite sprite-featureSupported"})
        Support = Supportclass[0]
        Supportstring = str(Support)
        String1 = Supportstring.split('qs=support-rating">',1)[1] 
        String2 = String1.split('</a></div></div><div class="rating-facet" data-toggle="tooltip" title=" Click to view In-Person',1)[0] 
        Supportrating=String2[-3:]
    except:
        Supportrating = "No Info Available"
    
    
    
    rows.append([Title,str(Description),URLlink,Image,RatingsAmount,ReviewsAmount,Review,Pros,Cons,Integrations,Trial,Supportrating,Score])
    
    
    
    
    print('---------------------------------')
    print(URLlink)
    print('---------------------------------')
    print(Title)
    print('---------------------------------')
    print(Description)
    print('---------------------------------')
    print(Image)
    print('---------------------------------')
    print(RatingsAmount)
    print('---------------------------------')
    print(ReviewsAmount)
    print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
 
#############4th page parsing 

for i in range(Amountofproviders3):
    
    Provider = Providers3[i]
    Title = Provider.div.div.div["title"]
    
    Descclass = Provider.findAll("div",{"class":"CategoryProduct_content__2ML8S"})
    Description = Descclass[0].div.text
    
    Imageclass = Provider.findAll("div",{"class":"CategoryProduct_logo__gijLT"})
    Image = Imageclass[0].div.img["src"]
    
    URLclass = Provider.findAll("h3",{"class":"CategoryProduct_heading-text__1snnq"})
    URL = URLclass[0].a["href"]
    URLlink = 'https://www.trustradius.com'+str(URL)
    
    try:
        Ratingamountclass = Provider.findAll("div",{"class":"CategoryProduct_rating-count__2hxFa"})
        RatingsAmount = Ratingamountclass[0].text
    
        Reviewamountclass = Provider.findAll("div",{"class":"CategoryProduct_rating-count__2hxFa"})
        ReviewsAmount = Reviewamountclass[1].text
    except:
        RatingsAmount = '0 Ratings'
        ReviewsAmount = '0 Reviews'
    
    internalreq = Request(URLlink, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage = urlopen(internalreq).read()
    internalpagesoup = soup(internalwebpage, "html.parser")
    try:
        Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Scoreclass = internalpagesoup.findAll("span",{"itemprop":"ratingValue"})
        Score = Scoreclass[0].text
    except:
        Score = "No Score Found"
        
    try:
        Comment = internalpagesoup.findAll("div",{"class":"review-questions"})
    
        Commentclass = internalpagesoup.findAll("div",{"class":"not-edited question-text"})
        Review = Commentclass[0].text
    except:
        Review = "No Reviews Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    
    
    try:
        Prossection = internalpagesoup.findAll("ul",{"class":"pros"})
    
        #Prosclass = internalpagesoup.findAll("div",{"class":"not-edited question-text"})
        Pros = Prossection[0].li.text
        
        
        
        
    except:
        Pros = "No Pros Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    
    try:
        Conssection = internalpagesoup.findAll("ul",{"class":"cons"})
    
        #Prosclass = internalpagesoup.findAll("div",{"class":"not-edited question-text"})
        Cons = Conssection[0].li.text
        
        
        
        
    except:
        Cons = "No Cons Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    
    internal2req = Request(URLlink2, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage2 = urlopen(internal2req).read()
    internalpagesoup2 = soup(internalwebpage2, "html.parser")
    try:
        #Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Trialclass = internalpagesoup2.findAll("span",{"class":"answer"})
        #Trial1 = soup(Trialclass, "html.parser")
        #Trial2 = internalpagesoup2.findAll("span",{"class":"sprite sprite-featureSupported"})
        Trial = Trialclass[0].text
    except:
        Trial = "No Info Available"
    
    
    try:
        #Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Integrationsclass = internalpagesoup2.findAll("section",{"id":"integrations"})
        #Trial1 = soup(Trialclass, "html.parser")
        #Trial2 = internalpagesoup2.findAll("span",{"class":"sprite sprite-featureSupported"})
        Integrations = Integrationsclass[0].div.text
        
    except:
        Integrations = "No Info Available"
    
    
    
    URLlink3 = URLlink+str('#3')
    
    
    
    
    internal3req = Request(URLlink3, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage3 = urlopen(internal3req).read()
    internalpagesoup3 = soup(internalwebpage3, "html.parser")
    try:
        #Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Supportclass = internalpagesoup3.findAll("div",{"class":"rating-summary-block"})
        #Trial1 = soup(Trialclass, "html.parser")
        #Trial2 = internalpagesoup2.findAll("span",{"class":"sprite sprite-featureSupported"})
        Support = Supportclass[0]
        Supportstring = str(Support)
        String1 = Supportstring.split('qs=support-rating">',1)[1] 
        String2 = String1.split('</a></div></div><div class="rating-facet" data-toggle="tooltip" title=" Click to view In-Person',1)[0] 
        Supportrating=String2[-3:]
    except:
        Supportrating = "No Info Available"
    
    
    
    rows.append([Title,str(Description),URLlink,Image,RatingsAmount,ReviewsAmount,Review,Pros,Cons,Integrations,Trial,Supportrating,Score])
    
    
    
    
    
    print('---------------------------------')
    print(URLlink)
    print('---------------------------------')
    print(Title)
    print('---------------------------------')
    print(Description)
    print('---------------------------------')
    print(Image)
    print('---------------------------------')
    print(RatingsAmount)
    print('---------------------------------')
    print(ReviewsAmount)
    print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')

#############5th page parsing 

for i in range(Amountofproviders4):
    
    Provider = Providers4[i]
    Title = Provider.div.div.div["title"]
    
    Descclass = Provider.findAll("div",{"class":"CategoryProduct_content__2ML8S"})
    Description = Descclass[0].div.text
    
    Imageclass = Provider.findAll("div",{"class":"CategoryProduct_logo__gijLT"})
    Image = Imageclass[0].div.img["src"]
    
    URLclass = Provider.findAll("h3",{"class":"CategoryProduct_heading-text__1snnq"})
    URL = URLclass[0].a["href"]
    URLlink = 'https://www.trustradius.com'+str(URL)
    
    try:
        Ratingamountclass = Provider.findAll("div",{"class":"CategoryProduct_rating-count__2hxFa"})
        RatingsAmount = Ratingamountclass[0].text
    
        Reviewamountclass = Provider.findAll("div",{"class":"CategoryProduct_rating-count__2hxFa"})
        ReviewsAmount = Reviewamountclass[1].text
    except:
        RatingsAmount = '0 Ratings'
        ReviewsAmount = '0 Reviews'
    
    internalreq = Request(URLlink, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage = urlopen(internalreq).read()
    internalpagesoup = soup(internalwebpage, "html.parser")
    try:
        Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Scoreclass = internalpagesoup.findAll("span",{"itemprop":"ratingValue"})
        Score = Scoreclass[0].text
    except:
        Score = "No Score Found"
        
    try:
        Comment = internalpagesoup.findAll("div",{"class":"review-questions"})
    
        Commentclass = internalpagesoup.findAll("div",{"class":"not-edited question-text"})
        Review = Commentclass[0].text
    except:
        Review = "No Reviews Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    
    
    try:
        Prossection = internalpagesoup.findAll("ul",{"class":"pros"})
    
        #Prosclass = internalpagesoup.findAll("div",{"class":"not-edited question-text"})
        Pros = Prossection[0].li.text
        
        
        
        
    except:
        Pros = "No Pros Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    
    try:
        Conssection = internalpagesoup.findAll("ul",{"class":"cons"})
    
        #Prosclass = internalpagesoup.findAll("div",{"class":"not-edited question-text"})
        Cons = Conssection[0].li.text
        
        
        
        
    except:
        Cons = "No Cons Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    
    internal2req = Request(URLlink2, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage2 = urlopen(internal2req).read()
    internalpagesoup2 = soup(internalwebpage2, "html.parser")
    try:
        #Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Trialclass = internalpagesoup2.findAll("span",{"class":"answer"})
        #Trial1 = soup(Trialclass, "html.parser")
        #Trial2 = internalpagesoup2.findAll("span",{"class":"sprite sprite-featureSupported"})
        Trial = Trialclass[0].text
    except:
        Trial = "No Info Available"
    
    
    try:
        #Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Integrationsclass = internalpagesoup2.findAll("section",{"id":"integrations"})
        #Trial1 = soup(Trialclass, "html.parser")
        #Trial2 = internalpagesoup2.findAll("span",{"class":"sprite sprite-featureSupported"})
        Integrations = Integrationsclass[0].div.text
        
    except:
        Integrations = "No Info Available"
    
    
    
    URLlink3 = URLlink+str('#3')
    
    
    
    
    internal3req = Request(URLlink3, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage3 = urlopen(internal3req).read()
    internalpagesoup3 = soup(internalwebpage3, "html.parser")
    try:
        #Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Supportclass = internalpagesoup3.findAll("div",{"class":"rating-summary-block"})
        #Trial1 = soup(Trialclass, "html.parser")
        #Trial2 = internalpagesoup2.findAll("span",{"class":"sprite sprite-featureSupported"})
        Support = Supportclass[0]
        Supportstring = str(Support)
        String1 = Supportstring.split('qs=support-rating">',1)[1] 
        String2 = String1.split('</a></div></div><div class="rating-facet" data-toggle="tooltip" title=" Click to view In-Person',1)[0] 
        Supportrating=String2[-3:]
    except:
        Supportrating = "No Info Available"
    
    
    
    rows.append([Title,str(Description),URLlink,Image,RatingsAmount,ReviewsAmount,Review,Pros,Cons,Integrations,Trial,Supportrating,Score])
    
    
    
    
    print('---------------------------------')
    print(URLlink)
    print('---------------------------------')
    print(Title)
    print('---------------------------------')
    print(Description)
    print('---------------------------------')
    print(Image)
    print('---------------------------------')
    print(RatingsAmount)
    print('---------------------------------')
    print(ReviewsAmount)
    print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')


#############6th page parsing 

for i in range(Amountofproviders5):
    
    Provider = Providers5[i]
    Title = Provider.div.div.div["title"]
    
    Descclass = Provider.findAll("div",{"class":"CategoryProduct_content__2ML8S"})
    Description = Descclass[0].div.text
    
    Imageclass = Provider.findAll("div",{"class":"CategoryProduct_logo__gijLT"})
    Image = Imageclass[0].div.img["src"]
    
    URLclass = Provider.findAll("h3",{"class":"CategoryProduct_heading-text__1snnq"})
    URL = URLclass[0].a["href"]
    URLlink = 'https://www.trustradius.com'+str(URL)
    
    try:
        Ratingamountclass = Provider.findAll("div",{"class":"CategoryProduct_rating-count__2hxFa"})
        RatingsAmount = Ratingamountclass[0].text
    
        Reviewamountclass = Provider.findAll("div",{"class":"CategoryProduct_rating-count__2hxFa"})
        ReviewsAmount = Reviewamountclass[1].text
    except:
        RatingsAmount = '0 Ratings'
        ReviewsAmount = '0 Reviews'
    
    internalreq = Request(URLlink, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage = urlopen(internalreq).read()
    internalpagesoup = soup(internalwebpage, "html.parser")
    try:
        Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Scoreclass = internalpagesoup.findAll("span",{"itemprop":"ratingValue"})
        Score = Scoreclass[0].text
    except:
        Score = "No Score Found"
        
    try:
        Comment = internalpagesoup.findAll("div",{"class":"review-questions"})
    
        Commentclass = internalpagesoup.findAll("div",{"class":"not-edited question-text"})
        Review = Commentclass[0].text
    except:
        Review = "No Reviews Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    
    
    
    try:
        Prossection = internalpagesoup.findAll("ul",{"class":"pros"})
    
        #Prosclass = internalpagesoup.findAll("div",{"class":"not-edited question-text"})
        Pros = Prossection[0].li.text
        
        
        
        
    except:
        Pros = "No Pros Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    
    try:
        Conssection = internalpagesoup.findAll("ul",{"class":"cons"})
    
        #Prosclass = internalpagesoup.findAll("div",{"class":"not-edited question-text"})
        Cons = Conssection[0].li.text
        
        
        
        
    except:
        Cons = "No Cons Found"
    #URLlink = 'https://www.trustradius.com'+str(URL)
    
    
    internal2req = Request(URLlink2, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage2 = urlopen(internal2req).read()
    internalpagesoup2 = soup(internalwebpage2, "html.parser")
    try:
        #Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Trialclass = internalpagesoup2.findAll("span",{"class":"answer"})
        #Trial1 = soup(Trialclass, "html.parser")
        #Trial2 = internalpagesoup2.findAll("span",{"class":"sprite sprite-featureSupported"})
        Trial = Trialclass[0].text
    except:
        Trial = "No Info Available"
    
    
    try:
        #Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Integrationsclass = internalpagesoup2.findAll("section",{"id":"integrations"})
        #Trial1 = soup(Trialclass, "html.parser")
        #Trial2 = internalpagesoup2.findAll("span",{"class":"sprite sprite-featureSupported"})
        Integrations = Integrationsclass[0].div.text
        
    except:
        Integrations = "No Info Available"
    
    
    
    URLlink3 = URLlink+str('#3')
    
    
    
    
    internal3req = Request(URLlink3, headers={'User-Agent': 'Mozilla/5.0'})
    internalwebpage3 = urlopen(internal3req).read()
    internalpagesoup3 = soup(internalwebpage3, "html.parser")
    try:
        #Header = internalpagesoup.findAll("div",{"class":"product-header section-block-head"})
    
        Supportclass = internalpagesoup3.findAll("div",{"class":"rating-summary-block"})
        #Trial1 = soup(Trialclass, "html.parser")
        #Trial2 = internalpagesoup2.findAll("span",{"class":"sprite sprite-featureSupported"})
        Support = Supportclass[0]
        Supportstring = str(Support)
        String1 = Supportstring.split('qs=support-rating">',1)[1] 
        String2 = String1.split('</a></div></div><div class="rating-facet" data-toggle="tooltip" title=" Click to view In-Person',1)[0] 
        Supportrating=String2[-3:]
    except:
        Supportrating = "No Info Available"
    
    
    
    rows.append([Title,str(Description),URLlink,Image,RatingsAmount,ReviewsAmount,Review,Pros,Cons,Integrations,Trial,Supportrating,Score])
    
    
    
    
    print('---------------------------------')
    print(URLlink)
    print('---------------------------------')
    print(Title)
    print('---------------------------------')
    print(Description)
    print('---------------------------------')
    print(Image)
    print('---------------------------------')
    print(RatingsAmount)
    print('---------------------------------')
    print(ReviewsAmount)
    print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')


 
 




    
#fieldnames = ['URL', 'VoIP Provider', 'Description','Image logo URL','Amount of ratings','Amount of reviews']

with open('output.csv', 'w',encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)

