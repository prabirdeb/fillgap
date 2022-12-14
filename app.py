# -*- coding: utf-8 -*-
"""fillgap.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Kg678a28BCkD9ZGkmcQnoCd73P8XGCjp
"""

# Writing helper functions

# Function for finding similarity score between two words

def similar(word1,word2):
  try:
    # Importing libraries
    import nltk
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    from nltk.corpus import wordnet

    # Finding the index of word1
    word1=word1.lower()
    len_word1=len(word1)
    index=len("Synset('")+len_word1+1
    text="Synset('"+word1+"."
    doc1 = [k for k in wordnet.synsets(word1) if str(k)[:index]==text]

    # Finding the index of word2
    word2=word2.lower()
    len_word2=len(word2)
    index=len("Synset('")+len_word2+1
    text="Synset('"+word2+"."
    doc2 = [k for k in wordnet.synsets(word2) if str(k)[:index]==text]
    
    # Finding the similarity score
    if len(doc1)>0:
      doc1=doc1[0]
    elif len(wordnet.synsets(word1))>0:
      doc1=wordnet.synsets(word1)[0]
    else:
      doc1=wordnet.synsets("up")[0]  # when word is not found in nltk

    if len(doc2)>0:
      doc2=doc2[0]
    elif len(wordnet.synsets(word2))>0:
      doc2=wordnet.synsets(word2)[0]
    else:
      doc2=wordnet.synsets("down")[0] # when word is not found in nltk

    score=doc1.wup_similarity(doc2)
    
  except:
    score=0
  return score

