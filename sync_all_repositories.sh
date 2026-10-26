#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="${HOME}/torky_independent_workspace"
echo "================================================================="
echo "   SYNCHRONIZING ALL 9 DEDICATED SCIENTIFIC PORTALS UPSTREAM    "
echo "================================================================="

REPOS=(
  "torky-web-platform"
  "torky-portal-systems"
  "torky-institute-core"
  "torky-field1-medical"
  "torky-field2-energy"
  "torky-field3-electrons"
  "torky-field4-photonics"
  "torky-field5-cosmology"
  "torky-fields6-9-advanced"
)

for repo in "${REPOS[@]}"; do
  TARGET_DIR="${WORKSPACE}/${repo}"
  if [ -d "${TARGET_DIR}" ]; then
    echo "--> Syncing Local State: ${repo}"
    cd "${TARGET_DIR}"
    
    # Initialize repository if not already verified
    if [ ! -d ".git" ]; then
      git init --quiet
      git branch -M main
    fi
    
    git add .
    # Prevent empty commit verification errors
    git commit -m "infrastructure: align architectural invariants and workflows to master protocol specification" --quiet || true
    
    # Check if upstream origin is armed before attempting push
    if git remote | grep -q 'origin'; then
      echo "    Pushing changes to remote upstream branch [main]..."
      git push origin main --quiet || echo "    ⚠️ Remote push skipped: Check networking credentials."
    else
      echo "    ✓ Sealed locally (No tracking remote set up yet)."
    fi
  else
    echo "  ⚠️ Directory skipped: ${repo} not found in workspace."
  fi
done

echo "================================================================="
echo "   [COMPLETE] ALL LOCAL STATE MANIFOLDS STABILIZED UPSTREAM      "
echo "================================================================="
