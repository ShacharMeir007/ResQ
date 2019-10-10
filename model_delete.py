from ibm_watson import VisualRecognitionV3
from ibm_watson import ApiException

'''
this script deletes a classifier from the IBM cloud
'''

# create IMB visual recognition object
visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='mUOB4w-I_VKBFR-1QQwlWB9vJepEJ4Z7SIudvwd_n4CY')


# delete the classifier with the given classifier_id from the IBM cloud
def delete_model(classifier_id):
    visual_recognition.delete_classifier(classifier_id)


try:
    delete_model('faces_1642978691')
except ApiException as ex:
    print("can't delete" + ex.message)
