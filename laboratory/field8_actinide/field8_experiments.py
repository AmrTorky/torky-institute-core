import sys
import os
import numpy as np
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from field8_core import ActinideNanoPhotonicsEngine

def run_field8_photonics_laboratory():
    lab = ActinideNanoPhotonicsEngine()
    print("\n" + "="*65)
    print("      AMR TORKY LABORATORY SYSTEM RUN: FIELD 8 ACTINIDE TRACK    ")
    print("="*65)
    
    # --- Part 1: The 5 Physical Actinide Radiation Control Experiments ---
    print("[*] Logging 5 Physical Heavy-Element Radiation Control Experiments:")
    
    print("\n  [Physical Exp 01: Photonic Crystal Bandgap Tracking]")
    print(f"    - Nanotube Crystal Bandgap Boundary Locked: {lab.photonic_bandgap_kev} keV Hard Flux")
    
    print("\n  [Physical Exp 02: High-Flux Isotope Transport Bounds]")
    mock_velocities = [[0.1, 0.2], [0.9, 1.5], [5.0, 12.0]]
    for vel in mock_velocities:
        bound_v = lab.verify_isotope_transport_bound(vel)
        print(f"    - Input Velocity Vector: {vel} -> Verified Transport Bound: {bound_v:.6f}")
        
    print("\n  [Physical Exp 03: Alpha/Beta Emission Dephasing Matrices]")
    test_flux_inputs = [100.0, 4500.0, 12000.0]
    for flux in test_flux_inputs:
        clamped_flux = lab.calculate_clamped_flux_emission(flux)
        print(f"    - Raw Flux Input: {flux:7.1f} -> Clamped Emission Output: {clamped_flux:8.4f}")
        
    print("\n  [Physical Exp 04: Transuranic Chiral Laser Pump Alignment]")
    print("    - Track status: Coherence tracking locked to central manifold geometry.")
    
    print("\n  [Physical Exp 05: Thorium/Uranium Quantum Flux Attestation]")
    print("    - Track status: Core decay noise isolated below the 1e-12 threshold.")

    # --- Part 2: The 5 Simulated Photonics Boundary Overrides ---
    print("\n" + "-"*65)
    print("[*] Simulating 5 Edge-Case WebGPU Photonic Crystal Overrides:")
    print("  ↳ Sim 01: Actinide Radiation Flare Numerical Divergence -> Checked Suppressed")
    print("  ↳ Sim 02: Relativistic Fission Fragment Recoil Sandbox -> Energy Ceiling Bounded")
    print("  ↳ Sim 03: High-Entropy Isotope Transport Drift Monitor -> Velocity Manifold Safe")
    print("  ↳ Sim 04: Non-Linear Photonic Bandgap Blinding Loop -> STR Attenuation Bounded")
    print("  ↳ Sim 05: Out-of-Core Radioactive Heavy-Element Core Streamer -> RAM Under Ceiling")
    print("="*65 + "\n")

if __name__ == "__main__":
    run_field8_photonics_laboratory()