# writing text pre-processing function
def text_process(text):
  try:
    text = text.lower()    # converting to lowercase
    import string
    # text =[char for char in text if char not in string.punctuation] # removing punctuations as available in string library creating problem in mathematics section
    punc='!"#$&\',;?@\\_`<>'
    text =[char for char in text if char not in punc]
    text=''.join(text) 

    import nltk
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

    tokens = nltk.word_tokenize(text)
    pos_tagged_tokens = nltk.pos_tag(tokens)

    list_of_verbs = []
    for i in range(len(pos_tagged_tokens)):
      if pos_tagged_tokens[i][1].startswith('V'):
        list_of_verbs.append(pos_tagged_tokens[i][0])
    
    nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.extend(list_of_verbs)

    text=[word for word in text.split() if word not in stopwords] # removing stopwords and verbs
    
    # Removing common_words
    common_words=['due','shall','etc.', 'e.g.', 'eg', 'eg.','1.','2.','3.','4.','5.','6.','7.','8.','9.','10.','11.','12.','13.','14.','15.','16.','17.','18.','19.','20.','i.','ii.','iii.','iv.','v.','vi.','vii.','viii.','ix.','x.','xi.','xii.','xiii.','xiv.','xv.','xvi.','xvii.','xviii.','xix.','xx.','a.','b.','c.','d.','e.','f.','g.','h.','1)','2)','3)','4)','5)','6)','7)','8)','9)','10)','11)','12)','13)','14)','15)','16)','17)','18)','19)','20)','i)','ii)','iii)','iv)','v)','vi)','vii)','viii)','ix)','x)','xi)','xii)','xiii)','xiv)','xv)','xvi)','xvii)','xviii)','xix)','xx)','a)','b)','c)','d)','e)','f)','g)','h)','(1)','(2)','(3)','(4)','(5)','(6)','(7)','(8)','(9)','(10)','(11)','(12)','(13)','(14)','(15)','(16)','(17)','(18)','(19)','(20)','(i)','(ii)','(iii)','(iv)','(v)','(vi)','(vii)','(viii)','(ix)','(x)','(xi)','(xii)','(xiii)','(xiv)','(xv)','(xvi)','(xvii)','(xviii)','(xix)','(xx)','(a)','(b)','(c)','(d)','(e)','(f)','(g)','(h)','towards','share','along','lies','climate','throughout','aim','rule','simply','structural','system','etc','like','orderly','manner','jealous', 'ahem', 'phew', 'blue-eyed', 'usually', 'ouch', 'expeditiously', 'foolish', 'morning', 'inquisitive', 'disgusted', 'whenever', 'hastily', 'confused', 'please', 'brr', 'well', 'nasty', 'question', 'power', 'home', 'art', 'defiant', 'enormously', 'air', 'oh', 'sparkling', 'nervously', 'selfish', 'glamorous', 'eagerly', 'point', 'homely', 'dizzy', 'perfectly', 'courageous', 'tough', 'money', 'others', 'incidentally', 'until', 'hmm', 'gleefully', 'year', 'fleetingly', 'famous', 'work', 'aww', 'level', 'muddy', 'shh', 'super', 'inasmuch', 'gentle', 'silently', 'tasty', 'emphatically', 'enchanting', 'annoyed', 'defiantly', 'girl', 'fancy', 'black', 'member', 'addition', 'program', 'idea', 'sore', 'bravely', 'precious', 'community', 'here', 'embarrassed', 'huh', 'lazily', 'fine', 'nervous', 'bored', 'instantly', 'before', 'even', 'obediently', 'cheerfully', 'strange', 'disturbed', 'clumsy', 'for', 'result', 'soundlessly', 'woman', 'important', 'hungrily', 'angry', 'student', 'shoo', 'creepy', 'cruel', 'number', 'determined', 'promptly', 'adventurous', 'horrible', 'difficult', 'grumpy', 'encore', 'rather', 'briskly', 'motionless', 'pleasant', 'system', 'depressed', 'audibly', 'madly', 'bewildered', 'never', 'quietly', 'dramatically', 'rarely', 'people', 'health', 'softly', 'shiny', 'enviously', 'jittery', 'research', 'scary', 'blushing', 'bad', 'morosely', 'relieved', 'powerfully', 'that', 'game', 'drab', 'job', 'delightful', 'thoughtless', 'tediously', 'city', 'outstanding', 'yo', 'golly', 'word', 'comfortable', 'evil', 'war', 'weakly', 'honestly', 'modern', 'hour', 'handsome', 'moment', 'obedient', 'eureka', 'worried', 'still', 'mother', 'merrily', 'all', 'issue', 'warmly', 'smiling', 'hence', 'poorly', 'child', 'business', 'obnoxiously', 'history', 'back', 'stormy', 'ahh', 'casually', 'president', 'encouraging', 'amused', 'indeed', 'ugliest', 'than', 'rats', 'lot', 'soon', 'annoyingly', 'deafeningly', 'charming', 'house', 'agreeable', 'ah', 'cute', 'graceful', 'fortunately', 'foolishly', 'light', 'country', 'thing', 'gifted', 'mysterious', 'likewise', 'daily', 'curious', 'glorious', 'easy', 'father', 'splendid', 'crowded', 'calm', 'finally', 'alas', 'information', 'healthy', 'panicky', 'room', 'successful', 'yearly', 'head', 'tender', 'life', 'boldly', 'normally', 'seldom', 'smoggy', 'company', 'elegant', 'school', 'inexpensive', 'envious', 'fair', 'cruelly', 'mushy', 'joyous', 'eww', 'silence', 'name', 'grieving', 'regularly', 'law', 'gleaming', 'kid', 'though', 'average', 'day', 'faithfully', 'book', 'badly', 'selfishly', 'tomorrow', 'cloudy', 'puzzled', 'rudely', 'wandering', 'deftly', 'cheerful', 'dull', 'part', 'hourly', 'different', 'wide-eyed', 'victoriously', 'excited', 'crazily', 'elated', 'dutifully', 'frail', 'odd', 'duh', 'gradually', 'story', 'yuck', 'expensive', 'office', 'case', 'ear-splittingly', 'shy', 'quickly', 'kind', 'week', 'immediately', 'gorgeous', 'zealous', 'seriously', 'place', 'worrisome', 'anxiously', 'languidly', 'after', 'once', 'yesterday', 'stupid', 'joylessly', 'psst', 'face', 'painfully', 'exuberant', 'shrilly', 'kindly', 'aggressive', 'furthermore', 'right', 'line', 'today', 'distinct', 'if', 'gosh', 'blah', 'however', 'achingly', 'nutty', 'loudly', 'impossible', 'enthusiastic', 'provided', 'awesome', 'sternly', 'haltingly', 'resonantly', 'proud', 'eye', 'leisurely', 'repulsive', 'rapidly', 'ugly', 'old-fashioned', 'blindly', 'long', 'poor', 'condemned', 'tense', 'restlessly', 'hungry', 'shakily', 'state', 'energetic', 'plain', 'bloody', 'unsightly', 'fantastic', 'body', 'lovely', 'hopelessly', 'awful', 'as', 'victorious', 'perfect', 'hush', 'a', 'frantic', 'angrily', 'unhappily', 'coyly', 'slowly', 'lazy', 'education', 'faithful', 'speedily', 'wildly', 'swiftly', 'careful', 'arrogant', 'scat', 'talented', 'tame', 'ashamed', 'water', 'innocent', 'force', 'government', 'occasionally', 'later', 'defeated', 'weary', 'unexpectedly', 'poised', 'person', 'aha', 'teacher', 'quaint', 'homeless', 'deliberately', 'helpless', 'minute', 'dead', 'zany', 'cow', 'putrid', 'gee', 'uproariously', 'cautious', 'anxious', 'awkwardly', 'dark', 'sleepy', 'no', 'study', 'vivacious', 'doubtful', 'lucky', 'instead', 'prickly', 'end', 'silly', 'clever', 'reason', 'powerful', 'there', 'hilarious', 'hey', 'man', 'brave', 'politely', 'gracefully', 'safely', 'itchy', 'crazy', 'often', 'time', 'night', 'example', 'area', 'bright', 'eek', 'whereas', 'team', 'troubled', 'lively', 'wearily', 'guy', 'beautiful', 'hand', 'excitedly', 'fact', 'just', 'annoying', 'mortally', 'magnificent', 'service', 'dejectedly', 'thankful', 'vociferously', 'wrong', 'ill', 'problem', 'alive', 'brightly', 'blue', 'grotesque', 'frightened', 'sadly', 'since', 'parent', 'crikey', 'obnoxious', 'yippee', 'attractive', 'better', 'alert', 'hurt', 'clean', 'always', 'group', 'dangerous', 'bingo', 'eventually', 'colorful', 'enough', 'wicked', 'door', 'outrageous', 'family', 'noisily', 'combative', 'faintly', 'car', 'solemnly', 'now', 'eager', 'side', 'funny', 'consequently', 'thoughtful', 'concerned', 'upset', 'open', 'way', 'uptight', 'happy', 'month', 'holy', 'adorable', 'in', 'vivaciously', 'jealously', 'spotless', 'breakable', 'when', 'friend', 'change', 'boastfully', 'good', 'terribly', 'sometimes', 'real', 'innocently', 'wherever', 'friendly', 'naughty', 'meanwhile', 'cooperative', 'bravo', 'helpful', 'generally', 'busy', 'clear', 'phooey', 'fragile', 'nice', 'lonely', 'jolly', 'wild', 'brainy', 'party', 'uninterested', 'supposing', 'miserably', 'grief', 'tired', 'doubtfully', 'irritably', 'terrible', 'happily', 'hurriedly', 'rich', 'accidentally', 'devotedly', 'world', 'elegantly', 'mysteriously', 'nightly', 'thunderously', 'filthy', 'misty', 'inaudibly', 'noiselessly', 'ugh', 'frequently', 'fierce', 'unusual', 'resoundingly', 'vast', 'weekly', 'witty']
    
    for k in common_words:
      if k in text: 
        text.remove(k)

    text=' '.join(text)

  except:
    text=text

  return text

