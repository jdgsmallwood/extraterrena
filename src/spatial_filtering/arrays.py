import numpy as np


class Array:
    def __init__(self, positions: np.ndarray):
        if len(positions.shape) == 1:
            positions = positions[:, np.newaxis]

        self.positions = np.array(
            [
                (
                    np.pad(position, (0, 3 - position.shape[0]), mode="constant")
                    if position.shape[0] < 3
                    else position
                )
                for position in positions
            ]
        )

    def steering_vector(
        self, theta_radians: list[float], wavelength: float
    ) -> np.ndarray:
        """
        This should be [az, el]

        Refs:
        https://www.antenna-theory.com/definitions/wavevector.php
        https://www.antenna-theory.com/definitions/steering.php
        """
        phi, theta = theta_radians

        return np.array(
            [
                np.exp(
                    -1.0j
                    * 2
                    * np.pi
                    * np.dot(
                        np.array(
                            [
                                np.sin(theta) * np.cos(phi),
                                np.sin(theta) * np.sin(phi),
                                np.cos(theta),
                            ]
                        ),
                        positions,
                    )
                    / wavelength
                )
                for positions in self.positions
            ]
        ).astype(np.complex128)
