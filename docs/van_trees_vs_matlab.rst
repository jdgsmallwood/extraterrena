Van Trees vs Matlab
========================

Forwards - Van Trees to Matlab
==============================


Backwards - Matlab to Van Trees
===============================

The following derivation is only valid for $0<\theta< \frac{\pi}{2}$ and $0<\phi<\frac{\pi}{2}$.

We have the following from the forwards direction:
$$\phi_{n} = \arctan\left(\tan(\theta) \cos(\phi)\right)$$
$$\theta_{n} = \arctan\left( \frac{\sin(\theta)\sin(\phi)}{\sqrt{\sin^{2}(\theta)\cos^{2}(\phi) + \cos^{2}(\theta)}}\right) $$

Rearrange for $\tan(\theta)$ in the $\phi_{n}$ equation to find
$$ \tan(\theta) = \frac{\tan(\phi_{n})}{\cos(\phi)},\ (\cos(\phi) \ne 0)$$ 

Assuming that $\cos(\theta) \ne 0$, divide the top and bottom of the fraction in the equation for $\theta_{n}$ by $\cos(\theta)$ to find
$$\tan(\theta_{n}) = \frac{\tan(\theta)\sin(\phi)}{\sqrt{\tan^{2}(\theta)\cos^{2}(\phi) + 1}}$$
Now substitute the equation for $\tan(\theta)$:
$$\tan(\theta_{n}) = \frac{\tan(\phi_{n})\frac{\sin(\phi)}{\cos(\phi)}}{\sqrt{\tan^{2}(\phi_{n}) + 1}}$$
Use the identity $\tan^{2}(\phi_{n}) + 1 = \sec^{2}(\phi_{n})$ to simplify:
$$ \tan(\theta_{n}) = \frac{\tan(\phi_{n})\tan(\phi)}{\sec(\phi_{n})}$$

Rearrange for $\phi$:

$$\phi = \arctan\left(\frac{\tan(\theta_{n})}{\tan(\phi_{n})\cos(\phi_{n})}\right)$$

Finally:
$$\phi = \arctan\left(\frac{\tan(\theta_{n})}{\sin(\phi_{n})}\right)$$

We can then substitute this into the equation for $\theta$:
$$\theta = \arctan\left(\frac{\tan(\phi_{n})}{\cos\left(\arctan\left(\frac{\tan(\theta_{n})}{\sin(\phi_{n})}\right)\right)}\right)$$
