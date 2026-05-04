## Cause and Effect

_Correlation does not imply causation._

## Cause and Effect

**Correct Cause and Effect**

> People are more likely to carry umbrellas on rainy days. _Therefore, rainy
> days cause people to carry umbrellas._

## Cause and Effect

**Reverse Causality**

> People are more likely to carry umbrellas on rainy days. _Therefore, carrying
> umbrellas causes rain._

## Cause and Effect

**Common Cause**

> People are more likely to carry umbrellas on days when they wear rain jackets.
> _Therefore, carrying umbrellas causes people to wear rain jackets._

## Historical Example

> A historical example of this is that Europeans in the Middle Ages believed
> that lice were beneficial to health since there would rarely be any lice on
> sick people. The reasoning was that the people got sick because the lice left.
> The real reason however is that lice are extremely sensitive to body
> temperature. A small increase of body temperature, such as in a fever, makes
> the lice look for another host. The medical thermometer had not yet been
> invented and so that increase in temperature was rarely noticed. Noticeable
> symptoms came later, which gave the impression that the lice had left before
> the person became sick.

https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation

## Spurious Correlations

**Names and Hydropower**

![](https://www.tylervigen.com/spurious/correlation/image/1519_popularity-of-the-first-name-aria_correlates-with_hydopower-energy-generated-in-equatorial-guinea.png)

## Spurious Correlations

**Degrees and Corn**

![](https://www.tylervigen.com/spurious/correlation/image/1254_masters-degrees-awarded-in-education_correlates-with_gmo-use-in-corn-grown-in-ohio.png)

## Spurious Correlations

**Memes and Statisticians**

![](https://www.tylervigen.com/spurious/correlation/image/7036_popularity-of-the-distracted-boyfriend-meme_correlates-with_the-number-of-statisticians-in-new-jersey.png)

## Spurious Correlations

**Milk and Burglary**

![](https://www.tylervigen.com/spurious/correlation/image/1036_milk-consumption_correlates-with_burglary-rates.png)

## Base Rate Neglect

https://en.wikipedia.org/wiki/Base_rate_fallacy

> A type of fallacy in which people tend to ignore the base rate (e.g., general
> prevalence) in favor of the individuating information (i.e., information
> pertaining only to a specific case).

## Base Rate Neglect

**Example: Breathalyzer Accuracy**

Imagine you stop a random driver on the road and have them take a breathalyzer
test. The test comes back positive. How much information does this result give
you that the driver is in fact drunk?

In this scenario, let's say:

- Breathalyzers are have a `5%` false positive rate (`5` in `100` sober drivers
  will test positive; `95` in `100` sober drivers will test negative).

- Breathalyzers are have a `0%` false negative rate (`100` in `100` drunk
  drivers will test positive).

- At any given time, `0.1%` of drivers on the road are drunk.

## Base Rate Neglect

Do the math out for `100000` drivers:

|                      |                    Sober |                  Drunk |    Total |
| -------------------- | -----------------------: | ---------------------: | -------: |
| Count                | `100000 * 0.999 = 99900` | `100000 * 0.001 = 100` | `100000` |
| Positive             |    `99900 * 0.05 = 4950` |     `100 * 1.00 = 100` |   `5050` |
| Percent of positives |  **`4950 / 5050 = 98%`** |  **`100 / 5050 = 2%`** |          |

## Simpsons Paradox

https://en.wikipedia.org/wiki/Simpson%27s_paradox

> Simpson's paradox is a phenomenon in probability and statistics in which a
> trend appears in several groups of data but disappears or reverses when the
> groups are combined. This result is often encountered in social-science and
> medical-science statistics, and is particularly problematic when frequency
> data are unduly given causal interpretations.

|          |              Avery |        Steph Curry |
| -------- | -----------------: | -----------------: |
| Saturday |   **`1/1 = 100%`** |     `90/99 = ~90%` |
| Sunday   | **`16/99 = ~16%`** |         `0/1 = 0%` |
| Combined |     `17/100 = 17%` | **`90/100 = 90%`** |

## Simpsons Paradox

https://en.wikipedia.org/wiki/Simpson%27s_paradox

> Simpson's paradox is a phenomenon in probability and statistics in which a
> trend appears in several groups of data but disappears or reverses when the
> groups are combined. This result is often encountered in social-science and
> medical-science statistics, and is particularly problematic when frequency
> data are unduly given causal interpretations.

|              |         Treatment A |         Treatment B |
| ------------ | ------------------: | ------------------: |
| Small stones |   **`81/87 = 93%`** |     `234/270 = 87%` |
| Large stones | **`192/263 = 73%`** |       `55/80 = 69%` |
| Both         |     `273/350 = 78%` | **`289/350 = 83%`** |
