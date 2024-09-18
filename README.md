# Phishing-Detection
### Project Proposal
##### Comments from Presentation
1. Can the web app for the model take over to actively prevent users from clicking links labeled as phishing?
2. What are the accuracy thresholds?
3. Choose a paper/project to replicate and enhance.
4. Compare the project to solutions that do not involve a large language model.
#### Problem 
Cybercrime is increasing alarmingly, and the most common of these crimes is phishing. The current solutions can leave potential phishing links unlabeled or just labeled as spam, automatic detection needs to be constantly updated, and a large amount of human error is involved. These phishing crimes can cost companies and individuals millions, all because someone clicked a link they should not have.
#### Solution
Our solution would be to create a model that can classify emails as 'phishing', 'spam', or legitimate in real time and accurately label these emails as a part of an existing email applications classification system.
Pretrained transformers (BERT, GPT) can be fine-tuned to create embeddings for phishing classification, and features from text and metadata can be used for finetuning. Data sets such as SpamAssassin or PhishTank can be used to get these features. A multi-modal model can combine text-based transformer models with other types of data (URL features, metadata) for a more robust phishing detection system.
The model can be implemented into a web app using Flask or a similar framework and be integrated into an email platform. The model can then label emails and automatically report phishing attempts. Specifically, we will be extending on the paper "Multimodel Phishing URL Detection Using LSTM,Bidirectional LSTM, and GRU Models" to have a real-time detection system rather than it solely being an offline system. For this objective we will likely be focusing on the GRU model of the multimodel system as it has a lower latency and is a lighter model.
#### Evaluation
We can determine the accuracy by using real-time testing on email streams and comparison between baseline models, such as BERT or GPT-2. Metrics such as the F1 score can be calculated to determine accuracy. Some existing solutions are human judgment, GPT and other baseline models, as well as non-LLM solutions. Our model can be compared against these for accuracy. The current accuracy thresholds are based on the model used. LSTM: 96.9%, Bi-LSTM: 99%, GRU: 97.5%
#### Feedback
After presenting this to the class, we received some very helpful feedback. First, we need to consider allowing the model to take over for the user, so it can actively prevent a user from clicking on phishing links. Also, we needed to determine a threshold for accuracy, or a goal for how correct we would like our model to be. We should also consider a previous paper to base our project on, and take this work and enhance it. We should find a project with available code, and we can evaluate our model the same way the previous researchers did. Lastly, we should also consider comparing our model against some non-LLM solutions.
#### References 
Roy, Sanjiban Sekhar, et al. “Multimodel Phishing URL Detection Using LSTM, Bidirectional LSTM, and GRU Models.” MDPI, Multidisciplinary Digital Publishing Institute, 21     
Nov. 2022, www.mdpi.com/1999-5903/14/11/340. 
