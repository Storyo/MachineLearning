import argparse

import torch
from torch.legacy.nn import Module, SpatialFullConvolution
from torch.autograd import Variable
from torch.nn import InstanceNorm3d
from torch.utils.serialization import load_lua
from torch.utils.serialization.read_lua_file import TorchObject
from transformer_net import TransformerNet

from _torch_converter import convert

def main():
    parser = argparse.ArgumentParser(
        description='Convert fast-neural-style model to CoreML'
    )

    parser.add_argument('-input', required=True, help='Path to Torch7 model')
    parser.add_argument('-output', required=True, help='CoreML output path')
    parser.add_argument(
        '-size',
        default=1000, type=int, help='Image width/height'
    )

    args = parser.parse_args()

    input_shape = (3, args.size, args.size)

    model = TransformerNet()
    model.load_state_dict(torch.load(args.input))
    model.eval()

    print(model)
    coreml_model = convert(
        model,
        [input_shape],
        input_names=['inputImage'],
        output_names=['outputImage'],
        image_input_names=['inputImage'],
        preprocessing_args={
            'is_bgr': True,

        },
        image_output_names=['outputImage'],
        deprocessing_args={
            'is_bgr': True,

        },
    )

    coreml_model.author = 'Storyo'
    coreml_model.license = 'Free for research use'
    coreml_model.short_description = 'Feedforward style transfer'
    coreml_model.input_description['inputImage'] = 'Image to stylize'
    coreml_model.output_description['outputImage'] = 'Stylized image'

    coreml_model.save(args.output)
    print('saved')

if __name__ == "__main__":
    main()
