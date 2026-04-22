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
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from position import Position
from simulated_vehicle import create_simulated_vehicle
from visualizer import create_visualizer

def generate_launch_description():
    
    # map_image_folder = os.path.abspath(
        # os.path.join(launch_file_dir, "../assets/maps/"))

    return LaunchDescription([
        *create_visualizer(
            whitelist=["ego_vehicle"],
            # asset_folder=map_image_folder,
            visualization_offset=(606440.120, 5797321.700),
        ),

        *create_simulated_vehicle(
            namespace="ego_vehicle",
            start_pose=(583266.7740, 5806405.922, 2.0),
            v2x_id=0,
            vehicle_id=111,
            controller=1,
            map_file="r2s_flightfield_edemissen_26022026_25832.r2sr",
        ),
    ])
