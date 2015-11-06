#project4

def readBooks(bfilename): #opens file with book names
    f=open(bfilename) #open file
    booksAndAuthors=f.readlines()
    for i in range(0,len(booksAndAuthors)):
        booksAndAuthors[i]=booksAndAuthors[i].replace("\n","")
    f.close()
    return booksAndAuthors #returns it as a list

def readUserProfile(filename): #(alice's)
    f=open(filename) #open user profile (alice)
    userProfile=f.readlines() 
    userProfile[1]=userProfile[1].split()
    for i in range(0,len(userProfile[1])):
        userProfile[1][i]=int(userProfile[1][i]) #converts each rating str to integer
    userRatings=userProfile[1]
    f.close()
    return userRatings

#print(readUserProfile("profile.txt"))

def readRatings(filename):
    otherRatings={}
    f=open(filename) #reads lines from text
    line=f.readlines()
    name=[] #new empty string for usernames
    ratings=[] #new empty string for ratings
    for i in range(1,len(line),2):
        line[i]=line[i].split()
        for j in range(0,len(line[i])):
            line[i][j]=int(line[i][j])
        ratings=ratings+[line[i]] #all users ratings in nest list
    for k in range(0,len(line),2):
        line[k]=line[k].replace("\n","")
        name=name+[line[k]] #corresponding user names
    for l in range(0,len(name)):
        otherRatings[name[l]]=ratings[l]#put all user names and ratings into a dictionary
    f.close()
    return(otherRatings) #return dictionary
    
#print(readRatings("ratings.txt"))

       
def recommendBooks(books, dictRatings, userRatings):
    simList=[]
    for key in dictRatings.keys(): #iterating over keys in dictionary
        similarity=0
        value=dictRatings[key]
        for i in range(0,len(userRatings)): #finding similarity to alice
            similarity=similarity+value[i]*userRatings[i]
        simList.append([similarity,key] )   
    for j in range(1,len(simList)): #creates a similarity list
        curr=simList[j]
        k=j-1
        while k>=0 and curr<simList[k]:
            simList[k+1]=simList[k]
            k=k-1
        simList[k+1]=curr
    simList.reverse()#highest score to lowest score(instead of lowest to highest)
    topFive=simList[0:5] #takes the top 5 users most similiar to alice, i.e. has the highest similarity score
    sortedRatings=[]
    recomBooks=""
    for i in range(0, len(topFive)):
        value1=dictRatings.get(topFive[i][1])
        sortedRatings=sortedRatings+[value1] #list of ratings from top 5
    #print(sortedRatings)
    for k in range(0,len(sortedRatings)):
        limit=0
        for l in range(0,len(sortedRatings[k])): #adding books to list of recommended books
            if sortedRatings[k][l]==5 and userRatings[l]==0:#if user gives it a 5 and alice gives 0
                if limit<5: #limiting 5 books per user
                    if books[l] not in recomBooks:
                        recomBooks=recomBooks+books[l]+"\n"
                        limit=limit+1
                if limit>=5:
                    recomBooks=recomBooks
    return recomBooks #returns string of recommended books to alice

def writeBooksToFile(recomBooks, filename):
    n=open(filename,'w') #creates new file to write list of recommended books in
    rBooks=n.write(recomBooks)
    n.close()

  
def main() :
    listOfBooks=readBooks("books.txt") 
    userProfile=readUserProfile("profile.txt") 
    dRatings=readRatings("ratings.txt")
    recBooks=recommendBooks(listOfBooks,dRatings,userProfile)
    writeBooksToFile(recBooks,"recommendedBooks.txt")

#main()
