from google.cloud import videointelligence


# This function is triggered when a file is added to a bucket
# It will check if the file is a video, if it is, it will send it to the video intelligence API
def file_added_to_bucket(event, context):
    file_type = event["name"].split(".")[-1]
    if file_type == "mp4":
        procees_video( event, context)

    else:
        print("Not a video")
        



# creating a client -- this is the video intelligence API
video_client = videointelligence.VideoIntelligenceServiceClient()

# This function will process the video and send it to the video intelligence API
def procees_video( event, context):
    # The name of the video file to analyze
    file_to_analyze = f"gs://{event['bucket']}/{event['name']}"


    # The path to the location of the results
    # This will be a json file
    output_path = "gs://results_ojt_video_analysis/{}.json".format(event['name'])

    features = [ # This is the features that will be used to analyze the video
    videointelligence.Feature.OBJECT_TRACKING,
    videointelligence.Feature.LABEL_DETECTION,
    videointelligence.Feature.SHOT_CHANGE_DETECTION,
    videointelligence.Feature.SPEECH_TRANSCRIPTION,
    videointelligence.Feature.LOGO_RECOGNITION,
    videointelligence.Feature.EXPLICIT_CONTENT_DETECTION,
    videointelligence.Feature.TEXT_DETECTION,
    videointelligence.Feature.FACE_DETECTION,
    videointelligence.Feature.PERSON_DETECTION
    ]

    # 1. Speech transcription
    transcript_config = videointelligence.SpeechTranscriptionConfig(
    language_code="en-US", enable_automatic_punctuation=True)

    # 2. Person detection
    person_config = videointelligence.PersonDetectionConfig(
        include_bounding_boxes=True,
        include_attributes=False,
        include_pose_landmarks=True,)

    # 3. Face detection
    face_config = videointelligence.FaceDetectionConfig(
        include_bounding_boxes=True, include_attributes=True)

    # this is the video context, it will be used to analyze the video
    # using the features that we have set (1,2,3)
    video_context = videointelligence.VideoContext(
        speech_transcription_config=transcript_config,
        person_detection_config=person_config,
        face_detection_config=face_config)

    # This will send the video to the video intelligence API
    # It will return an operation, which will be used to check the status of the video
    operation = video_client.annotate_video(
        request={"features": features,
                "input_uri": file_to_analyze,
                "output_uri": output_path,
                "video_context": video_context}
    )
    # now we saved the output of the video to a json file

    print("\nProcessing video.", operation)
    




