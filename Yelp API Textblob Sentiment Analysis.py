import requests
#imports the requests libraries into python.

api_key = 'eNBkKrZ4F79wLVxAFl-gE79gyHorlNVMwOvx9fxh0N981XDqRFi6N_XmCiaJNZlpuFLSGxNqA1YOOt2r5oVhSJW3KHgUTI2MokCLlI24MpuY8DP0r7Ik1jpT2aJuYnYx'
client_id = '37fegA5zMalFavRhxU7suA'
business_ID = 'tandoori-guys-broken-arrow'
endpoint = 'https://api.yelp.com/v3/businesses/{}/reviews'.format(business_ID)
headers = {'Authorization': 'bearer %s' % api_key}
#Created keys from the yelp developer portal to use in the client and also
#calls the business to get the reviews from the businessID

response = requests.get(url=endpoint, headers=headers)
business_data = response.json()
#Makes the response as a json format to read the reviews

from textblob import TextBlob
counter=0
totalP=0
totalS=0
temp_review = ""
for biz in business_data['reviews']:
    review = biz['text']
    currentP = TextBlob(review).polarity
    currentS = TextBlob(review).subjectivity
    totalP = totalP + currentP
    totalS = totalS + currentS
    counter+=1

P_analysis = totalP/counter
S_analysis = totalS/counter
print('The Polarity for the reviews is: ' + str(P_analysis))
print('The Subjectivity for the reviews is: ' + str(S_analysis))
