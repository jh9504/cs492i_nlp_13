# cs492i_nlp_team13
KAIST & NAVER Deep Learning Lecture

\# korquad-open-cs492I
KorQuad-Open Baseline Code for KAIST CS492I 2020 Fall

## Original Author
Seonhoon Kim (Naver)

## Edited by
KAIST cs492i_nlp_team13

Hyeonuk Nam, Jinhyuk Ryu

## Usage
This project is done by two KAIST students (Hyeonuk Nam, Jinhyuk Ryu)
for the class of CS492 - Deep Learning Project [NLP Korquad Task]
Thanks to cooperation from NAVER, NSML Platform (enables usage of GPUs and CPUs on the server)
 - https://ai.nsml.navercorp.com/intro

## Description
This README.md will help you with how to run our code using NSML platform

1. You will need to either download or pull all the codes in the repositry
2. Install NSML following the official document from NAVER : https://n-clair.github.io/ai-docs/_build/html/en_US/index.html
3. We two have used different programs to approach nsml server. Ubuntu and windows cmd with nsml installed according to the document above.
4. Upload our files to whichever program you prefer, and login to nsml account by typing $nsml login
5. type your ID and PW. (In our case, it was the github account)

# Files
General Help with what each files contain:

run_nsml.sh
- 
The bash file that sets our training settings such as:
model: koelectra,  epochs: 2,  train and eval batch sizes: 24

run_squad.py
- 
The main file that contains the training implementation codes to run, select paragraphs, evaluate, and predict.

open_squad.py
- 


open_squad_metrics.py
- 


setup.py
- 
contains prerequisite libraries if used additionally to what nsml provides by default

## For Training
 - assuming you are allocated with at least one GPU, execute bash file - (for nsml: ./run_nsml.sh   for local: ./run_local.sh)
We recommend running run_nsml.sh bash file since you are using the dataset already uploaded on nsml server.

## Our pretrained model which produced best score on nsml leader board
 - nsml kaist0013/korquad-open-ldbd3/126 electra_last
