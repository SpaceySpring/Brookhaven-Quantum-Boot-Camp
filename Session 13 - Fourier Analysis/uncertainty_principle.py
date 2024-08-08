# uncertainty_principle.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def f(x):
    # The Gaussian standard normal probability density function
    return (
        1
        / (sigma * np.sqrt(2 * np.pi))
        * np.exp((-1 / 2) * np.power(x, 2) / (np.power(sigma, 2)))
    )


def plot_samples(ts, ys, ax):
    global wave_pdf
    (wave_pdf,) = ax.plot(ts, ys, animated=True)
    ax.set_title("Particle Location (Probability Density)")
    ax.set_xlabel("Distance", loc="right")
    ax.set_ylabel("Probability Density")
    ax.set_ylim(0, 25)


def plot_powerspec(ps, ax):
    global wave_ps
    (wave_ps,) = ax.plot(range(len(ps)), ps, color="green", animated=True)
    ax.set_title("Particle Frequencies")
    ax.set_xlabel("Frequency", loc="right")
    ax.set_ylabel(r"$\Vert Amplitude\Vert$")
    ax.set_ylim(0, 1)


def anim_frame_counter():
    global sigma
    n = 1
    while n < 1200:
        sigma = 10 / n if n <= 600 else 10 / (1200 - n)
        n += 1
        yield n


def anim_draw_frame(t):
    global sigma
    ys = f(ts)
    wave_pdf.set_data(ts, ys)

    sigma /= 30
    ys = f(ts)
    ca = np.fft.rfft(ys) / 2
    ps = np.abs(ca) / len(ca)

    wave_ps.set_data(range(len(ps)), ps)

    return (
        wave_pdf,
        wave_ps,
    )


def main():
    global ts, sigma, anim

    ts = np.linspace(-1, 1, 1000, endpoint=False)

    sigma = 1
    ys = f(ts)

    ca = np.fft.rfft(ys) / 2
    ps = np.abs(ca) / len(ca)

    plt.figure(Path(__file__).name, figsize=(12, 4), constrained_layout=True)

    ax_pdf = plt.subplot(1, 2, 1)
    ax_ps = plt.subplot(1, 2, 2)

    plot_samples(ts, ys, ax_pdf)
    plot_powerspec(ps, ax_ps)

    # fmt: off
    anim = FuncAnimation(ax_pdf.figure,
        anim_draw_frame, anim_frame_counter, interval=25,
        cache_frame_data=False, blit=True, repeat=False)
    # fmt: on

    plt.show()


main()

"""
Q1. Why do the Fourier Transform frequencies spread out as we more tightly confine where the particle is likely to be found?
Answer_1. We are giving up accuracy for detection. This is us giving up knowing the momentum but we wil find the precise location. 

Q2. At the end of the animation, when the Power Spectrum shows only one frequency, why does the probability of finding the particle at any point 𝑥 spread out infinitely?
Answer_2. This is because its the reverse exchange of knowing the momentum instead of an exact point. The particle can be anywhere.

Q3. Do you believe a particle with 100% exactly known momentum could potentially exist anywhere in the universe – why or why not?
Answer_3. I think yes and no but I agree more toward yes because we know how fat it goes and what we can do is set up detectors in places we dont expect it to be.
When its picked up we know that it was there and that it can be anywhere without us looking at it
"""
