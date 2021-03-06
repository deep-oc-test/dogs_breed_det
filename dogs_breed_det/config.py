# -*- coding: utf-8 -*-
"""
   Module to define CONSTANTS used across the project
"""

from os import path
from webargs import fields
from marshmallow import Schema, INCLUDE

# identify basedir for the package
BASE_DIR = path.dirname(path.normpath(path.dirname(__file__)))
Dog_RemoteStorage = 'rshare:/deep-oc-apps/dogs_breed_det/'
Dog_RemoteShare = 'https://nc.deep-hybrid-datacloud.eu/s/D7DLWcDsRoQmRMN/download?path=%2F&files='
Dog_DataDir = 'dogImages'
Dog_WeightsPattern = 'weights.best.NETWORK.3layers.hdf5'
Dog_LabelsFile = path.join(BASE_DIR, 'data','dog_names.txt')


machine_info = { 'cpu': '',
                 'gpu': '',
                 'memory_total': '',
                 'memory_available': ''
               }

cnn_list = ['Resnet50', 'InceptionV3', 'VGG16', 'VGG19']

# class / place to describe arguments for predict()
class PredictArgsSchema(Schema):
    class Meta:
        unknown = INCLUDE  # supports extra parameters

    network = fields.Str(
        required=False,
        missing=cnn_list[0],
        enum=cnn_list,
        description="Neural model to use for prediction"
    )
    
    files = fields.Field(
        required=False,
        missing=None,
        type="file",
        data_key="data",
        location="form",
        description="Select the image you want to classify."
    )
    
    urls = fields.Url(
        required=False,
        missing=None,
        description="Select an URL of the image you want to classify."
    )


# class / place to describe arguments for train()
class TrainArgsSchema(Schema):
    class Meta:
        unknown = INCLUDE  # supports extra parameters
        
    num_epochs = fields.Integer(
        required=False,
        missing=1,
        description="Number of training epochs")

    network = fields.Str(
        required=False,
        missing=cnn_list[0],
        enum=cnn_list,
        description="Neural model to use")

    sys_info = fields.Boolean(
        required=False,
        missing=False,
        enum=[True, False],
        description="Print information about the system (e.g. cpu, gpu, memory)")
