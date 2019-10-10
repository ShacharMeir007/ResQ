import json
from ibm_watson import VisualRecognitionV3

'''
this scripts lists the classifier that currently on the IBM cloud
'''

# create IMB visual recognition object
visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='mUOB4w-I_VKBFR-1QQwlWB9vJepEJ4Z7SIudvwd_n4CY')
# list the classifier that currently on the IBM cloud
classifiers = visual_recognition.list_classifiers(verbose=True).get_result()
print(json.dumps(classifiers, indent=2))

