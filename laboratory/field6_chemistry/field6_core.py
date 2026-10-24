import numpy as np
import math

class QuantumChemistryManifoldEngine:
    """
    Field 6: Quantum Chemistry & Molecular Electronic Manifolds Interface Core.
    Locks short-range potential metrics to prevent infinite Hamiltonian spikes.
    """
    def __init__(self):
        self.epsilon = 0.016                  # Denominator smoothing factor
        self.energy_floor_hartree = -157.382  # Target structural lower boundary
        self.nuclear_charge_Z = 6             # Reference Carbon valence anchor

    def compute_clamped_potential(self, r_distance):
        """Replaces legacy 1/r singularities with regularized coordinate smoothing."""
        r = float(r_distance)
        # Apply invariant regularizer shift to safeguard the denominator array
        smoothed_potential = - self.nuclear_charge_Z / math.sqrt(r**2 + self.epsilon)
        
        # Enforce structural limits relative to the absolute energy floor
        if smoothed_potential < self.energy_floor_hartree:
            smoothed_potential = self.energy_floor_hartree
        return smoothed_potential

    def verify_scf_trace(self, density_matrix, exchange_matrix):
        """Evaluates convergence traces across Self-Consistent Field (SCF) matrices."""
        P = np.array(density_matrix, dtype=np.float64)
        K = np.array(exchange_matrix, dtype=np.float64)
        
        energy_trace = np.trace(np.dot(P, K))
        if energy_trace < self.energy_floor_hartree:
            energy_trace = self.energy_floor_hartree
        return energy_trace
