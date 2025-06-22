#!/bin/bash

############################################################################
#
# Install editable phidata in a virtual environment
# Usage:
#   ./scripts/dev_setup.sh
#
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "${CURR_DIR}")"
VENV_DIR="${REPO_ROOT}/phienv"
PYTHON_VERSION=$(python3 --version)
source "${CURR_DIR}/_utils.sh"

main() {
  print_heading "Phidata dev setup"
  print_heading "Creating venv: ${VENV_DIR}"

  print_info "Python version: ${PYTHON_VERSION}"
  print_info "Removing existing venv: ${VENV_DIR}"
  rm -rf "${VENV_DIR}"

  print_info "Creating python3 venv: ${VENV_DIR}"
  python3 -m venv "${VENV_DIR}"

  # Activate the venv
  source "${VENV_DIR}/bin/activate"

  print_info "Installing base python packages"
  pip3 install --upgrade pip pip-tools twine build

  # Install workspace
  source "${CURR_DIR}/install.sh"

  print_heading "Activate using: source ${VENV_DIR}/bin/activate"
}

main "$@"
