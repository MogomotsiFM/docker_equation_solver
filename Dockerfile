FROM public.ecr.aws/lambda/python:3.11

RUN rpm -q yum

RUN yum -y install git
RUN yum -y install openssh

RUN git clone https://github.com/MogomotsiFM/equation_solver.git .

RUN pwd && ls

# Install the specified packages
RUN pip install -r requirements.txt

RUN python setup.py build

RUN python setup.py install

# Copy function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.handler" ]