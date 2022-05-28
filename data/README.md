# Data
This folder contains all the data we took during our lab session.
- The data in the [pi](https://github.com/P2-718na/fresnel-coefficients-experiment/tree/master/data/pi)
  folder was recorded with the laser beam polarised _parallel to the
  plane of incidence_.
- The data in the [sigma](https://github.com/P2-718na/fresnel-coefficients-experiment/tree/master/data/sigma)
  folder was recorded with the laser beam polarised _perpendicular to the plane of incidence_.

For a quick reference, look at these images [_Mazzoldi_, 1998] :

|            pi polarisation            |             sigma polarisation              |
|:-------------------------------------:|:-------------------------------------------:|
| ![pi](../assets/pi-polarisation.jpeg) | ![sigma](../assets/sigma-polarisation.jpeg) |

## Datasets
### pi
- [sim.csv](pi/sim.csv): simulated data generated using _ROOT_. Parameters: `n1 = 1`, `n2 = 1.509`, `I_0 = 950`.
- [run1.csv](pi/run1.csv): first test run with lab equipment. Data logged with _Python_. Parameters: `step = 5°`.
- [run2.csv](pi/run2.csv): second test run with lab equipment. Data logged with _Python_. Parameters: `step = 5°`.
- [run3.csv](pi/run3.csv): third run with lab equipment. Data logged with _Python_. Parameters: `step = 2°`.
- [run3-manual.csv](pi/run3-manual.csv): third run with lab equipment. Data logged by hand. Parameters: `step = 2°`.
- [run3-adjusted.csv](pi/run3-adjusted.csv): Adjusted third run, accounting for errors on the y-axis and initial
  angle offset (`7°`). Part of this data (tail, from `31°` included) is taken from `run3.csv`. The
  rest is taken from `run3-manual.csv`, to account for (most likely) corrupted data.
- [run3-parabola.csv](pi/run3-parabola.csv): Data used for parabolic fit of Brewster's angle. Taken from `run3-adjusted.csv`
- [run3-normalised.csv](pi/run3-normalised.csv): Normalised data from `run3-adjusted.csv` using best fit from Mathematica.

### sigma
- [sim.csv](sigma/sim.csv): simulated data with parameters: `n1 = 1`, `n2 = 1.509`, `I_0 = 950`.
- [run1.csv](sigma/run1-adjusted.csv): first run with lab equipment. Data logged with _Python_. Parameters: `step = 2°`.
- [run1-manual.csv](sigma/run1-manual.csv): first run with lab equipment. Data logged by hand. Parameters: `step =
  2°`.
- [run1-adjusted.csv](sigma/run1-manual.csv): Adjusted first run, accounting for errors on the y-axis and initial
  angle offset (`7°`).
- [run1-normalised.csv](pi/run1-normalised.csv): Normalised data from `run1-adjusted.csv` using best fit from Mathematica.
