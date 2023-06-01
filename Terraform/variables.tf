#---- variables.tf/root ----

#Variable Declaration
variable "bucket_name" {
  type = list
  default  = ["terraform-test-jps3-1", "terraform-test-jps3-2", "terraform-test-jps3-3"]
}