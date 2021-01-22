import os


def r_listdir(rootdir):
    for root, subFolders, files in os.walk(rootdir):
        for folder in subFolders:
            outfileName = rootdir + "/" + folder + "/py-outfile.txt" # hardcoded path
            folderOut = open( outfileName, 'w' )
            print("outfileName is " + outfileName)

            for file in files:
                filePath = rootdir + '/' + file
                f = open( filePath, 'r' )
                toWrite = f.read()
                print("Writing '" + toWrite + "' to" + filePath)
                folderOut.write( toWrite )
                f.close()

            folderOut.close()

r_listdir("images")