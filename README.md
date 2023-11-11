# Fish Shell Installer

This script automates the installation and configuration of the Fish shell on Linux.

## Usage

To use the script:

1. Ensure Python 3.7 or higher is installed
2. Clone this repository
3. Run `python install_fish.py` 

The script will:

- Check if Fish is already installed and set as default shell
- Detect the Linux distribution
- Install the Fish package using the appropriate package manager
- Set Fish as the default shell for the current user
  
The user will need to log out and back in or start a new terminal session for the default shell change to take effect.

## Features

- Detects the current default shell
- Gets the Python version  
- Determines the Linux distribution
- Installs Fish based on the distribution
- Changes default shell to Fish
- Provides user-friendly output and instructions

## Supported Linux Distributions

- Arch
- Debian/Ubuntu
- Fedora/CentOS/RHEL

Contributions are welcome to expand support to other distros!

## Dependencies

- Python 3.7 or higher
- `subprocess` module
- `platform` module  
- `distro` module

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspiration and code snippets from [How to Programmatically Set the Default Terminal in Different Linux Distributions](https://www.digitalocean.com/community/tutorials/how-to-programmatically-set-the-default-terminal-in-different-linux-distributions)
- Fish shell [documentation](https://fishshell.com/docs/current/index.html)
