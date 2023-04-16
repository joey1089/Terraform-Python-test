#---- variables.tf/root ----

#Variable Declaration
variable "bucket_name" {
  type = list
  default  = ["testdemo-jps3-1", "testdemo-jps3-2", "testdemo-jps3-3"]
}