# -*- coding: utf-8 -*-
from os import path

# identify basedir for the package
basedir = path.dirname(path.normpath(path.dirname(__file__)))
dogS3Storage = 'https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/'
dogDatasetUrl = dogS3Storage + 'dogImages.zip'
dogDataDir = 'dogImages'
dogNamesFile = path.join(basedir,'data','dog_names.txt')
dogBreeds = 133


