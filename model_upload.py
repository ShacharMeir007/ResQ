import json
from ibm_watson import VisualRecognitionV3
'''
this module defines the upload function to the IBM cloud for the server
the upload function is used in the image server
'''
# create IMB visual recognition object
visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='mUOB4w-I_VKBFR-1QQwlWB9vJepEJ4Z7SIudvwd_n4CY')


# update the classifier_name classifier with the input
def upload(classifier_name, zip_name, person_name):
    with open(str('./' + zip_name + ".zip"), 'rb') as zip:
        updated_model = visual_recognition.update_classifier(
            classifier_id=classifier_name,
            positive_examples={person_name: zip}).get_result()
    print(json.dumps(updated_model, indent=2))
    return None
