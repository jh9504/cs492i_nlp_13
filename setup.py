# nsml: nsml/ml:cuda10.1-cudnn7-pytorch1.3keras2.3

from distutils.core import setup

setup(
    name='kaist-korquad-test',
    version='1.0',
    install_requires=[
        'boto3', 'regex', 'sacremoses', 'filelock', 'tokenizers',
        'tqdm', 'konlpy', 'sentencepiece==0.1.91', 'dataclasses',
        'transformers==3.5.0', 'onnxruntime==0.3.0', 'gluonnlp==0.6.0',
        'MXNet == 1.4.0'
    ]
)
