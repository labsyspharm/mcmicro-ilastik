# Preparation and processing of ome.tif images with Ilastik
mcmicro module for training and processing large images with Ilastik

## CommandIlastikPrepOME.py

Script for preparing ome.tif images to be accessed by Ilastik. Exports hdf5 formats.

**Headless Ilastik execution once the classifier is ready**

```
mkdir prob_maps/ilastik
python CommandIlastikPrepOME.py --input exemplar-001.ome.tif --output prob_maps/ilastik/ --num_channels 12
```

To apply an existing classifier to an hdf5 file created in the previous step:

```
/path/to/ilastik/run_ilastik.sh --headless --project=classifiers/exemplar_001.ilp prob_maps/ilastik/exemplar-001.hdf5
```

**For training follow these steps**
| Parameter | Default / e.g., | Description |
| --- | --- | --- |
| `--input` |`None` | Path to images (Ex: ./my_image.ome.tif ./my_image2.ome.tif)|
| `--output` |`None` | Path to output directory. Either single directory or number of directories=to number of images (Ex: ./my_outdir)|
| `--nonzero_fraction <value>` |`None` | Indicates fraction of pixels per crop above global threshold to ensure tissue and not only background is selected |
| `--nuclei_index <index>` |`1` | Index of nuclei channel to use for nonzero_fraction argument |
| `--crop` | Omitted | If specified, crop regions for ilastik training |
| `--num_channels <value>` | `None`| Number of channels to export per image (Ex: 40 corresponds to a 40 channel ome.tif image) |
| `--channelIDs <indices>` |`None` | Integer indices specifying which channels to export (Ex: 1 2 4) |
| `--ring_mask`| Omitted | Specify if you have a ring mask in the same directory to use for reducing size of hdf5 image |
| `--crop_amount <integer>`| `None`| Number of crops you would like to extract |

For example: `python CommandIlastikPrepOME.py --input /Users/joshuahess/Desktop/VV_40c.ome.tif /Users/joshuahess/Desktop/VV_40c_test.ome.tif --output /Users/joshuahess/Desktop/TestingIlastik --nonzero_fraction 0.5 --nuclei_index 1 --crop --crop_size 400 400 --num_channels 3 --channelIDs 0 1 2 --ring_mask --crop_amount 2`
