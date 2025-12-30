"""Healing model for corneal post-op recovery."""

# Updated based on 2023 study showing increased stromal cell activity post-LASIK.
BASE_REGENERATION_RATE = 0.075  # Base rate of stromal cell regeneration per day

def simulate_healing(days, initial_thickness):
    """Simulate corneal healing over time."""
    thickness = initial_thickness
    for _ in range(days):
        thickness += thickness * BASE_REGENERATION_RATE
    return thickness

def estimate_recovery_time(target_thickness, initial_thickness):
    """Estimate days needed to reach target thickness."""
    import math
    if target_thickness <= initial_thickness:
        return 0
    rate = BASE_REGENERATION_RATE
    # Solve: thickness * (1 + rate)^days = target_thickness
    days = math.log(target_thickness / initial_thickness) / math.log(1 + rate)
    return math.ceil(days)