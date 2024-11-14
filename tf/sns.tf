resource "aws_sns_topic" "notifier" {
  name = var.project_name
}

resource "aws_sns_topic_subscription" "notifier" {
  topic_arn = aws_sns_topic.notifier.arn
  protocol  = "lambda"
  endpoint  = aws_lambda_function.notifier.arn
}