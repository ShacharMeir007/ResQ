import json
from ibm_watson import VisualRecognitionV3

'''
this module defines the search function on the IBM cloud for the server
the search function is used in the image server
'''

# create IMB visual recognition object
visual_recognition = VisualRecognitionV3(
    '2018-03-19',

    url="https://gateway.watsonplatform.net/visual-recognition/api",
    iam_apikey='mUOB4w-I_VKBFR-1QQwlWB9vJepEJ4Z7SIudvwd_n4CY')


# classifies the image input to the appropriate class in my classifiers
def search(img_name: str):
    with open(img_name, 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file,
            threshold='0.5',
            owners=['me']
        ).get_result()
        result = match_names(json.dumps(classes, indent=2))
        print(result)
        return result


# converting the IBM classify result massage to result tuple
def match_names(classes_massage):
    final_name = classes_massage.split("classes")
    final_name = final_name[1].split("classifier_id")
    final_name = final_name[0].split("}")
    final_name = final_name[0].split("{")
    final_name = final_name[1].strip("\n")
    final_name = final_name.strip(" ")
    final_name = final_name.split(",")
    name = final_name[0].split(':')[1]
    score = final_name[1].split(':')[1].strip("\n")
    final_name = (name.strip('"').strip(' ""'), float(score))
    return final_name

