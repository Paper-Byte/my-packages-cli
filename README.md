# My Packages

My Packages is a Python-based CLI that allows you to store packages in a local relational database. The database is ran using SQLite3, making it quick and easy to spin up locally. All CRUD operations are performed through the CLI. You can also directly install packages that have been saved to the local DB to any project you wish.

## Installation

Fork and clone this repo.

Once cloned, ensure you install all dependancies using

```bash
pipenv install
```

## Usage

```python
python lib/cli.py
```

While in the project directory will launch the CLI

From there follow CLI options with user input to navigate and execute commands

## Visuals

_Main Menu_
![Main Menu](https://i.ibb.co/HGSD8Tr/Screenshot-2023-10-08-at-2-17-25-PM.png)

_Language Menu_
![Language Menu](https://i.ibb.co/VpCJ2HX/Screenshot-2023-10-08-at-1-32-43-PM.png)

_Package Menu_
![Package Menu](https://i.ibb.co/Xbkn46W/Screenshot-2023-10-08-at-1-33-03-PM.png)

_Dev Menu_
![Dev Menu](https://i.ibb.co/vsgC5mL/Screenshot-2023-10-08-at-1-33-27-PM.png)

## Roadmap

Support for other package mangers to come

```
bun
yarn
pip
```

Support for custom templates that can be shard to come

_ex: barebones react with just redux and react-icons_

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
