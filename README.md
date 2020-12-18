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

## Files
General Help with what each files contain:

setup.py 
 -contains prerequisite libraries if used additionally to what nsml provides by default

models.py 
 - contains basic training models - [resnet18, resnet50, densenet121]
Setting for pretrained is turned False, because we want to see how much our code can improve training acc,
not how finely we can tune the pretrained models given.
            
ImageDataLoader_MT.py 
 - Slight change to oringinally given baseline ImageDataLoader.py, which introduced parameter k to
   SimpleImageloader function. The k will allow augmentation to the training data to increase the number of
   training dataset. This file basically allows the main file to pass on train/valid/test loader to the
   train() function.

main_MT_TSA_transform.py 
 - Changed from originally given baseline main.py. We added MeanTeacher method to training function,
 Introduced Time Signal Annealing technique in training function to load and train each epochs with 
 different datasets according to randomized transform selection using the function newly created as 
 well.
 The types of tests we offer are
  1. Different applications of basic settings(we recommend setting A,B,C defined in the code: best result settings we tested):   
   ```
   a) no_trainaug k - number of augmentation for each training data
   b) batchsize - training data batchsize
   c) unlbatchsize - unlabeled data batchsize
   d) epochdrop - epoch of which batch size drops
   e) tbs_d - batchsize for epoch drop
   f) utb_d - batchsize_unlabeled for eopch drop
   g) epochdropdrop - epoch of which batchsize drops again (second drop)
   h) tbs_dd - batchsize for epoch drops second time
   i) utb_dd - unlabeled data batchsize for epoch drops second time 
   ```                           
### Objective

## Improve how to select the best answer among different contexts.

We deal with a QA task with a single question and multiple contexts (i.e., paragraphs). One of the most important issues in this type of task is in which paragraph to pick the answer span. Current naive implementation is comparing the probability in a prediction and choosing the paragraph with the largest.
This NSML&KAIST CS492I_NLP Project aims to improve the given baseline code with manipulations 

### Improve how to select training samples considering a memory limit.

There are multiple contexts, but since there is a memory limit, we cannot include everything in training. The baseline is using first three samples in sequence. Which training samples should we choose to learn the best representation? 

## For Training
 - assuming you are allocated with at least one GPU, execute bash file - (for nsml: ./run_nsml.sh   for local: ./run_local.sh)
We recommend running run_nsml.sh bash file since you are using the dataset already uploaded on nsml server.

## Our pretrained model which produced best score on nsml leader board
 - nsml kaist0013/korquad-open-ldbd3/126 electra_last
