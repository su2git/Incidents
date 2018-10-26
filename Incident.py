
# pip pyodbc --at doc
# https://github.com/mkleehammer/pyodbc/wiki/Getting-started


import pyodbc as pyodbc

driver= '{ODBC Driver 13 for SQL Server}'

cnxn = pyodbc.connect(
    Trusted_Connection='Yes',
    Driver='{ODBC Driver 13 for SQL Server}',
    Server='EDWP,1433',
    Database='PKG_IT'
)


cursor = cnxn.cursor()



#https://www.analyticsvidhya.com/blog/2018/02/the-different-methods-deal-text-data-predictive-python/


cursor.execute("SELECT * FROM [PKG_IT].[dbo].[INCIDENT_IT_FACT] I  ;")
while True:
    row = cursor.fetchone()
    if not row:
        break
    train = row.SHRT_DESC
    #print(type(row.SHRT_DESC))



train['word_count'] = train['SHRT_DESC'].apply(lambda x:x.split(" "))
#train[['SHRT_DESC' ,'word_count']].head()


#Number of Words
train['word_count'] = train['SHRT_DESC'].apply(lambda x: len(str(x).split(" ")))
train[['SHRT_DESC','word_count']].head()

#Number of characters
train['char_count'] = train['SHRT_DESC'].str.len() ## this also includes spaces
train[['SHRT_DESC','char_count']].head()

#Average Word Length
def avg_word(sentence):
  words = sentence.split()
  return (sum(len(word) for word in words)/len(words))

train['avg_word'] = train['SHRT_DESC'].apply(lambda x: avg_word(x))
train[['SHRT_DESC','avg_word']].head()

#Number of stopwords
from nltk.corpus import stopwords
stop = stopwords.words('english')

train['stopwords'] = train['SHRT_DESC'].apply(lambda x: len([x for x in x.split() if x in stop]))
train[['SHRT_DESC','stopwords']].head()

# Number of special characters
train['hastags'] = train['SHRT_DESC'].apply(lambda x: len([x for x in x.split() if x.startswith('#')]))
train[['SHRT_DESC','hastags']].head()


#Number of numerics
train['numerics'] = train['SHRT_DESC'].apply(lambda x: len([x for x in x.split() if x.isdigit()]))
train[['SHRT_DESC','numerics']].head()

#Number of Uppercase words
train['upper'] = train['SHRT_DESC'].apply(lambda x: len([x for x in x.split() if x.isupper()]))
train[['SHRT_DESC','upper']].head()


#Lower case
train['SHRT_DESC'] = train['SHRT_DESC'].apply(lambda x: " ".join(x.lower() for x in x.split()))
train['SHRT_DESC'].head()

#Removing Punctuation
train['SHRT_DESC'] = train['SHRT_DESC'].str.replace('[^\w\s]','')
train['SHRT_DESC'].head()

#Removal of Stop Words
from nltk.corpus import stopwords
stop = stopwords.words('english')
train['SHRT_DESC'] = train['SHRT_DESC'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
train['SHRT_DESC'].head()

#Common word removal
#Rare words removal
#Spelling correction
#Tokenization
#Stemming
#Lemmatization
#N-grams
#Term frequency
#Inverse Document Frequency
#Term Frequency – Inverse Document Frequency (TF-IDF)
#Bag of Words
#Sentiment Analysis
#Word Embeddings
