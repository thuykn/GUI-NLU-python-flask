# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import os
import json
from flask import Flask
from flask import jsonify

sys.path.append(os.path.join(os.getcwd(),'..'))
import watson_developer_cloud
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features

# In[3]:
app = Flask("NLU App")
 nlu = watson_developer_cloud.NaturalLanguageUnderstandingV1(
   version='2017-02-27',
    username='1cde75f8-52d6-4cff-8737-1ba58975d3e1',
    password='qF0xq5mTkx3e')

# In[6]:

response = nlu.analyze(
    text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
             'Superman fears not Banner, but Wayne.',
    features=[features.Entities(), features.Keywords()])
  
    #version='2017-02-27',
     #username=os.getenv('NATURAL_LANGUAGE_UNDERSTANDING_USERNAME'),
     #password=os.getenv('NATURAL_LANGUAGE_UNDERSTANDING_PASSWORD') )

     print(json.dumps(response, indent=2))

     @app.route("/")
     def eval_default():
        response = nlu.analyze(
              text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
	    	      'Superman fears not Banner, but Wayne.',
              features=[features.Entities(), features.Keywords()])
        return jsonify(response)
# In[ ]:
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=int(os.getenv('PORT',8080)))
