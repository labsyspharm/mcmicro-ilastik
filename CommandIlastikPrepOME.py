#Script for parsing command line arguments and running ilastik prep functions
#Joshua Hess
import ParseInput
import IlastikPrepOME

#Parse the command line arguments
args = ParseInput.ParseInputOME()

#Run the MultiIlastikOMEPrep function
IlastikPrepOME.MultiIlastikOMEPrep(**args)
