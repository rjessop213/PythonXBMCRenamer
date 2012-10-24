import os
import argparse


def RenameFile(filename, options):
    print(filename)

def ParseTarget(options):
    if os.path.isdir(options.target):
        for root, dirs, filenames in os.walk(options.target):
            for filename in filenames:
                RenameFile(os.path.join(root, filename), options)
    elif os.path.isfile(options.target):
        RenameFile(options.target, options)
    else:
        raise Exception("Invalid target spedified: %s"%options.target)


if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Renames video file(s) to better match what XBMC TV program scrapers expect")
    parser.add_argument("target", help="The file to rename, or a directory to search for video files (using the recursive option)")
    parser.add_argument("-v", "--verbose", help="Prints extra information", action="store_true")
    parser.add_argument("-e", "--episodenames", action="store_true", help="Add episode names from thetvdb.com - requires a thetvdb.com API key; see README")
    seriesIDGroup=parser.add_mutually_exclusive_group(required=True)
    seriesIDGroup.add_argument("-si", "--seriesid", help="Get the series name and episode names via thetvdb.com series ID - Requires a thetvdb.com API key; see README")
    seriesIDGroup.add_argument("-sn", "--seriesname", help="The name of the series")
    ParseTarget(parser.parse_args())
