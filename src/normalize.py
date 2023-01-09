import os
import subprocess


def normalizeDir(workingDir, files, outputBaseDir, keepStructure=False):
    for f, dir in files.items():
        print("Processing file: {}".format(f))
        outStructureDir = ""
        if keepStructure:
            outStructureDir = dir
            print(outStructureDir)

        sourceDir = os.path.join(workingDir, dir)
        file = os.path.join(sourceDir, f)
        outputDir = os.path.join(outputBaseDir, outStructureDir)
        outputFile = os.path.join(outputDir, f)
        if not os.path.exists(outputDir):
            print("Output folder does not exists. Creating: ", outputDir)
            os.makedirs(os.path.join(outputBaseDir, outputDir))

        normalizeFile(file, outputFile)

        if os.path.exists(outputFile):
            removeOriginalFile(sourceDir, file)


def normalizeFile(file, output):
    command = ["ffmpeg-normalize", file, "-o", output, "-f", "-c:a", "aac"]
    print(" ".join(command))
    subprocess.run(command)


def removeOriginalFile(dir, file):
    print("Removing file from watchdir: {}".format(file))
    os.remove(file)
