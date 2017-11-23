# NumpyLoadTxt-Lambda
The function demonstrates the usage of Numpy.loadtxt function in AWS Lambda

# Setup
[*] Download the code and install numpy by running "pip install numpy -t <path_to_project_dir>"
[*] Zip the file using the command "zip -r lambda.zip ."
[*] Upload the zip file to S3 bucket
[*] Download the template.yml file and import into Cloudformation. Provide the location of the zip file and bucket where you will be uploading CSV files. 
[*] Cloudformation will create lambda function with full S3 permission. The function will be triggered when CSV file is uploaded to the bucket.
