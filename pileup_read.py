import argparse 

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help = "The imput file")
    parser.add_argument("-o", "--output", help = "The output file")
    args = parser.parse_args()
    return args

def pileupreader(inFile, outFile):
    ofile = open(outFile, 'w+')
    with open(inFile, 'r') as fin:
        for lin in fin: 
            entry = lin.split()
            
            if ((entry[4]).replace(".", "").replace("$", "").replace("*","") != ""):
                print (lin.strip("\n"), file = ofile)
    ofile.close()

if __name__ == "__main__":
    args = argparser()
    pileupreader(args.input, args.output)