# writing stemming function
def stem(word):
  from nltk.stem.snowball import SnowballStemmer
  try:
    # removing all brackets
    if word[:1]=="(" and word[-1:]==")":
      word=word[1:-1]

    elif word[:1]=="{" and word[-1:]=="}":
      word=word[1:-1]

    elif word[:1]=="[" and word[-1:]=="]":
      word=word[1:-1]

    elif word[:1]=="(" or word[:1]=="{" or word[:1]=="[":
      word=word[1:]

    elif word[-1:]==")" or word[-1:]=="}" or word[-1:]=="]":
      word=word[:-1]

    elif word[-1:]==".":
      word=word[:-1]
    
    elif word[-1:]==":":
      word=word[:-1]

    stemmer = SnowballStemmer("english") 
    text = stemmer.stem(word)
        
  except:
    text=word

  return text

def cl_lst():
  try:
    # Importing libraries
    import numpy as np
    import pandas as pd
    
    # Reading student data as pandas df
    gsheetid = "1g1uWDGjJ1aGRXtJVkISj9qwq-DJmnzTS"
    sheet_name = "Sheet1" # Student should not change the sheet name

    # Converting google sheet to csv
    gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)

    # Creating student data df
    student_data = pd.read_csv(gsheet_url)
  
    result=list(student_data["Class"].unique())
    result = [x for x in result if str(x) != 'nan']
    
  except:
    result=[]
    student_data=pd.DataFrame([[]])

  return result, student_data

