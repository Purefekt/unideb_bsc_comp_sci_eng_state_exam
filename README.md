# Website URL:

https://veer-singh.com/unideb_bsc_comp_sci_eng_state_exam/

## To Contribute Install Project with Conda

Clone the main branch of this repository and cd into the project directory

```
cd unideb_bsc_comp_sci_eng_state_exam
```

Run this command to create a conda virtual environment with the name `unideb_bsc_comp_sci_eng_state_exam` and install all its packages

```
conda env create -f environment.yml
```

Activate this virtual environment

```
conda activate unideb_bsc_comp_sci_eng_state_exam
```

Cd into the `project_files` directory

```
cd project_files
```

Edit the markdown files in the `docs` directory to change the content. Manage pages using the `mkdocs.yml` file.  
Run this command to run the server on local machine

```
mkdocs serve
```

The website will be available on

```
http://127.0.0.1:8000/
```
