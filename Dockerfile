FROM python:3.11
# FROM python:3.12.0b4-alpine3.18

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN pip install -e .


# sudo apt-get update
# sudo apt-get install pandoc
# sudo apt-get -y install texlive-xetex texlive-fonts-recommended texlive-plain-generic pandoc

ENTRYPOINT [ "citros" ]

# run
# docker run citros:latest run ... 
# docker run citros:latest data create 
