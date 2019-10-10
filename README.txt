README

    ResQ is a recognition software designed to make finding people during crisis more efficient.
    The software uses image inputs from rescue and medical teams to make a learning model which with
    an input image the software can match and locate the person in the image

SERVER
    the server manages image transfers to the Visual recognition tool
    and data transfers to the database
VISUAL RECOGNITION
    the visual recognition works with the IBM tools
    we built function for creating updating and search a learning model
    the Server uses this function to analyze it's stream and talk to the IBM cloud

DATABASE
    the database stores location information about rescue's of the disaster

HACKATHON
    for the current prototype we've prepared the visual recognition tool
    the server and the database although we don't have user interfaces for
    inputs of images and we assume all input are valid