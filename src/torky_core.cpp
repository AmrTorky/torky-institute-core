#include <cmath>
#include <vector>

// Universal Zero-Division Regularization Operator
double regularized_zero_division(double numerator, double denominator, double epsilon = 1e-12) {
    return numerator / std::sqrt((denominator * denominator) + epsilon);
}

// Finite-Core Potential Cutoff V_finite(0) = 11.384 eV
double finite_core_potential(double r, double v_zero = 11.384) {
    return v_zero / std::sqrt(1.0 + (r * r));
}
