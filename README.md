1. Inside a git repository
    - Initialize DVC: 
        * `div init`
    - Tracking files to DVC: 
        * `div add [file] to track`
    - Create local remote on hard drive (in this case storing on local computer, but can be added anywhere like Azure, AWS, etc..): 
        * `dvc remote add -d [name-remote] [location like /temp/dvc-storage]`
    - Push the data to remote: 
        * `dvc push`
    - To recover the data
        * `dvc pull`