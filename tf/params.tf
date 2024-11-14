#Replace the values in the console to keep them out of state + IaC
resource "aws_ssm_parameter" "pushover" {
  for_each = var.pushover_parameters

  name  = "/${var.project_name}/${each.key}"
  type  = "SecureString"
  value = "PLACEHOLDER"

  lifecycle {
    ignore_changes = [value]
  }
}