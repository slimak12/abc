#!/usr/bin/env python

# ---- IMPORT MODULE(S)
from distutils.core import setup

# ---- SETUP INFORMATION
setup(name         = "bee_colony",
      version      = "x.x.x",
      description  = "Artificial Bee Colony Algorithm",
      author       = "Romain Wuilbercq",
      author_email = "romain.wuilbercq@gmail.com",
      keywords     = ["optimisation", "swarm", "stochastic", "global"],
      classifiers  = [
          "Programming Language :: Python",
          "Development Status :: Beta",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3"
      ],
      long_description = """

      The Artificial Bee Colony (ABC) algorithm is based on the
      intelligent foraging behaviour of honey bee swarm, and was first proposed
      by Karaboga in 2005.

      """)
