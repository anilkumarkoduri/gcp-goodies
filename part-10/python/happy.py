from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw
from google.cloud import storage
import datetime
import csv

bucket_name = "softwaremill"
csv_file = "softwaremill.csv"
storage_client = storage.Client() #.from_service_account_json('/home/kris/Downloads/happy.json')

def getFiles(bucket_name):
    blobs = storage_client.list_blobs(bucket_name)
    return blobs
    #     date_str = blob.name[:10]
    #     date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    #     print(date_obj)


def detect_face(bucket_name, image_name):
    print("Detecting faces for: " + image_name)
    """Uses the Vision API to detect faces in the given file.
    Args:
        face_file: A file-like object containing an image with faces.
    Returns:
        An array of Face objects with information about the picture.
    """
    joy_likelihoods = []
    client = vision.ImageAnnotatorClient()
    response = client.annotate_image({'image': {'source': {'image_uri': 'gs://'+bucket_name+'/'+image_name}},'features': [{'max_results': 50, 'type': vision.enums.Feature.Type.FACE_DETECTION}]})
    for annotation in response.face_annotations:
        joy_likelihoods.append(annotation.joy_likelihood)
    return joy_likelihoods


def getLikelihoodsOfJoy():
    d = {}
    blobs = getFiles(bucket_name)
    # blobs = list(blobsx)[:3]
    for blob in blobs:
        name = blob.name
        date_str = str(name[:10])
        likelihoods = detect_face(bucket_name, name)
        if date_str in d:
            d[date_str] += likelihoods
        else:
            d[date_str] = likelihoods
    return d

def createCSV(csv_file, rows):
    with open(csv_file, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Day', 'Level', 'Count'])
        for row in rows:
            filewriter.writerow(row)

def getCSVLines(likelihoods):
    rows = []
    for key in likelihoods:
        values = likelihoods[key]
        levels = set(values)
        for level in levels:
            count = values.count(level)
            rows.append([key, level, count])
    return rows
# print(getLikelihoodsOfJoy())
# blobs = getFiles(bucket_name)
# createCSV(csv_file)
likelihoods = getLikelihoodsOfJoy()
rows = getCSVLines(likelihoods)
createCSV(csv_file, rows)