import numpy as np
import matplotlib.pyplot as plt

from spatial_filtering import arrays, constants


def simulate_linear_array_construct(
    num_antennas: int,
    f: float,
    theta_deg: list[float],
    amplitude: float,
    time_points=np.ndarray,
    sigma: float = 0.5,
) -> np.ndarray:
    """Constructs a uniform linear array with num_antennas elements and spacing of wavelength / 2. Then simulates a series of signals from different directions
    and returns raw voltage data at each antenna.

    """
    wavelength = constants.c / f

    d = wavelength / 2
    array = arrays.UniformLinearArray(num_antennas, d)
    return simulate_linear_array(array, f, theta_deg, amplitude, time_points, sigma)


def simulate_linear_array(
    array: arrays.Array,
    f: float,
    theta_deg: list[float],
    amplitude: float,
    time_points: np.ndarray,
    sigma: float = 0.5,
) -> np.ndarray:
    """Simulates a signal hitting a uniform linear array from an angle theta."""

    wavelength = constants.c / f
    if not isinstance(theta_deg, list) and not isinstance(theta_deg, np.ndarray):
        theta_deg = [theta_deg]

    signal = amplitude * np.exp(1j * 2 * np.pi * f * time_points)

    output = np.zeros((array.num_antennas, time_points.shape[0]), dtype=np.complex128)

    for theta in theta_deg:
        theta_rad = np.deg2rad(theta)
        steer_vec = array.steering_vector(theta_rad, wavelength)
        voltages = steer_vec[np.newaxis].T @ signal[np.newaxis]

        output += voltages

    noise = np.random.multivariate_normal(
        np.zeros(array.num_antennas),
        np.diag(np.ones(array.num_antennas) * sigma),
        time_points.shape[0],
    ).T
    return output + noise
