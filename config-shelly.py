# ______               ___ __               _______ __           __ __ 
#|      |.-----.-----.'  _|__|.-----.______|     __|  |--.-----.|  |  |
#|   ---||  _  |     |   _|  ||  _  |______|__     |     |  -__||  |  |
#|______||_____|__|__|__| |__||___  |      |_______|__|__|_____||__|__|
#                             |_____|                                  
#
# <config-shell.py>
# Description:
#   A Python script to automate the process of changing the default shell to Fish on Linux systems.
#   The script detects the current shell, checks the installed Python version, and adjusts the
#   installation commands accordingly.
# Author:
#    Angel (CypherOxide) Santiago
#    as@angelsantiago.me 
#    https://github.com/cypheroxide
# Copyright: Angel (CypherOxide) Santiago, 2023
#
# License:
#    This project is licensed under the MIT License - see the LICENSE.md file for details.
#
# GitHub Repository:
#    https://github.com/cypheroxide/config-shell
#
# Disclaimer:
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.
#
#

import subprocess
import platform
from distro import linux_distribution

# Get the current user's default shell
def get_current_shell():
  return subprocess.check_output(["echo", "$SHELL"]).decode().strip()

# Get the installed Python version
def get_python_version():
  try:
    output = subprocess.check_output(["python3", "--version"], stderr=subprocess.STDOUT).decode() 
    # Parse out just the major.minor version
    return output.split(" ")[1]  
  except subprocess.CalledProcessError:
    return None

# Get the Linux distribution name
def get_linux_distribution():
  try:
    return linux_distribution(full_distribution_name=False)[0].lower()
  except:
    return None

# Install Fish shell based on the distribution
def install_fish(distro):
  package_manager = None
  if distro == "arch":
    package_manager = "pacman"
  elif distro in ["debian", "ubuntu"]:
    package_manager = "apt"
  elif distro in ["fedora", "centos", "rhel"]:
    package_manager = "dnf"

  if package_manager:
    # Update packages and install fish
    subprocess.run([f"sudo {package_manager} update"], shell=True, check=True) 
    subprocess.run([f"sudo {package_manager} install fish"], shell=True, check=True)
  else:
    print(f"Unable to install fish on {distro}")

# Change the default shell to Fish  
def change_default_shell():
  subprocess.run(["chsh", "-s", "/usr/bin/fish"])

def main():
  
  # Get information about current environment
  current_shell = get_current_shell()
  print(f"Current shell: {current_shell}")

  python_version = get_python_version()

  distro = get_linux_distribution()

  # Check if Fish is already the default shell
  if "/fish" in current_shell:
    print("Fish shell already set as default")
  else:
    # Check Python version
    if python_version:
      print(f"Python {python_version} detected") 
    else:
      print("Unsupported Python version")
      return
    
    # Install and configure Fish
    if distro:
      print(f"{distro} distro detected")
      print("Installing fish...")
      install_fish(distro)
      print("Changing default shell...")
      change_default_shell()
      print("Fish installed and set as default shell! Restart your terminal.")
    else:
      print("Could not determine Linux distribution.")
  

if __name__ == "__main__":
  main()