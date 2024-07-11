# Use the AWS base image for Python 3.12
FROM public.ecr.aws/lambda/python:3.12

# Install build-essential compiler and tools
RUN microdnf update -y && microdnf install -y gcc-c++ make

# Copy the requirements file
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the requirements
RUN pip install -r requirements.txt

# Copy the Lambda function code
COPY travelAgent.py ${LAMBDA_TASK_ROOT}

# Set permission to make the file executable
RUN chmod +x travelAgent.py

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "travelAgent.lambdaHandler" ]