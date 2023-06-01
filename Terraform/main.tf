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

resource "aws_s3_bucket" "public_bucket" {
  bucket = "terraform-public-jps3-01"
  
}

# Set S3 policy to public
resource "aws_s3_bucket_public_access_block" "s3-public-set" {
  # count = length(var.bucket_name)
  bucket = aws_s3_bucket.public_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}