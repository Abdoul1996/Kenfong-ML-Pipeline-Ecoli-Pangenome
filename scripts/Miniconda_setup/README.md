# 🚀 Miniconda Setup Script

## 📌 Overview
This script automates the installation of **Miniconda** and sets up essential bioinformatics tools in dedicated Conda environments.

### 🛠️ Tools Installed:
- **BBMap (bbduk.sh)**: A fast, accurate adapter and quality trimming tool for DNA sequencing reads.
- **Unicycler**: An assembly pipeline for bacterial genomes.
- **SRA-Tools**: A toolkit for retrieving and processing sequencing data from NCBI's Sequence Read Archive.
- **Prokka**: A rapid prokaryotic genome annotation tool.
- **Roary**: A tool for large-scale bacterial pangenome analysis.

---

## 📥 Installation & Setup
### 🔽 1. Download & Run the Script
```bash
wget https://github.com/Abdoul1996/Kenfong-ML-Pipeline-Ecoli-Pangenome/raw/main/scripts/Miniconda_setup/install_conda.sh -O install_miniconda_envs.sh
chmod +x install_miniconda_envs.sh
./install_miniconda_envs.sh
```

### 🚀 2. Activate Conda Environments
Once the installation is complete, activate the required environment before using a tool:
```bash
conda activate ecoli-env    # For BBMap, Unicycler, SRA-Tools
conda activate prokka-env   # For Prokka
conda activate roary-env    # For Roary
```

### 📜 3. Verify Installed Environments
To check if all environments were created successfully, run:
```bash
conda env list
```
You should see:
```
# conda environments:
#
base                  *  /home/user/miniconda
ecoli-env               /home/user/miniconda/envs/ecoli-env
prokka-env              /home/user/miniconda/envs/prokka-env
roary-env               /home/user/miniconda/envs/roary-env
```

---

## 🎯 Expected Output for Each Tool
### 🧪 **BBMap (bbduk.sh)**
```bash
bbduk.sh --help
```
**Expected Output:**
```
BBMap package version 39.01
Written by Brian Bushnell
```

### 🧬 **Unicycler**
```bash
unicycler --help
```
**Expected Output:**
```
Unicycler: An assembly pipeline for bacterial genomes
Version: 0.5.0
```

### 📥 **SRA-Tools**
```bash
fastq-dump --help
```
**Expected Output:**
```
Usage: fastq-dump [options] <accession>
```

### 🏷️ **Prokka**
```bash
prokka --help
```
**Expected Output:**
```
Prokka v1.14.6 - rapid prokaryotic genome annotation
```

### 🧬 **Roary**
```bash
roary -h
```
**Expected Output:**
```
Roary: the pangenome pipeline
Version: 3.8.0
```

---

