# -*- coding: utf-8 -*-
"""fillgap.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Kg678a28BCkD9ZGkmcQnoCd73P8XGCjp
"""

# Writing helper functions

# writing text pre-processing function
def text_process(text):
  try:
    text = text.lower()    # converting to lowercase
    import string
    text =[char for char in text if char not in string.punctuation] # removing punctuations
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
    text=' '.join(text)

  except:
    text=text

  return text

def cl_lst():
  try:
    # Importing libraries
    import numpy as np
    import pandas as pd
    # global c
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
  return result

def medium_lst(cl):
  try:
    # Importing libraries
    import numpy as np
    import pandas as pd
    # global c
    # Reading student data as pandas df
    gsheetid = "1g1uWDGjJ1aGRXtJVkISj9qwq-DJmnzTS"
    sheet_name = "Sheet1" # Student should not change the sheet name

    # Converting google sheet to csv
    gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)

    # Creating student data df
    student_data = pd.read_csv(gsheet_url)
  
    result=list(student_data[(student_data.Class==cl)]["Medium"].unique())
    result = [x for x in result if str(x) != 'nan']
    
  except:
    result=[]
  return result

def id_lst(cl,medium):
  try:
    # Importing libraries
    import numpy as np
    import pandas as pd
    # global c
    # Reading student data as pandas df
    gsheetid = "1g1uWDGjJ1aGRXtJVkISj9qwq-DJmnzTS"
    sheet_name = "Sheet1" # Student should not change the sheet name

    # Converting google sheet to csv
    gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)

    # Creating student data df
    student_data = pd.read_csv(gsheet_url)
  
    result=list(student_data[(student_data.Class==cl) & (student_data.Medium==medium)]["ID"].unique())
    result = [x for x in result if str(x) != 'nan']
    
  except:
    result=[]
  return result

def subject_lst(id):
  try:
    # Importing libraries
    import numpy as np
    import pandas as pd
    # global c
    # Reading student data as pandas df
    gsheetid = "1g1uWDGjJ1aGRXtJVkISj9qwq-DJmnzTS"
    sheet_name = "Sheet1" # Student should not change the sheet name

    # Converting google sheet to csv
    gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)

    # Creating student data df
    student_data = pd.read_csv(gsheet_url)

    # Creating individual student df
    # Getting google sheet id
    gsheetid = student_data[(student_data["ID"]==id) & (student_data["Status"]=="Active")]["Concept_link"].values[0].replace("https://docs.google.com/spreadsheets/d/","").split("/")[0]
    sheet_name = "Concepts" # Student should not change the sheet name

    # Converting google sheet to csv
    gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)

    # Creating individual student data df
    individual_student_data = pd.read_csv(gsheet_url)
    individual_student_data = individual_student_data[(individual_student_data["Class"]==student_data[(student_data["ID"]==id)]["Class"].values[0])]

    result=list(individual_student_data["Subjects"].unique())
    result = [x for x in result if str(x) != 'nan']
    
  except:
    result=[]

  return result

def topic_lst(id, subject):
  '''
  id=int
  subject=list of subjects
  '''
  try:
    # Importing libraries
    import numpy as np
    import pandas as pd
    # global c
    # Reading student data as pandas df
    gsheetid = "1g1uWDGjJ1aGRXtJVkISj9qwq-DJmnzTS"
    sheet_name = "Sheet1" # Student should not change the sheet name

    # Converting google sheet to csv
    gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)

    # Creating student data df
    student_data = pd.read_csv(gsheet_url)

    # Creating individual student df
    # Getting google sheet id
    gsheetid = student_data[(student_data["ID"]==id) & (student_data["Status"]=="Active")]["Concept_link"].values[0].replace("https://docs.google.com/spreadsheets/d/","").split("/")[0]
    sheet_name = "Concepts" # Student should not change the sheet name

    # Converting google sheet to csv
    gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)

    # Creating individual student data df
    individual_student_data = pd.read_csv(gsheet_url)
    individual_student_data = individual_student_data[(individual_student_data["Class"]==student_data[(student_data["ID"]==id)]["Class"].values[0])]

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

# Writing main function

