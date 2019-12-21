<p align="center">
    <strong>
        MYSQL-AUTORESTORE - LINUX & UNIX
    </strong>
</p>

<p align="center">
    <img alt="MIT" src="https://img.shields.io/badge/license-MIT-green.svg">
    <img alt="multi-convert" src="https://img.shields.io/badge/server-MYSQL-red">
    <img alt="multi-convert" src="https://img.shields.io/badge/python-3.*-blue">
</p>


## Introduction
Recently, I was migrating to a new PC, I needed to also migrate all local mysql databases. I dumped all into separate _**.sql**_ files and migrated the folder containing them all.

It then struck me: I would have to create the database one after the other and import the dumps for each manually. That was going to take a whole lot of time. So, I decided to write a fast tool for myself.

This tool was built to auto restore **SQL** dumps in a directory by creating databases (the names are gotten from the title of the dump file) that do not exist before importing each file.

## Requirements
* MYSQL
* You must have Python3.* installed

## Installation
* Go to your home directory on your terminal:

	`$ cd ~`

* Clone `mysql-autorestore` into your home directory:

	`$ git clone https://github.com/hfally/mysql-autorestore.git`
	
* Edit configuration file to put your correct MYSQL details
	For example: `$ nano mysql-autorestore/config.py`
		
		# MYSQL CREDENTIALS
		
		MYSQL_USERNAME = 'root'
		MYSQL_PASSWORD = ''
		MYSQL_HOST = 'localhost'
		MYSQL_PORT = '3306'
		
	press _ctr+x_ then _y_ to exit and save update if you are using _nano_.
	
	**<small>NB: Any text editor can be used to edit the config file</small>**
	
* Add `$HOME/mysql-autorestore/bin` to your PATH.

#### How to add to your PATH
* Run the command below. There is 70% chances you are using the default bash terminal, but if you happen to be using
another terminal like `zsh` switch `.baschrc` for `.zshrc` in the commands below.

	`$ echo 'export PATH="$PATH:$HOME/mysql-autorestore/bin"' >> .bashrc`

* You will need to source your .bashrc or logout/login (or restart the terminal) for the updates to take effect. 
To source your .bashrc, simply run:

	`$ source ~/.bashrc`

**<small>NB: If you use zsh or any other shell, follow the same route (replace .bashrc with .zshrc in the commands above as stated previously)</small>**

## Basic Usage
* To confirm if `mysql-autorestore` is properly installed, run:

    `$ mysql-autorestore`
    
    If this returns how to use the tool, then you're good to go, else, go through this manual again.

* Go to the folder that houses the dump files from the terminal

    `$ cd /path-to-dump-files/` 
    
    ***REPLACE** `path-to-dump-files` with the correct path to dump files, e.g databases*

* Run the command below to do the cleanup

    `$ mysql-autorestore start`

Sip juice and eat pringles while your databases get created and dumps imported.

You can always get help through `$ mysql-autorestore --help`

## Pending
* [ ] Add option to exclude stated dumps files
* [ ] Auto backup of all databases (dumping to sql files using mysqldump)

## Supported OS
- Linux
- UNIX

## License

Mysql-Autorestore is an open-sourced software licensed under the [MIT license](http://opensource.org/licenses/MIT)

## Contribution
For contribution and personal bug reporting, send a mail to the author <a href='mailto:tofex4eva@yahoo.com'>tofex4eva@yahoo.com</a>
