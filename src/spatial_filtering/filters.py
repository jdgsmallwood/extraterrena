from abc import ABC, abstractmethod

import numpy as np


class Filter(ABC):
    """Takes in an array covariance matrix and returns
    a corrected array covariance matrix.
    """

    @abstractmethod
    def filter(
        self,
        acm: np.array,
    ): ...


class NullEigenvalueFilter(Filter):
    def filter(self, acm: np.array):
        eigenvalues, eigenvectors = np.linalg.eigh(acm)
        eigenvalues[-1] = 0
        return eigenvectors @ np.diag(eigenvalues) @ eigenvectors.conj().T


class ShrinkEigenvalueFilter(Filter):
    def filter(self, acm: np.array):
        eigenvalues, eigenvectors = np.linalg.eigh(acm)
        eigenvalues[-1] = np.mean(eigenvalues[:-1])
        return eigenvectors @ np.diag(eigenvalues) @ eigenvectors.conj().T
