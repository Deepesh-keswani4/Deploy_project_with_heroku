import json
import app as model
from flask import Flask
from flask import request
  
app = Flask(__name__)
  
@app.route('/api', methods = ['POST'])
def postJsonHandler():
    data = request.json
    result = model.cosine_function(data['text1'], data['text2'])
    return json.dumps({"similarity_score": result})
  
app.run(host='0.0.0.0', port=3300)