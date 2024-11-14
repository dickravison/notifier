#Get current account info
data "aws_caller_identity" "current" {}

#Get data for requests lambda layer
data "aws_lambda_layer_version" "layer" {
  layer_name = "requests"
}

#Create zip archive of source code
data "archive_file" "notifier" {
  type        = "zip"
  source_dir  = "../src/notifier"
  output_path = "../src/notifier.zip"
}

#Get key ID for SSM key
data "aws_kms_key" "ssm" {
  key_id = "alias/aws/ssm"
}