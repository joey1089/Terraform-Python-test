#---- main.tf/root -----

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.63"
    }
  }
}

provider "aws" {  
  region  = "us-east-1"
}

#Resource to create s3 bucket
resource "aws_s3_bucket" "demo_bucket" {
  count = length(var.bucket_name)
  bucket = var.bucket_name[count.index]
}