#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="${HOME}/torky_independent_workspace"
echo "================================================================="
echo "   PROVISIONING MISSING SCIENTIFIC FIELD REPOSITORIES ON GITHUB  "
echo "================================================================="

# Verify if GitHub CLI is installed and authenticated
if ! command -v gh &> /dev/null; then
    echo "❌ Error: GitHub CLI ('gh') is not installed."
    echo "Please install it via: sudo apt install gh"
    exit 1
fi

if ! gh auth status &> /dev/null; then
    echo "❌ Error: GitHub CLI is not authenticated."
    echo "Please run: gh auth login"
    exit 1
fi

# List of scientific repositories that threw 'Not Found' errors
FIELD_REPOS=(
  "torky-field1-medical"
  "torky-field2-energy"
  "torky-field3-electrons"
  "torky-field4-photonics"
  "torky-field5-cosmology"
  "torky-fields6-9-advanced"
)

# Fetch authenticated GitHub username
USER_NAME=$(gh api user --jq '.login')
echo "Authenticated User: ${USER_NAME}"

for repo in "${FIELD_REPOS[@]}"; do
    TARGET_DIR="${WORKSPACE}/${repo}"
    if [ -d "${TARGET_DIR}" ]; then
        echo "--> Checking remote presence for: ${repo}"
        
        # Check if the repository already exists on GitHub
        if ! gh repo view "${USER_NAME}/${repo}" &> /dev/null; then
            echo "    [MISSING] Creating upstream repository: ${USER_NAME}/${repo}"
            # Creates a public repository (change --public to --private if security bounds require it)
            gh repo create "${USER_NAME}/${repo}" --public --description "Torky Protocol Independent Portal - ${repo}"
            
            # Reset and apply the correct remote URL configuration locally
            cd "${TARGET_DIR}"
            git remote remove origin &> /dev/null || true
            git remote add origin "git@github.com:${USER_NAME}/${repo}.git"
            echo "    ✓ Local remote origin aligned to git@github.com:${USER_NAME}/${repo}.git"
        else
            echo "    ✓ Upstream repository verified on GitHub."
        fi
    fi
done

echo "================================================================="
echo "   [COMPLETE] ALL UPSTREAM MATRIX CHANNELS ARMED AND ROUTED      "
echo "================================================================="