def medium_lst(cl, student_data):
  try:
    # Importing libraries
    import numpy as np
    import pandas as pd
     
    result=list(student_data[(student_data.Class==cl)]["Medium"].unique())
    result = [x for x in result if str(x) != 'nan']
    
  except:
    result=[]
    
  return result

def id_lst(cl, medium, student_data):
  try:
    # Importing libraries
    import numpy as np
    import pandas as pd
  
    result=list(student_data[(student_data.Class==cl) & (student_data.Medium==medium)]["ID"].unique())
    result = [x for x in result if str(x) != 'nan']
        
  except:
    result=[]
    
  return result

def subject_lst(id, medium, student_data):
  try:
    # Importing libraries
    import numpy as np
    import pandas as pd

    # Creating individual student df
    # Getting google sheet id
    gsheetid = student_data[(student_data["ID"]==id) & (student_data["Status"]=="Active")]["Concept_link"].values[0].replace("https://docs.google.com/spreadsheets/d/","").split("/")[0]
    sheet_name = "Concepts" # Student should not change the sheet name

    # Converting google sheet to csv
    gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)

    # Creating individual student data df
    individual_student_data = pd.read_csv(gsheet_url)
    individual_student_data = individual_student_data[(individual_student_data["Class"]==student_data[(student_data["ID"]==id)]["Class"].values[0])]

    subject=list(individual_student_data["Subjects"].unique())
    subject = [x for x in subject if str(x) != 'nan']

    if medium=="English" and "Hindi" in subject:
      subject.remove("Hindi")

    if medium=="English" and "hindi" in subject:
      subject.remove("hindi")

    if medium=="English" and "Bengali" in subject:
      subject.remove("Bengali")

    if medium=="English" and "bengali" in subject:
      subject.remove("bengali")

    if medium=="English" and "Sanskrit" in subject:
      subject.remove("Sanskrit")

    if medium=="English" and "sanskrit" in subject:
      subject.remove("sanskrit")

    # Getting the subjects where atleast 5 concepts present
    relevant_features=['Concept-1', 'Concept-2', 'Concept-3', 'Concept-4', 'Concept-5',
    'Concept-6', 'Concept-7', 'Concept-8', 'Concept-9', 'Concept-10',
    'Concept-11', 'Concept-12', 'Concept-13', 'Concept-14', 'Concept-15',
    'Concept-16', 'Concept-17', 'Concept-18', 'Concept-19', 'Concept-20']

    result=[]
    for sub in subject: 
      concepts_d=individual_student_data[(individual_student_data.Subjects==sub)]
      concepts_d=concepts_d[relevant_features]
      concepts_d=pd.DataFrame(concepts_d.values.flatten(), columns=['documents'])
      concepts_d.dropna(inplace=True) 
      concepts_d=concepts_d[(concepts_d['documents']!='\n')]
      concepts_d=concepts_d[(concepts_d['documents']!='\n\n')]
      concepts_d=concepts_d[(concepts_d['documents']!='No data')].reset_index()
      concepts_d.drop('index',axis=1, inplace=True)
      if concepts_d.shape[0]>=5:
        result.append(sub)
  
  except:
    result=[]
    individual_student_data=pd.DataFrame([[]])

  return result, individual_student_data

def topic_lst(id, subject, individual_student_data):
  '''
  id=int
  subject=list of subjects
  '''
  try:
    # Importing libraries
    import numpy as np
    import pandas as pd

    relevant_features=['Concept-1', 'Concept-2', 'Concept-3', 'Concept-4', 'Concept-5',
    'Concept-6', 'Concept-7', 'Concept-8', 'Concept-9', 'Concept-10',
    'Concept-11', 'Concept-12', 'Concept-13', 'Concept-14', 'Concept-15',
    'Concept-16', 'Concept-17', 'Concept-18', 'Concept-19', 'Concept-20']
    # Getting the topics where atleast 5 concepts present

    result=[]
    for sub in subject: 
      for top in list(individual_student_data[(individual_student_data.Subjects==sub)]["Topics"].unique()):
        concepts_d=individual_student_data[(individual_student_data.Subjects==sub) & (individual_student_data.Topics==top)]
        concepts_d=concepts_d[relevant_features]
        concepts_d=pd.DataFrame(concepts_d.values.flatten(), columns=['documents'])
        concepts_d.dropna(inplace=True) 
        concepts_d=concepts_d[(concepts_d['documents']!='\n')]
        concepts_d=concepts_d[(concepts_d['documents']!='\n\n')]
        concepts_d=concepts_d[(concepts_d['documents']!='No data')].reset_index()
        concepts_d.drop('index',axis=1, inplace=True)
        if concepts_d.shape[0]>=5:
          result.append(top)
    
  except:
    result=[]
  
  return result

