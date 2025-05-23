import numpy as np
import polars as pl
from spatial_filtering import arrays


class MUSICDOA:
    """Uses the MUSIC algorithm to return sensitivities to particular directions.  
    
    
    """
    def get_directions(
        self, array: arrays.Array, acm: np.ndarray, num_interferers: int, wavelength: float
    ) -> pl.DataFrame:
        _, evecs = np.linalg.eigh(acm)
        theta_range = np.linspace(-90, 90, 1000)

        output = []
        for theta in theta_range:
            steer_vec = array.steering_vector(np.deg2rad(theta), wavelength).T
            Q = 1 / np.abs(
                steer_vec.conj().T
                @ evecs[:, :-num_interferers]
                @ evecs[:, :-num_interferers].conj().T
                @ steer_vec
            )
            output.append(Q)
        output = np.array(output)
        output = 10 * np.log10(np.abs(output) / np.max(np.abs(output)))  # convert to dB
        
        df = pl.DataFrame({
            "theta_deg": theta_range,
            "q_db": output
        })
        return df