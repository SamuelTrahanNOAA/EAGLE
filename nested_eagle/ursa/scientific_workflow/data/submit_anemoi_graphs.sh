#!/bin/bash
#SBATCH -J nested_eagle_graphit
#SBATCH -o slurm/graphit_processing.%j.out
#SBATCH -e slurm/graphit_processing.%j.err
#SBATCH --account=gsd-fv3-dev
#SBATCH --partition=u1-service
#SBATCH --mem=128g
#SBATCH -t 30:00
#SBATCH --nodes=1
#SBATCH --ntasks=1

# shellcheck disable=SC1091
source /scratch4/NAGAPE/epic/role-epic/miniconda/bin/activate
conda activate eagle
module load gcc

set -xue

export LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$LD_LIBRARY_PATH

rm -rf output-folder
rm -f graph.pt
anemoi-graphs create graph.yaml graph.pt
test -s graph.pt
anemoi-graphs inspect graph.pt output-folder/
