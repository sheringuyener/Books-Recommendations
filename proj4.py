from flask import *

app = Flask(__name__)
numBooks = 0

def readBooks(bfilename):
    f=open(bfilename)
    booksAndAuthors=f.readlines()
    for i in range(0,len(booksAndAuthors)):
        booksAndAuthors[i]=booksAndAuthors[i].replace("\n","")
    f.close()
    return booksAndAuthors #returns it as a list
       

@app.route('/')
def createProfile():
    allBooks=readBooks("books.txt")
    html+=""
    html +='<!DOCTYPE html>\n'
    html +='<html>\n'
    html +='<body>\n'
    html +='<form method="POST" action="/showResult">\n'
    for i in range(0,len(allBooks)):
        html+='<input type="radio" name="option" value='+i+'>'+allBooks[i]+'<br>\n'
    html +='</form>\n'
    html +='</body>\n'
    html +='</html>\n'
    return html
    
##
##@app.route('/recommend', methods = ['POST'])
##def recommend() :
##       # call readBooks again
##       # call readRatings
##       # get the user's ratings from the form
##       # call recommendBooks
##       # display a list of recommended books       
##    
##  
##def readRatings(filename):
##    otherRatings={}
##    f=open(filename) #reads lines from text
##    line=f.readlines()
##    name=[]
##    ratings=[]
##    for i in range(1,len(line),2):
##        line[i]=line[i].split()
##        for j in range(0,len(line[i])):
##            line[i][j]=int(line[i][j])
##        ratings=ratings+[line[i]]
##    #print(ratings)
##    for k in range(0,len(line),2):
##        line[k]=line[k].replace("\n","")
##        name=name+[line[k]]
##    for l in range(0,len(name)):
##        otherRatings[name[l]]=ratings[l]
##    f.close()
##    return(otherRatings)
##       
##def recommendBooks(books, dictRatings, userRatings) :
##    simList=[]
##    for key in dictRatings.keys():
##        similarity=0
##        value=dictRatings[key]
##        for i in range(0,len(userRatings)):
##            similarity=similarity+value[i]*userRatings[i]
##        simList.append([similarity,key] )   
##    for j in range(1,len(simList)):
##        curr=simList[j]
##        k=j-1
##        while k>=0 and curr<simList[k]:
##            simList[k+1]=simList[k]
##            k=k-1
##        simList[k+1]=curr
##    simList.reverse()#highest score to lowest score
##    topFive=simList[0:5] #should be 0-5, not 0-6
##    sortedRatings=[]
##    recomBooks=""
##    for i in range(0, len(topFive)):
##        value1=dictRatings.get(topFive[i][1])
##        sortedRatings=sortedRatings+[value1]
##    for k in range(0,len(sortedRatings)):
##        limit=0
##        for l in range(0,len(sortedRatings[k])):
##            if sortedRatings[k][l]==5 and userRatings[l]==0:
##                if limit<5:
##                    if books[l] not in recomBooks:
##                        recomBooks=recomBooks+books[l]+"\n"
##                        limit=limit+1
##                if limit>=5:
##                    recomBooks=recomBooks
##    return recomBooks
##                             
##       
##
##def writeBooksToFile(recomBooks, filename):
##    n=open(filename,'w')
##    rBooks=n.write(recomBooks)
##

app.run()
