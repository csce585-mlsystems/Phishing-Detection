# Phishing-Detection

### How to replicate results

#### Train models
First, clone this repository onto your local machine
Start by installing all necessary packages in the requirements.txt file, as well as react and node.js for the web app.
Next, each model can be trained and tested for accuracy by running their respective Jupyter notebooks.
#### Tun Webapp
The react web app can be run by navigating to the app directory and running 'npm start' in the terminal.
Then, open another terminal window, navigate to the webapp_backend directory, and edit webapp_ModelAPI to whichever model you desire for the webapp. It will be the GRU model by default.
Start the backend server by running webapp_modelAPI in Python. 
Navigate to localhost:3000 to check single URLs with the model to see if they are phishing or benign.
From here, the user can input a single link to check its safety and see their link history.
The user can also connect their Gmail account, where they will be navigated to log in and authenticate with Gmail, once this is completed, they can navigate back to the react app to see recent links in emails and their classifications!
#### Load Bearing Testing
Load bearing testing can be done using locust by simply starting the backend server as shown above, then opening a new terminal and running 'locust -f locustfile.py --host=http://localhost:5000'
From here, navigate to the locust dashboard at localhost:8089, and then run locust testing as desired

Thanks!

### Project Proposal
##### Comments from Presentation
1. Can the web app for the model take over to actively prevent users from clicking links labeled as phishing?
2. What are the accuracy thresholds?
3. Choose a paper/project to replicate and enhance.
4. Compare the project to solutions that do not involve a large language model.
#### Problem 
Cybercrime is increasing alarmingly, and the most common of these crimes is phishing. The current solutions can leave potential phishing links unlabeled or just labeled as spam, automatic detection needs to be constantly updated, and a large amount of human error is involved. These phishing crimes can cost companies and individuals millions, all because someone clicked a link they should not have.
#### Solution
We are replicating and extending the research paper “Multimodel Phishing URL Detection Using LSTM, Bidirectional LSTM, and GRU Models.” from the Multidisciplinary Digital Publishing Institute. In this paper, researchers explored how different models detected malicious URLs. The models, listed in the title of the paper, are LSTM, BiLSTM, and GRU-based RNN algorithms. Our extension would be to determine the best model to classify URLs in real time and accurately label these emails as a part of an existing email applications classification system via a web app. The paper simply finds BiLSTM to be the most accurate model, however, latency, efficiency, and robustness are also important to a model working in real-time.
#### Evaluation
We will evaluate each model's accuracy against thresholds from the paper: LSTM: 96.9%, BLSTM: 99%, GRU: 97.5%. F1 score, FPR, and TNR are also important accuracy metrics. For latency, we can see the inference time per URL, as well as end-to-end latency. We can test the model's robustness by stress testing it with simulated data streams, ensuring the model can handle lots of incoming data. The size of the model and accuracy will be favored over latency, as a few milliseconds will not make or break the real-time evaluation of emails.
#### Feedback
After presenting this to the class, we received some very helpful feedback. First, we need to consider allowing the model to take over for the user, so it can actively prevent a user from clicking on phishing links. Also, we needed to determine a threshold for accuracy or a goal for how correct we would like our model to be. We should also consider a previous paper to base our project on, and take this work and enhance it. We should find a project with available code, and we can evaluate our model the same way the previous researchers did. Lastly, we should also consider comparing our model against some non-LLM solutions.
#### References 
Roy, Sanjiban Sekhar, et al. “Multimodel Phishing URL Detection Using LSTM, Bidirectional LSTM, and GRU Models.” MDPI, Multidisciplinary Digital Publishing Institute, 21     
Nov. 2022, www.mdpi.com/1999-5903/14/11/340. 
