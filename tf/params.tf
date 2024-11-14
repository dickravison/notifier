#Replace the values in the console to keep them out of state + version control
resource "aws_ssm_parameter" "user" {
  name  = "/notifier/user"
  type  = "String"
  value = "PLACEHOLDER"

  lifecycle {
    ignore_changes = [value]
  }
}

resource "aws_ssm_parameter" "token" {
  name  = "/notifier/token"
  type  = "String"
  value = "PLACEHOLDER"

  lifecycle {
    ignore_changes = [value]
  }
}