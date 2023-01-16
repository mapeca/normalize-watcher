from time import sleep
import os
import signal

import files
import normalize


def handler_stop_signals(signum, frame):
    print("Stopping...")
    quit(0)


signal.signal(signal.SIGINT, handler_stop_signals)
signal.signal(signal.SIGTERM, handler_stop_signals)


def checkMovies(watchDir, normalizedDir, keepStructure):
    watchedFiles = files.checkWatchdir(watchDir)
    normalize.normalizeDir(watchDir, watchedFiles,
                           normalizedDir, keepStructure)
    files.removeEmptyDirs(watchDir)


def checkShows(watchDir, normalizedDir, keepStructure):
    watchedFiles = files.checkWatchdir(watchDir)
    normalize.normalizeDir(watchDir, watchedFiles,
                           normalizedDir, keepStructure)
    files.removeEmptyDirs(watchDir)


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
        print("NORMALIZED_KEEP_MOVIES_STRUCTURE env variable was not configured. Default value is: 'True'")
        keepMoviesStructure = False
    elif str(keepMoviesStructure) != "":
        if str(keepMoviesStructure).upper() == "TRUE":
            keepMoviesStructure = True
        else:
            keepMoviesStructure = False

    ShowsDir = os.getenv("NORMALIZE_SHOWS")
    if ShowsDir == None:
        print("NORMALIZE_SHOWS env variable was not configured. Default value is: '/media/shows'")
        ShowsDir = "/media/Shows"

    normalizedShowsDir = os.getenv("NORMALIZED_SHOWS")
    if normalizedShowsDir == None:
        print("NORMALIZED_SHOWS env variable was not configured. Default value is: '/media/normalized_shows'")
        normalizedShowsDir = "/media/normalized_SHOWS"

    keepShowsStructure = os.getenv("NORMALIZED_KEEP_SHOWS_STRUCTURE")
    if keepShowsStructure == None:
        print("NORMALIZED_KEEP_SHOWS_STRUCTURE env variable was not configured. Default value is: 'False'")
        keepShowsStructure = True
    elif str(keepShowsStructure) != "":
        if str(keepShowsStructure).upper() == "TRUE":
            keepShowsStructure = True
        else:
            keepShowsStructure = False

    watchInterval = os.getenv("NORMALIZE_INTERVAL")
    if watchInterval == None:
        print("NORMALIZE_INTERVAL env variable was not configured. Default value is: 30")
        watchInterval = 30
    print("Starting v0.1")
    while True:
        checkMovies(moviesDir, normalizedMoviesDir, keepMoviesStructure)
        checkShows(ShowsDir, normalizedShowsDir, keepShowsStructure)
        sleep(watchInterval)