def fill_gap(id, subject, topic):
  '''
  id=int
  subject=list
  topic=list
  '''
  try:
    # Importing libraries
    import numpy as np
    import pandas as pd
    # global c
    # Reading student data as pandas df
    gsheetid = "1g1uWDGjJ1aGRXtJVkISj9qwq-DJmnzTS"
    sheet_name = "Sheet1" # Student should not change the sheet name

    # Converting google sheet to csv
    gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)

    # Creating student data df
    student_data = pd.read_csv(gsheet_url)

    # Creating individual student df
    # Getting google sheet id
    gsheetid = student_data[(student_data["ID"]==id) & (student_data["Status"]=="Active")]["Concept_link"].values[0].replace("https://docs.google.com/spreadsheets/d/","").split("/")[0]
    sheet_name = "Concepts" # Student should not change the sheet name

    # Converting google sheet to csv
    gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)

    # Creating individual student data df
    individual_student_data = pd.read_csv(gsheet_url)
    individual_student_data = individual_student_data[(individual_student_data["Class"]==student_data[(student_data["ID"]==id)]["Class"].values[0])]

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

    if subject_data.shape[0]!=0:
      # Random selection of concept
      index_lst=list(subject_data.index)
      import random
      random.shuffle(index_lst)
      original_text=subject_data.documents[index_lst[0]]

      # Generating answer and question
      # Random selection of question
      import random
      text=text_process(original_text)
      if len(text.split())>0:
        lst=text.split()
        random.shuffle(lst)
        ans=lst[0]
        
        ans_index=original_text.lower().split().index(ans)
        original_text=original_text.split()
        original_text[ans_index]="_____"
        ques=" ".join(original_text)
        
      else:
        ques="Ask question again. Concept found is very poor in strength:("
        ans=""
      
    else:
      ques="You have no concept record for this subject"
      ans=""
  except:
    ques="Please provide correct id, subject and topic"
    ans=""
  
  return ques, ans

# def check(student_ans, ans):
#   student_ans=student_ans.lower()
#   if student_ans==ans:
#     # c=c+10
#     result=f"Awesome! Absolutely correct.\nCorrect answer is {ans}" # \nYour total score: {c}
#   else:
#     # c=c-10
#     result=f"Incorrect. Please revise the chapter.\nCorrect answer is {ans}" # \nYour total score: {c}
#   return result

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

cl = st.selectbox("Class", cl_lst()) 

medium = st.selectbox("Medium", medium_lst(cl)) 

id = st.selectbox("Your ID", id_lst(cl, medium)) 

subject = st.multiselect("Subject ", subject_lst(id)) 

topic = st.multiselect("Topic ", topic_lst(id, subject))

add_bg_from_local('fillgap.png')   

question= st.button("Get Question")  

if "score" not in st.session_state:
  st.session_state.score=0

if question: # when any button is pressed in streamlit,code runs from the begining
  ques_ans = fill_gap(id, subject, topic)
  st.write(ques_ans[0])
  ques = ques_ans[0]
  correct_ans = ques_ans[1]
  st.session_state.ques=ques
  st.session_state.correct_ans=correct_ans

student_ans = st.text_input("Type your answer (clear your ans before getting new question)")
st.session_state.student_ans=student_ans

if len(st.session_state.student_ans)>0:
  if st.session_state.student_ans==st.session_state.correct_ans:
    st.write("Question:")
    st.write(st.session_state.ques)
    st.write("Result:")
    st.write(f"Awesome! Absolutely correct.\nCorrect answer is {st.session_state.correct_ans}")
    st.session_state.score=st.session_state.score+10
    st.write(f"Your total score {st.session_state.score}")
  else:
    st.write("Question:")
    st.write(st.session_state.ques)
    st.write("Result:")
    st.write(f"Incorrect. Please revise the chapter.\nCorrect answer is {st.session_state.correct_ans}")
    st.session_state.score=st.session_state.score-10
    st.write(f"Your total score {st.session_state.score}")
  
  # result=check(st.session_state.student_ans, st.session_state.correct_ans)
  # st.session_state.result=result
  # st.write("Question:")
  # st.write(st.session_state.ques)
  # st.write("Result:")
  # st.write(st.session_state.result)



st.write(st.session_state)

