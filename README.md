# README.md

## Files Introduction:
1. `Asset.py`: file contains the 'Asset' class, which keeps track of an individual's finance throughout trading.
2. `get_data.py`: file contains the 'get_data' function, which is used to get the bitcoin ohlcv data in 720 days.
3. `env.yml`: file contains the conda environment information.
4. `EMA_SMA (baseline).ipynb` file contains the **baseline strategy**, and `RSI (genetic algorithm).ipynb` file contains our **proposed strategy**.
5. The generated figures will be written into the `figure` folder.


## Steps for reproduction of the results:
1.  Clone this repository to your computer by `git clone <repository url>`
2.  Switch to the main branch by `git checkout main`
3.  Open the folder in **VS Code** or **jupyter notebook**
4.  If you have installed the `ta` and `cxtt` packages, you can skip the step 5 and 6. Otherwise, please follow the step 5 and 6 to create a new conda environment.
5.  Create a new conda environment and activate it in your local machine by `conda env create -f env.yml` and `conda activate btcbot`
6.  Setting the VS Code to use the conda environment you just created (**Ctrl + Shift + P > Python: Select Interpreter > btcbot**)
7.  Run the code in the `EMA_SMA (baseline).ipynb` and `RSI (genetic algorithm).ipynb` files to reproduce the results. (You can run the code by clicking the `Run Cell` button in the top right corner of each cell, or use `Shift + Enter` to run the code in each cell)

   
## Update some packages during development:
1.  If you want to install some new packages, please remember to **manually add them to the env.yml without any version and os dependencies**. Please **DON'T** export it by `conda env export --no-builds > env.yml` because it will causes some ResolvePackageNotFound Error. For example, if you run the command `pip install ipykernel ` then you can add a line at the bottom of the env.yml like `- ipykernel`.
2.  If you want to deactive the conda environment, please use `conda deactivate`
3.  If you want to delete your local conda environment, please use `conda env remove -n btcbot`

## Git commands:
1.  If you want to push your code, please use `git push origin <branch-name>` after using `git add .` and `git commit -m "<your commit message>"` (You need to set the `origin` url first)
2.  If you want to pull the latest code, please use `git pull origin <branch-name>` (You need to set the `origin` url first)
3.  If you want to create a new branch, please use `git checkout -b <branch-name>` (We use the develop branch as the default development branch, and when we finish a version, we will merge the develop branch to the main branch). Then you can push it to the github by `git push origin <branch-name>`.

