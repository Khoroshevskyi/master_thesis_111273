# This file contain scripts for over and under sampling
# 1. Oversampling
# w. Undersmapling

from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
import pandas as pd
from typing import List


def apply_oversampling(x: pd.DataFrame, y: pd.DataFrame):
    """
    Apply oversampling
    :param x: DataFrame of x
    :param y: DataFrame of y
    :return: oversampled X and y
    """
    x_class = x

    smote = SMOTE(random_state=101)
    x_class, label_y = smote.fit_resample(x_class, y)
    return x_class, label_y


def apply_undersampling(x: pd.DataFrame, y: pd.DataFrame):
    """
    Apply undersampled
    :param x: DataFrame of x
    :param y: DataFrame of y
    :return: Undersampled X and y
    """
    x_class = x

    undersample = RandomUnderSampler(sampling_strategy='majority')
    x_class, label_y = undersample.fit_resample(x_class, y)

    return x_class, label_y


def return_same(x: pd.DataFrame, y: pd.DataFrame):
    """
    Return as it is.
    :param x: DataFrame of x
    :param y: DataFrame of y
    :return: x, y
    """
    return x, y


sampling_func = {
    "no_sampling": return_same,
    "oversampling": apply_oversampling,
    "undersampling": apply_undersampling,
}