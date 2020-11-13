from torch import nn
from blocks.decoding_block import DecodingBlock
from args import ARGS

class Decoder(nn.Module):

    def __init__(self):
        super().__init__()
        self.d_block_1 = DecodingBlock(ARGS['encoder'][2], ARGS['encoder'][3], ARGS['decoder'][0])
        self.d_block_2 = DecodingBlock(ARGS['encoder'][1], ARGS['decoder'][0], ARGS['decoder'][1])
        self.d_block_3 = DecodingBlock(ARGS['encoder'][0], ARGS['decoder'][1], ARGS['decoder'][2])

    def forward(self, x_1, x_2, x_3, x_4):
        output_1 = self.d_block_1(x_3, x_4)
        output_2 = self.d_block_2(x_2, output_1)
        output_3 = self.d_block_3(x_1, output_2)

        return output_1, output_2, output_3