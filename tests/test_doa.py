import numpy as np 
import polars as pl
import pytest
import random

from spatial_filtering import arrays, constants, simulation, direction_of_arrival


class TestMusicDoA:

    def test_music_doa_output_format(self):
        np.random.seed(42)

        f = 1e9 
        wv = constants.c / f
        array = arrays.UniformLinearArray(10, wv / 2)


        X = simulation.simulate_linear_array(array, f, [30], 10, np.linspace(0,10, 100), sigma = 0.1)

        acm = np.cov(X)

        df = direction_of_arrival.MUSICDOA().get_directions(array, acm, 1, wv) 
        assert isinstance(df, pl.DataFrame)
        assert len(df.columns) == 2
        assert df.columns == ["theta_deg", "q_db"]

        assert np.isclose(df.sort('q_db', descending=True)["theta_deg"][0], 30.0)
