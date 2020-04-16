#!/bin/bash

#ilastik headless will not run if any of the folder paths contain spaces!

#Enter the path to where ilastik application is stored (Most of the time it will be in the applications folder)

ilastik_location=$1

#Input the location of your ilastik pixel classification project

ilastik_project_location=$2

#Input the location of the folders that contain the images to be batch processed

hdf5_locations=$3

#Append each hdf5 location folder in order to extract all elements that end with .hdf5

#hdf5_input=("${hdf5_locations[@]/%//*crop0.hdf5}")

#The following line of code will load headless ilastik and batch process each image that ends with crop0.hdf5 in the hdf5 location folders list

${ilastik_location}/run_ilastik --headless --project=${ilastik_project_location} ${hdf5_locations}