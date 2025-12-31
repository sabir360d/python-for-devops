import boto3
import json

# Get EC2 Instance Information
def list_ec2_instances():
    """
    Connects to AWS EC2 service
    Returns a list of EC2 instance IDs and their states
    """

    ec2_client = boto3.client("ec2")          # Create EC2 client
    response = ec2_client.describe_instances()  # Call AWS API

    ec2_list = []  # Empty list to store EC2 details

    # AWS returns data in Reservations -> Instances structure
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            ec2_list.append({
                "instance_id": instance["InstanceId"],
                "state": instance["State"]["Name"]
            })

    return ec2_list

# Get S3 Bucket Information
def list_s3_buckets():
    """
    Connects to AWS S3 service
    Returns a list of S3 bucket names
    """

    s3_client = boto3.client("s3")         # Create S3 client
    response = s3_client.list_buckets()    # Call AWS API

    bucket_list = []

    for bucket in response["Buckets"]:
        bucket_list.append(bucket["Name"])

    return bucket_list


# Main Program Starts Here
def main():
    print("Connecting to AWS...\n")

    # Collect AWS resource information
    report = {
        "ec2_instances": list_ec2_instances(),
        "s3_buckets": list_s3_buckets()
    }

    # Print output in terminal
    print("AWS Resource Report")
    print(json.dumps(report, indent=4))

    # Save output to JSON file
    with open("aws_report.json", "w") as json_file:
        json.dump(report, json_file, indent=4)

    print("\nReport successfully saved as aws_report.json")


# This ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
