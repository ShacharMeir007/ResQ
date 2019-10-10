import model_upload as model_update
import processor as processor

'''
this script search and upload are called from the server to analyze it's inputs
'''


def search(img_name):
    return processor.search(img_name)


def upload(classifier_name, zip_name, person_name):
    return model_update.upload(classifier_name, zip_name, person_name)
