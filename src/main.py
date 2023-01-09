from time import sleep
import os

import files
import normalize


def checkMovies(watchDir, normalizedDir, keepStructure):
    watchedFiles = files.checkWatchdir(watchDir)
    normalize.normalizeDir(watchDir, watchedFiles,
                           normalizedDir, keepStructure)
    files.removeEmptyDirs(watchDir)


def checkShows():
    # print("")
    return


if __name__ == "__main__":

    moviesDir = os.getenv("NORMALIZE_MOVIES")
    if moviesDir == None:
        print("NORMALIZE_MOVIES env variable was not configured. Default value is: '/media/movies'")
        moviesDir = "/media/movies"

    normalizedMoviesDir = os.getenv("NORMALIZED_MOVIES")
    if normalizedMoviesDir == None:
        print("NORMALIZED_MOVIES env variable was not configured. Default value is: '/media/normalized_movies'")
        normalizedMoviesDir = "/media/normalized_movies"

    keepMoviesStructure = os.getenv("NORMALIZED_KEEP_MOVIES_STRUCTURE")
    if keepMoviesStructure == None:
        print("NORMALIZED_KEEP_MOVIES_STRUCTURE env variable was not configured. Default value is: 'False'")
        keepMoviesStructure = False
    elif str(keepMoviesStructure) != "":
        if str(keepMoviesStructure).upper() == "TRUE":
            keepMoviesStructure = True
        else:
            keepMoviesStructure = False

    watchInterval = os.getenv("NORMALIZE_INTERVAL")
    if watchInterval == None:
        print("NORMALIZE_INTERVAL env variable was not configured. Default value is: 30")
        watchInterval = 30
    print("Starting v0.1")
    while True:
        checkMovies(moviesDir, normalizedMoviesDir, keepMoviesStructure)
        checkShows()
        sleep(watchInterval)
