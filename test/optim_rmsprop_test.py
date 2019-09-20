#!/usr/bin/env python3

import unittest
from test.generic.optim_test_util import TestOptimizer

from classy_vision.optim.rmsprop import RMSProp


class TestRMSPropOptimizer(TestOptimizer, unittest.TestCase):
    def _get_config(self):
        return {
            "name": "rmsprop",
            "num_epochs": 90,
            "lr": 0.1,
            "momentum": 0.9,
            "weight_decay": 0.0001,
            "alpha": 0.9,
            "eps": 1e-8,
            "centered": False,
        }

    def _instance_to_test(self):
        return RMSProp