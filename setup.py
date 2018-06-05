#! /usr/bin/env python
# -*- coding: utf-8 -*-

# package: lie_ti
# file: setup.py
#
# Part of ‘lie_ti’, a package providing molecular docking functionality
# for the LIEStudio package.
#
# Copyright © 2018 Valerio Ferrario, Institute of Biochemistry and Technical Biochemistry
# University of Stuttgart, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

distribution_name = 'lie_ti'

setup(
    name=distribution_name,
    version=0.2,
    description='MDStudio Thermodynamic Integration using Gromacs',
    author="""
    Valerio Ferrario - Institute of Biochemistry and Technical Biochemistry - Stuttgard
    Marc van Dijk - VU University - Amsterdam
    Paul Visscher - Zefiros Software (www.zefiros.eu)
    Felipe Zapata - eScience Center (https://www.esciencecenter.nl/)""",
    author_email=['valerio.ferrario@itb.uni-stuttgart.de', 'm4.van.dijk@vu.nl', 'f.zapata@esciencecenter.nl'],
    url='https://github.com/MD-Studio/MDStudio',
    license='Apache Software License 2.0',
    keywords='MDStudio molecular-simulation TI Thermodynamic-integration ',
    platforms=['Any'],
    packages=find_packages(),
    package_data={'lie_ti': ['data/*']},
    py_modules=[distribution_name],
    install_requires=['cerise_client', 'numpy', 'panedr', 'retrying'],
    extras_require={'test': ['coverage']},
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
    ],
    scripts=['scripts/getEnergies.py']
)
