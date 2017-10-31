# Machine Learning - Style transfer

## torch2coreml
* This folder contains the modified code from prisma torch2coreml. 
* This version works for pytorch instead of torch and supports instance normalization while the prisma version, currently does not.
* Original prisma version link: https://github.com/prisma-ai/torch2coreml

* Example command to convert a pytorch model to a coreml model with 1024 resolution:
python pytorch2coreml/convert-fast-neural-style.py -input pytorchModels/takes.model -output pytorchModels/takes.mlmodel -size 1024

* You can use these models in the IOS_TestProject.

## pytorchModels
* Contains the current pytorch trained models and coreml models used in storyo for themes book and takes.

* To train more trained models use the implementation as shown in the following link: 
https://github.com/pytorch/examples/tree/master/fast_neural_style

## compiled
* Contains the compiled coreml models to use directly in storyo or any other xamarin IOS project that doesn't want to compile the models in execute time.

* Example command to compile models:
"path to your applications folder"  /Applications/Xcode.app/Contents/Developer/usr/bin/coremlc compile pytorchModels/book.mlmodel compiled/

## Requirements
* coremltools (0.6.3)
* Xcode 9
* python 2.7
* PyTorch
* torch
* luarocks