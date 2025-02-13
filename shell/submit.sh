mkdir src/pyclassify/
mkdir scripts
mkdir test
mkdir shell
mkdir experiments
touch src/pyclassify/__init__.py
touch src/pyclassify/utils.py
touch scripts/run.py
touch shell/submit.sbatch
touch shell/submit.sh
touch experiments/config.yaml
touch test/test_.py
python -m pip freeze > requirements.txt
wget https://github.com/MatteB03/Files-for-wget/blob/main/.gitignore
wget https://github.com/MatteB03/Files-for-wget/blob/main/pyproject.toml
sed 's/@NAME/user.name/g' pyproject.toml
sed 's/@MAIL/user.email/g' pyproject.toml