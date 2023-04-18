from git import Repo
import shutil
import os

reset = False
repo = 'clone'

if reset == True:
    shutil.rmtree(repo)

isExist = os.path.exists('clone')

if not isExist:
   os.makedirs(repo)
   git_url = 'https://github.com/tategallery/collection.git/'
   repo_dir = os.getcwd() + '/clone'
   Repo.clone_from(git_url, repo_dir)