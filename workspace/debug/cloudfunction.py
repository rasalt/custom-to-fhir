def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    from google.cloud import pubsub_v1
    import json
    # TODO(developer)
    project_id = "smede-276406"
    topic_id = "workspace"

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)

    testdata = {"fname": "John", "lname": "Smith", "dob": "1970-01-02", "sex": "male"}
    testdata_str = json.dumps(testdata)
    # Data must be a bytestring
    data = testdata_str.encode("utf-8")
    # Add two attributes, origin and username, to the message
    future = publisher.publish(
        topic_path, data
    )
    print(future.result())

    print(f"Published message {testdata_str} custom attributes to {topic_path}.")
    return f'Hello World!'

