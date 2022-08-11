import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', nargs='*', help="Images for CommandIlastikPrepOME.py")
    parser.add_argument('--model', help="Custom model for run_ilastik.sh",
                        default="/app/classifiers/exemplar_001_nuclei.ilp")

    args, pargs = parser.parse_known_args()

    # Construct a CommandIlastikPrepOME.py call
    cmd1 = "python /app/CommandIlastikPrepOME.py --input " + \
        " ".join(args.input) + " " + " ".join(pargs)
    print(cmd1)
    os.system(cmd1)

    # Construct a run_ilastik.sh call
    cmd2 = "/ilastik-release/run_ilastik.sh --headless --export_dtype uint8 --project " + \
        str(args.model) + " *.hdf5"
    print(cmd2)
    os.system(cmd2)
