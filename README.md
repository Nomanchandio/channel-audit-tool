# YouTube Channel Info Retrieval

This project contains the source code for a Lambda function that retrieves information about a YouTube channel using the YouTube Data API. 

## Functionality

The Lambda function `lambda_handler` takes an event and context as input, where the event includes the channel ID for which the information is to be retrieved. The function queries the YouTube Data API to fetch details such as channel title, description, published date, subscriber count, view count, and video count.

## Deployment

To deploy the Lambda function, you need to set up the necessary environment variables, including the YouTube Data API key (`API_KEY`). Ensure that the API key has the appropriate permissions to access the YouTube Data API.

After configuring the environment variables, deploy the function to your AWS Lambda environment using the deployment method of your choice, such as the AWS Management Console or AWS CLI.

## Usage

To use this Lambda function:

1. Deploy the function to your AWS Lambda environment.
2. Invoke the function by passing the channel ID as part of the event data.
3. Receive the channel information as the function's response.

## Sample Event Data

Here is an example of a sample event data that can be sent to the Lambda function:

```json
{
    "channel_id": "UC_x5XG1OV2P6uZZ5FSM9Ttw"
}
Replace the channel_id value with the actual ID of the YouTube channel for which you want to retrieve information.

Response Format
The Lambda function returns a JSON response with the channel information in the following format:

json
{
    "message": "Your channel audit info",
    "data": {
        "channel_title": "Example Channel",
        "channel_description": "This is a sample channel description.",
        "published_at": "2023-04-01T12:00:00Z",
        "subscriber_count": "1000",
        "view_count": "50000",
        "video_count": "100"
    }
}

## Error Handling
The Lambda function handles various error scenarios, such as missing or invalid channel ID in the event data or failure to retrieve channel information from the YouTube Data API. If any error occurs during request processing, an appropriate error response will be returned.

Credits
This Lambda function was created by [Your Name] and is provided under the [license name] license. Feel free to use and modify it according to your requirements.