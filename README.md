# cs492i_nlp_team13
KAIST & NAVER Deep Learning Lecture

\# korquad-open-cs492I
KorQuad-Open Baseline Code for KAIST CS492I 2020 Fall

## Original Author
Seonhoon Kim (Naver)

## Edited by
KAIST cs492i_nlp_team13

Hyeonuk Nam, Jinhyuk Ryu

## Train in NSML
```bash
sh run_nsml.sh
```

## Train in Local
```bash
sh run_local.sh
```

### Objective

## Improve how to select the best answer among different contexts.

We deal with a QA task with a single question and multiple contexts (i.e., paragraphs). One of the most important issues in this type of task is in which paragraph to pick the answer span. Current naive implementation is comparing the probability in a prediction and choosing the paragraph with the largest.
This NSML&KAIST CS492I_NLP Project aims to improve the given baseline code with manipulations 

### Improve how to select training samples considering a memory limit.

There are multiple contexts, but since there is a memory limit, we cannot include everything in training. The baseline is using first three samples in sequence. Which training samples should we choose to learn the best representation? 

### Our best model

## Path to our pre-trained model in NSML
'''kaist0013/korquad-open-ldbd3/126 electra_last'''
