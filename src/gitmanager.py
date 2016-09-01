import subprocess
import os
from config import GIT_REPO_DIR_NAME, GIT_REPO_URL


def git_update():
    """
        Update the GIT database repo
    """
    current_dir = os.getcwd().split('/')[-1]
    try:
        if check_repo_exist():
            # Checks if the directory is GIT_REPO_DIR_NAME or not, if not changes to that dir
                # This is to avoid recursive chdir calls
            if current_dir != GIT_REPO_DIR_NAME:
                print("Changing directory")
                os.chdir(GIT_REPO_DIR_NAME)
            subprocess.call(['git', 'pull'])
            # Sleeps for 10 secs, waits till the pull is completed
            # time.sleep(10)
        else:
            print('Some problem with the repo, repo doesnt exist')
    except Exception as e:
        raise e
    finally:
        os.chdir("../")


def get_current_dir():
    tmp = os.getcwd().split('/')
    return tmp[-1]


def git_clone():
    """
        GIT DATA repo doesn't exist, pull the repo
    """
    try:
        os.chdir(GIT_REPO_DIR_NAME)
        subprocess.call(['git', 'clone', GIT_REPO_URL])
    except Exception as e:
        raise e


def check_repo_exist():
    """
        Check if git data repo exist
    """
    try:
        if GIT_REPO_DIR_NAME not in os.listdir():
            subprocess.call(['git', 'clone', GIT_REPO_URL])
        else:
            return False
    except Exception as e:
        raise e