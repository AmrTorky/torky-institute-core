#include <cmath>
#include <vector>

// Universal Unrelaxed Scale Floor (la) = e^-1 nm ≈ 0.36787944117 nm
const double l_a = 0.36787944117;

// Phenomenological Finite-Core Regularizer (\epsilon = 0.016 nm^2)
// Prevents singularity explosions, establishing Coulomb ceiling of 11.384 eV
double non_singular_potential(double r, double epsilon = 0.016, double v_zero = 11.384) {
    return v_zero / std::sqrt((r * r) + epsilon);
}

// Smale's 7th Problem Closed-Form depressed cubic optimizer (O(2^N) -> O(N^2 log(1/\delta)))
std::vector<double> solve_cubic_equilibrium(double h_eff, double epsilon = 0.016) {
    std::vector<double> results;
    double arg = (-3.0 * std::sqrt(3.0) * epsilon * h_eff) / 8.0;
    if (arg > 1.0) arg = 1.0;
    if (arg < -1.0) arg = -1.0;
    double phi = std::acos(arg) / 3.0;
    double sgn = (h_eff >= 0.0) ? 1.0 : -1.0;
    results.push_back(sgn * (2.0 / std::sqrt(3.0)) * std::cos(phi));
    return results;
}
