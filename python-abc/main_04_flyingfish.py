#!/usr/bin/env python3
"""
This script demonstrates multiple inheritance by using a FlyingFish object
that can both swim and fly, and display its habitat.
"""

from task_04_flyingfish import Fish, FlyingFish

flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()
