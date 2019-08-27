# Applied Data Science from University of Michigan - Coursera
Specialization: https://www.coursera.org/specializations/data-science-python

## TODO
- [x] Course 1: Introduction to Data Science with Python
- [ ] Course 2: Applied Plotting, Charting & Data Representation
- [ ] Course 3: Applied Machine Learning
- [ ] Course 4: Applied Text Mining
- [ ] Course 5: Applied Social Network Analysis

## How to download Jupyter notebook from the course
1. Open https://bmezydqoczesyhncakuvix.coursera-apps.org/tree
2. Select file one by one, then click download

## Download whole directory (optional)
Source: https://github.com/jupyter/notebook/issues/3092

> Content of dog-project folder are-
> 1>Dogproject.ipynb
> 2>dogimages folder
> .
> .some other usefull files

Now you want to zip the dog-project folder.

1. Click on the orange Jupyter circle on the top left of the workspace(`Dogproject.ipynb`).
2. You will see `dog-project folder`. Now don't go inside it.
3. Open Terminal by Clicking New(look right ) -> Terminal.
4. Zip the dog-project folder with the following command in the terminal: `zip -r dog-project.zip dog-project`
5. Alternatively one can use tar command if zip is not available: `tar czf dog-project.tar.gz dog-project`

## Course 1: Introduction to Data Science with Python
https://www.coursera.org/learn/python-data-analysis

### Interesting Quiz question
Given a 6x6 NumPy array r, which of the following options would slice the shaded elements?

Shaded elements is `[0, 7, 14, 21, 28, 35]`
```python
import numpy as np
r = np.array([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29], [30, 31, 32, 33, 34, 35]])
```

Solution:
```python
r.reshape(36)[::7]
```

## Course 2: Applied Plotting, Charting & Data Representation
https://www.coursera.org/learn/python-plotting

TODO

## Course 3: Applied Machine Learning
https://www.coursera.org/learn/python-machine-learning

TODO

## Course 4: Applied Text Mining
https://www.coursera.org/learn/python-text-mining

TODO

## Course 5: Applied Social Network Analysis
https://www.coursera.org/learn/python-social-network-analysis

TODO
