#Functions for parsing command line arguments for ome ilastik prep
import argparse


def ParseInputOME():
   """Function for parsing command line arguments for input to ilastik prep functions"""

#if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument('--input',nargs='*', help="enter path to images with spaces between each image (Ex: /path1/image1.ome.tiff /path2/image2.ome.tiff)")
   parser.add_argument('--output',nargs='*')
   parser.add_argument('--crop', action='store_true',default = False)
   parser.add_argument('--no-crop', dest='crop', action='store_false')
   parser.add_argument('--crop_size',type=int,nargs='*')
   parser.add_argument('--nonzero_fraction',type=float)
   parser.add_argument('--nuclei_index',type=int)
   parser.add_argument('--num_channels',type=int)
   parser.add_argument('--ring_mask', action='store_true',default = False)
   parser.add_argument('--no-ring_mask', dest='ring_mask', action='store_false')
   args = parser.parse_args()
   #Create a dictionary object to pass to the next function
   dict = {'input': args.input, 'output': args.output, 'crop': args.crop,\
      'crop_size':args.crop_size,'nonzero_fraction':args.nonzero_fraction,\
         'nuclei_index':args.nuclei_index, 'num_channels':args.num_channels,\
         'ring_mask':args.ring_mask}
   #Print the dictionary object
   print(dict)
   #Return the dictionary
   return dict
