# notifier

Simple project to send notifications using Pushover. 

This will deploy a Lambda function and SNS topic. The Lambda function is subscribed to the SNS topic so any messages sent to this SNS topic will be sent to the user using Pushover.

The credentials for Pushover are kept in AWS Parameter Store. The values are added manually in the console to keep them out of state and version control, this would ideally be handled by some kind of Secret Store. 