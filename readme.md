# normalize-watcher
Simple python script to watch a directory containing new/existing video files and normalize audio tracks, save the output in a output directory and remove the watched directory files already normalized.

If you want to use this, keep in mind it is WIP. Only works for movies or shows not both.

# Uses?
Main purpose for this script was to use it in a workflow where Radarr is not used to manage media, rather to manage download client instead.
Example 1: Jackett <-> Radarr -> Deluge -> Radarr -> Tdarr -> normalize-watcher -> Plex
Example 2: Input -> normalize-watcher -> normalized

# Usage
## Clone repo
You can clone this repo and run the main.py with python, but you'll need to install [ffmpeg-normalize](https://github.com/slhck/ffmpeg-normalize)
Once you have installed ffmpeg-normalize, you need to setup basic ENV values.

## Docker compose
You can use shipped [docker-compose](docker-compose.yaml) which builds using [Dockerfile](Dockerfile), or you can build the image and push to your private registry.

## Env
### NORMALIZE_MOVIES
Movies folder which we want to normalize.
Ex: /media/movies
### NORMALIZED_MOVIES
Movies folder where normalized files are put into.
Ex: /media/normalized_movies
### NORMALIZED_KEEP_MOVIES_STRUCTURE
Keep folder structure or save only files.
Ex: True (default False)
### NORMALIZE_INTERVAL
Time (in seconds) between checks of the watchfolders.
Ex: 30
