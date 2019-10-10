import json
from ibm_watson import VisualRecognitionV3
'''
this script creates the IBM classifier "faces" on the cloud
'''

# create IMB visual recognition object
visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='mUOB4w-I_VKBFR-1QQwlWB9vJepEJ4Z7SIudvwd_n4CY')

# creates the classifier on the IBM cloud
with open('./portman.zip', 'rb') as portman, open(
        './seinfeld.zip', 'rb') as seinfeld:
    model = visual_recognition.create_classifier(
        'faces',
        positive_examples={'portman': portman, 'seinfeld': seinfeld}
    ).get_result()

print(json.dumps(model, indent=2))


