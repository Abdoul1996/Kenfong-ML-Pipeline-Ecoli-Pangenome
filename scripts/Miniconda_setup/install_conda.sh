#!/bin/bash
## Name: 👨‍🎓 Estefanos Kebebew

green='\e[32m'
blue='\e[34m'
yellow='\e[33m'
red='\e[31m'
nc='\e[0m' # No color

# ASCII Art Banner
echo -e "${blue}========================================="
echo -e "${yellow}🚀 Automated Miniconda & Bioinformatics Setup 🚀"
echo -e "${blue}=========================================${nc}\n"

# Download and install Miniconda
echo -e "${green}🔽 Downloading Miniconda...${nc}"
curl -o miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
echo -e "${green}✅ Miniconda Installed!${nc}\n"

# Initialize conda
source $HOME/miniconda/bin/activate
conda init

echo -e "${blue}🔄 Refreshing shell...${nc}"
source ~/.bashrc

# Function to create and configure conda environments
echo -e "${yellow}✨ Setting up Conda environments...${nc}\n"
create_env() {
    env_name=$1
    shift
    echo -e "${green}🌱 Creating environment: ${env_name}...${nc}"
    conda create -n "$env_name" -y
    conda activate "$env_name"
    echo -e "${green}📦 Configuring channels and installing packages for ${env_name}...${nc}"
    conda config --add channels defaults
    conda config --add channels bioconda
    conda config --add channels conda-forge
    for package in "$@"; do
        echo -e "${yellow}🔧 Installing: $package${nc}"
        conda install -c bioconda "$package" -y
    done
    echo -e "${green}✅ Environment ${env_name} setup completed!${nc}\n"
}

# Create and set up environments
create_env "ecoli-env" "bbmap=39.01" "unicycler=0.5.0" "sra-tools"
create_env "prokka-env" "prokka=1.14.6"
create_env "roary-env" "roary=3.8.0"

# Display installed environments
echo -e "${blue}📜 Installed Conda Environments:${nc}"
conda env list

echo -e "${green}🎉 All environments are ready! 🚀${nc}"
