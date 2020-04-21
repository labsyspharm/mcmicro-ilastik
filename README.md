# Preparation and processing of ome.tif images with Ilastik
MCMICRO module for training and processing large images with Ilastik

## Headless Ilastik execution once the classifier is ready
Example:
./IlastikHeadless.sh /n/groups/lsp/ilastik/ilastik-1.3.3post2-Linux/ /home/ds230/files_ilastik_test/exemplar_001.ilp /home/ds230/files_ilastik_test/exemplar-001.hdf5



## CommandIlastikPrepOME.py
Script for preparing ome.tif images to be accessed by Ilastik. Exports hdf5 formats.

Command line execution example:
python CommandIlastikPrepOME.py --input /Users/joshuahess/Desktop/VV_40c.ome.tif /Users/joshuahess/Desktop/VV_40c_test.ome.tif --output /Users/joshuahess/Desktop/TestingIlastik --nonzero_fraction 0.5 --nuclei_index 1 --crop --crop_size 400 400 --num_channels 3 --ring_mask

* input: Path to images (Ex: ./my_image.ome.tif ./my_image2.ome.tif)

* output: Path to output directory. Either single directory or number of directories=to number of images (Ex: ./my_outdir)

* nonzero_fraction: Indicates fraction of pixels per crop above global threshold to ensure

* nuclei_index: Index of nuclei channel to use for nonzero_fraction argument

* crop: include if you choose to crop regions for ilastik training, if not, do not include this argument

* num_channels: Number of channels to export per image (Ex: 40 corresponds to a 40 channel ome.tif image)

* ring_mask: include if you have a ring mask in the same directory to use for reducing size of hdf5 image. do not include if not
