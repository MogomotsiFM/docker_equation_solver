FROM public.ecr.aws/lambda/python:3.11 as development

RUN rpm -q yum

RUN yum -y install git
RUN yum -y install openssh

RUN yum -y install zip

RUN git clone https://github.com/MogomotsiFM/equation_solver.git .

# Install the specified packages
RUN pip install -r requirements.txt

RUN python setup.py build

RUN python setup.py install

# Copy function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

# Run the unit tests
RUN coverage run -m pytest  --junit-xml=unit-tests.xml 
RUN coverage html
RUN zip -r htmlcov.zip htmlcov


ENTRYPOINT ["/bin/bash", "-l", "-c", "ls"]

# Generate reports
FROM scratch AS reporter
# WORKDIR ${LAMBDA_TASK_ROOT}/reports
COPY --from=development /var/task/htmlcov.zip /code_coverage.zip
COPY --from=development /var/task/unit-tests.xml /unit_tests.xml

ENTRYPOINT ["/bin/bash", "-l", "-c", "ls"]


# Create the production image
FROM public.ecr.aws/lambda/python:3.11 as production

#WORKDIR ${LAMBDA_TASK_ROOT}
COPY --from=development ${LAMBDA_TASK_ROOT} .

COPY --from=development ${LAMBDA_TASK_ROOT}/requirements.txt .

# Install the specified packages
RUN pip install -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.handler" ]