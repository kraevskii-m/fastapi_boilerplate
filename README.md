# FastAPI Boilerplate
FastAPI boilerplate with PostgreSQL

## Requirements
* Python >= 3.11.4
* Poetry
* Docker

## How to install
### Install Python 3.11.4

For example using `pyenv` on MacOS

```shell
brew install pyenv
pyenv install 3.11.4
# Optional. Select 3.11.4 as global python version
pyenv global 3.11.4
# Or set local version in project directory
pyenv local 3.11.4
```

### Install Poetry
```shell
curl -sSL https://install.python-poetry.org | python3 -

# for zsh
poetry completions zsh > ~/.zfunc/_poetry 
# and add to .zshrc
fpath+=~/.zfunc
autoload -Uz compinit && compinit

# for bash
poetry completions bash >> ~/.bash_completion

# for Oh My Zsh
mkdir $ZSH_CUSTOM/plugins/poetry
poetry completions zsh > $ZSH_CUSTOM/plugins/poetry/_poetry
# You must then add poetry to your plugins array in ~/.zshrc:
plugins(
  poetry
  ...
)
```
### Install dependencies
```shell
poetry init
```
### Configure the pre-commit hooks
```shell
pre-commit install
```
### Install the migrate tool
```shell
brew install golang-migrate
```
### Migrations
```shell
make new_migration
make migrate
```
