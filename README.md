iris
====

Artificial neural network project for Machine Learning (CAP5610)

Getting Started
---

1. Clone the repository.
2. Run `python iris.py`

Files
---

Below are the files of importance within the project.

```
/iris
|- basket.py - a helper script
|- iris.data - the Iris datset
+- iris.py - the entry point for the ANN
```

Algorithm
---

Below is the algorithm for training the artificial neural network.

1. Find the weighted sum.

![weighted sum](http://www.sciweavers.org/tex2img.php?eq=S%3D%5Csum_%7Bi%3D1%7D%5E%7B4%7Dw_ix_i&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0)

2. Apply the sigmoid function (where x = S computed above).

![sigmoid function](http://www.sciweavers.org/tex2img.php?eq=%5Csigma%28x%29%20%3D%20%5Cfrac%7B1%7D%7B1%2Be%5E%7B-x%7D%7D&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0)

3. Compute the error gradient (where d is the desired value).

![error gradient](http://www.sciweavers.org/tex2img.php?eq=%20%5Cdelta%20%3D%20%5Csigma%281-%5Csigma%29%28d%20-%20%5Csigma%29&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0)

4. Update the weights.

![update weights](http://www.sciweavers.org/tex2img.php?eq=w_i%20%3D%20w_i%20%2B%20%5Calpha%20%5Ccdot%20x_i%20%5Ccdot%20%5Cdelta&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0[/img])
