import torch
import torch.nn.functional as F


def resize_tensor():
    image = torch.rand((1, 1, 4, 4)) #batch_size, depth, height, width
    print ('image', image)

    # by defining scale
    image_double_size = F.interpolate(image, scale_factor=2, mode='bilinear')
    print ('image_double_size', image_double_size)

    #by defining output size
    image_double_size = F.interpolate(image, size=(8, 8), mode='bilinear')
    print('image_double_size', image_double_size)


if __name__=='__main__':
    resize_tensor()