# question types: numerical, general
def question_type(id, subject, topic, individual_student_data):
  '''
  id=int
  subject=list
  topic=list
  '''
  try:
    # Importing libraries
    import numpy as np
    import pandas as pd

    # Getting the document for the subject
    df_lst=[]
    for s in subject:
      for t in topic:
        sub=s.title() # Converting to title case
        subject_data=individual_student_data[(individual_student_data.Subjects==sub) & (individual_student_data.Topics==t)]

        relevant_features=['Concept-1', 'Concept-2', 'Concept-3', 'Concept-4', 'Concept-5',
        'Concept-6', 'Concept-7', 'Concept-8', 'Concept-9', 'Concept-10',
        'Concept-11', 'Concept-12', 'Concept-13', 'Concept-14', 'Concept-15',
        'Concept-16', 'Concept-17', 'Concept-18', 'Concept-19', 'Concept-20']

        subject_data=subject_data[relevant_features]
        df_lst.append(subject_data)
    # Concatinating all the df
    subject_data=pd.concat(df_lst)
    # Creating documents with all individual cell
    subject_data=pd.DataFrame(subject_data.values.flatten(), columns=['documents'])

    # Removing null value rows
    subject_data.dropna(inplace=True) 

    # There are many documents with only newline character. Removing those rows
    subject_data=subject_data[(subject_data['documents']!='\n')]
    subject_data=subject_data[(subject_data['documents']!='\n\n')]

    # Removing all the rows with no data and reseting index 
    subject_data=subject_data[(subject_data['documents']!='No data')].reset_index()

    subject_data.drop('index',axis=1, inplace=True)

    result=[]
    if subject_data.shape[0]!=0:
      
      for original_text_old in subject_data.documents:

        # Removing image link from original text
        original_text="\n".join([k for k in original_text_old.split("\n") if k[:4]!="http"])

        text=text_process(original_text)
        # Finding the numerical values
        import re      
        numbers=re.findall(r"[-+]?(?:\d*\.\d+|\d+)", text)
      
        if len(text.split())>0:
          if len(numbers)>=3 and 'numerical' not in result:   # Finding the numerical problem
            result.append('numerical')
            
          elif len(numbers)<3 and 'general' not in result:
            result.append('general')        
              
    else:
      result=['general']
  except:
    result=['general']
    subject_data=pd.DataFrame([[]])
  
  return result, subject_data

def inspire():
  try:
    import random
    lst=["Superb!","Mind-blowing!","Awesome!","Wonderful!","Stunning!","Spectacular!","Miraculous!","Majestic!","Inspiring!","Amazing!","Astonishing!","Astounding!","Breathtaking!","Imposing!","Marvelous!","Incredible!","Fascinating!","Fabulous!","Excellent!","Unbelievable!","Fantastic!"]
    random.shuffle(lst)
    res=lst[0]

  except:
    res="Awesome!"
  return res

