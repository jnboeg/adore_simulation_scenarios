# ********************************************************************************
# Copyright (c) 2025 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0
#
# SPDX-License-Identifier: EPL-2.0
# ********************************************************************************

from launch import LaunchDescription
from launch_ros.actions import Node

import os
import sys
sys.path.append(os.path.dirname(__file__)) # this line is very importatnt to find the helper functions

from position import Position
from simulated_rosmaster import create_simulated_vehicle
from visualizer import create_visualizer

start_position = Position(lat_long=(52.40210384485703798, 10.22701509921937557), psi=-3.0)
goal_position = Position(lat_long=(52.40202537485703971, 10.22653251921937567), psi=0.0)

def generate_launch_description():
    return LaunchDescription([
        *create_simulated_vehicle(
            namespace="ego_vehicle",
            # start_pose_utm=(583266.7740, 5806405.922, 2.0),
            start_pose_utm=start_position.get_utm_coordinates(),
            goal_position_utm=goal_position.get_utm_coordinates(),
            v2x_id=0,
            vehicle_id=111,
            map_file="r2s_scaled_flightfield_edemissen_27042026_25832.r2sr",
        ),
        *create_visualizer(
            whitelist=["ego_vehicle"],
            # asset_folder=map_image_folder,
            # visualization_offset=(606440.120, 5797321.700),
            visualization_offset=start_position.get_utm_coordinates(),
        ),
    ])
