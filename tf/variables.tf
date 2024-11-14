variable "region" {
  type        = string
  description = "AWS region to deploy the application in"
}

variable "project_name" {
  type        = string
  description = "Name of the project for this application"
}

variable "runtime" {
  type        = string
  description = "The runtime for the Lambda function"
}

variable "pushover_parameters" {
  type        = map(any)
  description = "The parameters to store in Parameter Store"
  default = {
    user  = {}
    token = {}
  }
}