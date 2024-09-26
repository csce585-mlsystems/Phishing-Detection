# Replicating Multimodal phishing detection and implementing a real-time evaluation Experiment Setup Discussion

## Key Challenge 
- Developing an accurate and robust model phishing detection
- incorporating multiple modes for more robust detection
- Real-time detection

## Initial Experiment
un a phishing email data set through a baseline model or non-llm approach and see the accuracy of the results. We can compare the performance of a state-of-the-art phishing detection model to that of a baseline to show the importance of modern models for phishing detection. 
Metrics we need to show are F1 score, meeting our accuracy thresholds, and improved accuracy over baseline models and non-LLM methods.  

## Goals
Our first goal is to create an evaluation environment to create valuable data that can be used for a final research paper. The environment we’re going to use is Jupyter notebook. 
The key challenge we are trying to address is accurate and robust phishing detection in real time.  
Our primary goal is to achieve real-time detection with high accuracy and low latency. The experiment will involve observing how well the model can detect phishing URLs in emails given a real-time environment where we will measure the latency and overall success with varying batch sizes. This will result in meaningful data that will display the trade-off between accuracy and latency, producing crucial evaluation metrics.


## Steps: 

    Set up phishing detection model in a Jupyter Notebook. 

    Use malicious URL dataset, to simulate phishing detection. 

    Define the evaluation metrics  

    Collect the performance data including during real-time detection 

## Design Sketch
### Independent Variables
- Email Content
- URLs
- Attachments
- Sender Info
- Historical Data

### Dependent Variables
- Phishing Label (Phishing, Spam, Legit)

### Control Groups
- Real Emails
- Dataset of previously classified phishing, spam, and legit emials
- Time-based Control
 