# Writing main function
def fill_gap(id, subject, topic, ques_type, subject_data):
  '''
  id=int
  subject=list
  topic=list
  ques_type=list
  '''
  try:
    # Importing libraries
    import numpy as np
    import pandas as pd

    original_text_list=[]
    if subject_data.shape[0]!=0:
      
      for original_text in subject_data.documents:

        text=text_process(original_text)
        # Finding the numerical values
        import re      
        numbers=re.findall(r"[-+]?(?:\d*\.\d+|\d+)", text)
              
        if len(text.split())>0:
          if len(numbers)>=3 and 'numerical' in ques_type:   # Finding the numerical problem
            original_text_list.append(original_text)
            
          elif len(numbers)<3 and 'general' in ques_type:
            original_text_list.append(original_text)   

      import random
      random.shuffle(original_text_list)
      original_text_old=original_text_list[0]

      # Removing image link from original text
      original_text="\n".join([k for k in original_text_old.split("\n") if k[:4]!="http"])

      # Finding the image links
      list_of_images=[k for k in original_text_old.split("\n") if k[:4]=="http"]
    
      text=text_process(original_text)
      # Finding the numerical values
      import re      
      numbers=re.findall(r"[-+]?(?:\d*\.\d+|\d+)", text)

      # Generating answer and question
      # Random selection of question
      import random
      
      if len(text.split())>0:
        if len(numbers)>=3:   # Finding the numerical problem
          random.shuffle(numbers)
          ans=numbers[0]
        else:
          lst=text.split()
          random.shuffle(lst)
          ans=lst[0]
        
        # !"#$&\',;?@\\_`<> considering these characters at the start and end of answer
        for k in original_text.lower().split():
          if k==ans or k==ans+"," or k==","+ans or k==ans+";" or k==";"+ans or k==ans+"?" or k=="?"+ans or k==ans+"#" or k=="#"+ans or k==ans+"!" or k=="!"+ans or k==ans+"'" or k=="'"+ans or k==ans+"@" or k=="@"+ans or k==ans+"&" or k=="&"+ans or k==ans+"_" or k=="_"+ans or k==ans+">" or k==">"+ans or k==ans+"<" or k=="<"+ans or k==ans+">>" or k==">>"+ans:
            ans_index = original_text.lower().split().index(k)
            break

        # ans_index=original_text.lower().split().index(ans)
        original_text1=original_text.split("\n")  # code for retaining the structure of concepts entered by students
        original_text2=[]
        for k in original_text1:
          original_text2.append(k.split())
        c=0
        for k in original_text2:
          ans_index=ans_index-len(k)
          if ans_index<0:
            original_text2[c][ans_index]="_____"
            break
          c+=1
        ques=[" ".join(k) for k in original_text2]
        ques="\n".join(ques)
                
      else:
        ques="Ask question again. Concept found is very poor in strength:("
        ans=""
        list_of_images=[]
      
    else:
      ques="You have no concept record for this subject"
      ans=""
      list_of_images=[]
  except:
    ques="Please provide numerical values with space in the concept"
    ans=""
    list_of_images=[]
  
  return ques, ans, list_of_images

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

# Streamlit Project
import streamlit as st # All the text cell will be displayed after this import statement

st.title("Welcome to FillGap Practice !!")

cl_list = cl_lst()

cl = st.selectbox("Class", cl_list[0]) 

medium = st.selectbox("Medium", medium_lst(cl, cl_list[1])) 

id = st.selectbox("Your ID", id_lst(cl, medium, cl_list[1])) 

subject_list=subject_lst(id, medium, cl_list[1])

subject = st.multiselect("Subject ", subject_list[0]) 

topic = st.multiselect("Topic ", topic_lst(id, subject, subject_list[1]))

question_types=question_type(id, subject, topic, subject_list[1])

ques_type = st.multiselect("Question Type ", question_types[0])

add_bg_from_local('fillgap.png')   

question= st.button("Get Question")  

if "score" not in st.session_state:
  st.session_state.score=0

if question: # when any button is pressed in streamlit,code runs from the begining
  ques_ans = fill_gap(id, subject, topic, ques_type, question_types[1])
  for k in ques_ans[0].split("\n"):
      st.write(k)
  # st.write(ques_ans[0])
  if len(ques_ans[2])>0:
    for image in ques_ans[2]:
      st.image(image, width=400) # Manually Adjust the width of the image as per requirement
    
  ques = ques_ans[0]
  correct_ans = ques_ans[1]
  st.session_state.ques=ques
  st.session_state.correct_ans=correct_ans.lower()

student_ans = st.text_input("Type your answer (clear your ans before getting new question)")
st.session_state.student_ans=student_ans.strip().lower()

if len(st.session_state.student_ans)>0:
  if stem(st.session_state.student_ans)==stem(st.session_state.correct_ans) or similar(st.session_state.student_ans,st.session_state.correct_ans)>=0.9:
    st.balloons()
    st.write("Question:")
    for k in st.session_state.ques.split("\n"):
      st.write(k)
    
    st.write("Result:")
    st.write(f"{inspire()} Absolutely correct.")
    st.write(f"Correct answer is {st.session_state.correct_ans}")
    st.session_state.score=st.session_state.score+10
    st.write(f"Your total score {st.session_state.score}")
  else:
    st.write("Question:")
    for k in st.session_state.ques.split("\n"):
      st.write(k)
    
    st.write("Result:")
    st.write(f"Incorrect. Please revise the chapter.")
    st.write(f"Correct answer is {st.session_state.correct_ans}")
    st.session_state.score=st.session_state.score-10
    st.write(f"Your total score {st.session_state.score}")

