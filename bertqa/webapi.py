from flask import Flask
from flask import request
import os
import pandas as pd
from ast import literal_eval

from cdqa.utils.converters import pdf_converter
from cdqa.utils.filters import filter_paragraphs
from cdqa.pipeline import QAPipeline
from cdqa.utils.download import download_model




# df = pdf_converter(directory_path='./data/pdf/')

jdfshdf = ["The Graduate Record Examinations (GRE) is a standardized test that is an admissions requirement for many graduate schools[7] in the United States and Canada[8]. The GRE is owned and administered by Educational Testing Service (ETS).[9] The test was established in 1936 by the Carnegie Foundation for the Advancement of Teaching.[10]",

"According to ETS, the GRE aims to measure verbal reasoning, quantitative reasoning, analytical writing, and critical thinking skills that have been acquired over a long period of learning. The content of the GRE consists of certain specific algebra, geometry, arithmetic, and vocabulary sections. The GRE General Test is offered as a computer-based exam administered at Prometric testing centers. In the graduate school admissions process, the level of emphasis that is placed upon GRE scores varies widely between schools and departments within schools. The importance of a GRE score can range from being a mere admission formality to an important selection factor.",

"The GRE was significantly overhauled in August 2011, resulting in an exam that is not adaptive on a question-by-question basis, but rather by section, so that the performance on the first verbal and math sections determines the difficulty of the second sections presented. Overall, the test retained the sections and many of the question types from its predecessor, but the scoring scale was changed to a 130 to 170 scale (from a 200 to 800 scale).[11]",

"The cost to take the test is US$205,[5] although ETS will reduce the fee under certain circumstances.[6] It also provides financial aid to those GRE applicants who prove economic hardship.[12] ETS does not release scores that are older than five years, although graduate program policies on the acceptance of scores older than five years will vary."]
data = [['123', jdfshdf]] 
df = pd.DataFrame(data, columns = ['title', 'paragraphs']) 


df.head()
cdqa_pipeline = QAPipeline(reader='./models/bert_qa_vCPU-sklearn.joblib', max_df=1.0)




app = Flask(__name__)

@app.route('/train')
def train():
   tr = request.args.get('tr').split(',')
   # print(tr)
   # Fit Retriever to documents


   # Send model to GPU
   # cdqa_pipeline.cuda()

   # Fit Retriever to documents
   # print(df)
   # print(df['paragraphs'].loc[0] )
   print(tr)
   df['paragraphs'].loc[0] = tr
   print(df)
   cdqa_pipeline.fit_retriever(X=df)
   query = 'loss 2014'
   prediction = cdqa_pipeline.predict(X=query)

   return prediction[0]


@app.route('/predict')
def predict():
   tr = request.args.get('tr')
   # print(tr)
   # Fit Retriever to documents

   # cdqa_pipeline = QAPipeline(reader='./models/bert_qa_vCPU-sklearn.joblib', max_df=1.0)

   # Send model to GPU
   # cdqa_pipeline.cuda()

   # Fit Retriever to documents
   # print(df)
   # print(df['paragraphs'].loc[0] )
   # print(df)
   # df['paragraphs'].loc[0] = [tr,tr,tr]
   # print(df)
   # cdqa_pipeline.fit_retriever(X=df)
   query = tr
   prediction = cdqa_pipeline.predict(X=query)
   
   return prediction[0]


@app.route('/')
def hello_world():
   return prediction[0]

if __name__ == '__main__':
   app.run()